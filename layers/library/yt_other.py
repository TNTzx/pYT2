"""Other Youtube-related stuff."""

import pytube as yt

import layers.library.other_functions as o_f


DEFAULT_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
DEFAULT_YT_OBJ = yt.YouTube(DEFAULT_URL)
DEFAULT_STREAM_FILTER = {
    "progressive": True
}

class StreamInfo():
    """Includes info for a stream, as well as the Stream object itself."""
    def __init__(self, stream: yt.Stream, idx_from_all_streams: int):
        self.stream = stream
        self.idx_from_all_streams = idx_from_all_streams

    def __repr__(self):
        return f"({self.stream.mime_type}) {self.stream.resolution} [ {o_f.bytes_to_mb(self.stream.filesize)} MB ]"
