"""Contains the Task class."""


import pytube as yt


class Task():
    """A task."""
    def __init__(
            self,
            stream: yt.Stream,
            convert_form: str,
            output_path: str
            ):
        self.stream = stream
        self.convert_form = convert_form
        self.output_path = output_path

    def download(self):
        """Download the task."""
