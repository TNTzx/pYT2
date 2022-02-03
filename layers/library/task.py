"""Contains the Task class."""


import os
import tempfile as tmp
import typing as typ
import pytube as yt
import moviepy.editor as mpy
import proglog as plg

import layers.library.yt_other as yt_o
import layers.library.convert_forms as c_f


class Task():
    """A task."""
    def __init__(
            self,
            yt_obj: yt.YouTube,
            selected_stream_info: yt_o.StreamInfo = None,
            selected_convert_form: c_f.ConvertFormat = None,
            output_path: str = None,
            ):
        self.yt_obj = yt_obj
        self.selected_stream = selected_stream_info
        self.selected_convert_form = selected_convert_form
        self.output_path = output_path
        self.callbacks = self.Callbacks()

        self.streams_list: list[yt.Stream] = []

    def __repr__(self):
        return (
            f"{self.yt_obj.title} "
            f"({self.selected_convert_form.file_ext}) | "
            f"{self.selected_stream.__repr__()}"
        )

    class Callbacks():
        """Stores callbacks."""
        def __init__(self):
            self.youtube = self.YouTube()
            self.converting = self.Converting()

        class YouTube():
            """Youtube callbacks."""
            def __init__(self):
                self.on_start: typ.Callable = lambda stream, chunk, bytes_remaining: None
                self.on_progress: typ.Callable = lambda stream, chunk, bytes_remaining: None
                self.on_complete: typ.Callable = lambda stream, file_path: None

        class Converting():
            """Converting callbacks."""
            def __init__(self):
                self.on_start: typ.Callable = lambda: None
                self.on_progress: typ.Callable = lambda done, total: None
                self.on_complete: typ.Callable = lambda: None


    def update_streams_list(self):
        """Update the streams list from self.yt_obj."""
        self.streams_list = list(reversed(self.yt_obj.streams.filter(**yt_o.DEFAULT_STREAM_FILTER)))

    def update_selected_stream(self):
        """Updates the selected stream based on self.yt_obj and self.selected_stream."""
        self.selected_stream.stream = self.streams_list[self.selected_stream.idx_from_all_streams]


    def download(self):
        """Download the task."""
        self.yt_obj = yt.YouTube(self.yt_obj.watch_url,
            on_progress_callback=self.callbacks.youtube.on_progress,
            on_complete_callback=self.callbacks.youtube.on_complete
        )
        self.update_streams_list()
        self.update_selected_stream()
        selected_stream = self.selected_stream.stream

        temp_path = (tmp.gettempdir(), f"temp.{selected_stream.subtype}")
        self.callbacks.youtube.on_start(selected_stream, 0, selected_stream.filesize)
        selected_stream.download(temp_path[0], temp_path[1])

        if selected_stream.type == "video":
            clip = mpy.VideoFileClip(os.path.join(*temp_path))
        elif selected_stream.type == "audio":
            clip = mpy.AudioFileClip(temp_path)

        self.callbacks.converting.on_start()

        self_me = self

        class ConvertProgressLogger(plg.ProgressBarLogger):
            """Convert progress logger."""
            def bars_callback(self, bar, attr, value, old_value=None):
                self_me.callbacks.converting.on_progress(value, self.bars[bar]['total'])

        self.selected_convert_form.convert(clip, self.output_path, original_format=selected_stream.subtype, logger=ConvertProgressLogger())
        self.callbacks.converting.on_complete()

        clip.close()
        os.remove(os.path.join(*temp_path))


DEFAULT_TASK = Task(
    yt_o.DEFAULT_YT_OBJ,
    yt_o.StreamInfo(
        yt_o.DEFAULT_YT_OBJ.streams.filter(progressive=True).get_highest_resolution(), 0
    ),
    c_f.convert_formats[1],
    r"E:/[9] dump/a.mp3"
)
