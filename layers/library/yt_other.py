"""Other Youtube-related classes."""

import pytube as yt

import layers.library.other_functions as o_f


DEFAULT_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"


class StreamInfo():
    """Includes info for a stream, as well as the Stream object itself."""
    def __init__(self, stream: yt.Stream):
        self.stream = stream

    def __repr__(self):
        return f"({self.stream.mime_type}) {self.stream.resolution} [ {o_f.bytes_to_mb(self.stream.filesize)} MB ]"
