"""Contains the Task class."""


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

    def __repr__(self):
        return (
            f"{self.yt_obj.title} "
            f"({self.selected_convert_form.file_ext}) | "
            f"{self.selected_stream.__repr__()}"
        )


    def download(self):
        """Download the task."""
