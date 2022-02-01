"""Contains convert formats."""


import layers.library.other_functions as o_f


class ConvertFormat():
    """Contains information for a convert format."""
    def __init__(self, file_ext: str, _type: o_f.Unique):
        self.file_ext = file_ext
        self.type = _type

    class Types():
        """Types of convert formats."""
        video = "Video"
        audio = "Audio"

convert_formats = [
    ConvertFormat("mp4", ConvertFormat.Types.video),
    ConvertFormat("mp3", ConvertFormat.Types.audio),
]


def convert_format_to_str(convert_format: ConvertFormat):
    """Converts a ConvertFormat into a string for UI purposes."""
    return f"{convert_format.file_ext} ({convert_format.type})"

convert_format_dict = {
    convert_format_to_str(convert_format): convert_format
    for convert_format in convert_formats
}
