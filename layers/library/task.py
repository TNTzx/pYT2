"""Contains the Task class."""


import os
import typing as typ
import pytube as yt

import layers.library.yt_other as yt_o
import layers.library.convert_forms as c_f


class Task():
    """A task."""
    def __init__(
            self,
            yt_obj: yt.YouTube,
            selected_stream_info: yt_o.StreamInfo = None,
            selected_convert_form: c_f.ConvertFormat = None,
            output_path: str = None
            ):
        self.yt_obj = yt_obj
        self.selected_stream = selected_stream_info
        self.selected_convert_form = selected_convert_form
        self.output_path = output_path

        self.streams_list: list[yt.Stream] = []

    def __repr__(self):
        return (
            f"{self.yt_obj.title} "
            f"({self.selected_convert_form.file_ext}) | "
            f"{self.selected_stream.__repr__()}"
        )

    def update_streams_list(self):
        """Update the streams list from self.yt_obj."""
        self.streams_list = list(reversed(self.yt_obj.streams.filter(**yt_o.DEFAULT_STREAM_FILTER)))


    def download(
            self,
            on_progress_callback: typ.Callable = lambda stream, chunk, bytes_remaining: None,
            on_complete_callback: typ.Callable = lambda stream, file_path: None,
        ):
        """Download the task."""
        self.yt_obj = yt.YouTube(self.yt_obj.watch_url,
            on_progress_callback=on_progress_callback,
            on_complete_callback=on_complete_callback
        )
        self.update_streams_list()

        path_tup = os.path.split(self.output_path)
        self.streams_list[self.selected_stream.idx_from_all_streams].download(path_tup[0], path_tup[1])


DEFAULT_TASK = Task(
    yt_o.DEFAULT_YT_OBJ,
    yt_o.StreamInfo(
        yt_o.DEFAULT_YT_OBJ.streams.filter(progressive=True).get_highest_resolution(), 0
    ),
    c_f.ConvertFormat("mp3", c_f.ConvertFormat.Types.audio),
    r"E:/[9] dump/a.mp3"
)
