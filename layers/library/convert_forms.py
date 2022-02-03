"""Contains convert formats."""


import layers.library.other_functions as o_f


class ConvertFormat():
    """Contains information for a convert format."""
    def __init__(self, file_ext: str, _type: o_f.Unique):
        self.file_ext = file_ext
        self.type = _type

    def __repr__(self):
        return f"{self.file_ext} ({self.type})"

    class Types():
        """Types of convert formats."""
        video = "Video"
        audio = "Audio"

convert_formats = [
    ConvertFormat("mp4", ConvertFormat.Types.video),
    ConvertFormat("mp3", ConvertFormat.Types.audio),
]
