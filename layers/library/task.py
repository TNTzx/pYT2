"""Contains the Task class."""


import pytube as yt

import layers.library.convert_forms as c_f


class Task():
    """A task."""
    def __init__(
            self,
            yt_obj: yt.YouTube,
            selected_stream: str = None,
            selected_convert_form: str = None,
            output_path: str = None
            ):
        self.yt_obj = yt_obj
        self.selected_stream = selected_stream
        self.selected_convert_form = selected_convert_form
        self.output_path = output_path

    def __repr__(self):
        pass


    def download(self):
        """Download the task."""

tasks: list[Task] = []

def get_task_str(task: Task):
    """Returns the string representation of the task."""
