"""Contains convert formats."""


import os
import typing as typ
import moviepy.editor as mpy

import layers.library.other_functions as o_f


class ConvertError(Exception):
    """An error has occured in converting."""


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

    def convert(self, clip: mpy.VideoFileClip | mpy.AudioFileClip, output_path: str):
        """Convert"""
        output_path_tup = os.path.split(output_path)
        filename_tup = os.path.splitext(output_path_tup[1])
        new_path = os.path.join(output_path_tup[0], f"{filename_tup[0]}.{self.file_ext}")

        if isinstance(clip, mpy.VideoFileClip):
            if self.type == ConvertFormat.Types.video:
                clip.write_videofile(new_path)
            if self.type == ConvertFormat.Types.audio:
                clip.audio.write_audiofile(new_path)
        elif isinstance(clip, mpy.AudioFileClip):
            if self.type == ConvertFormat.Types.audio:
                clip.write_audiofile(new_path)
            else:
                raise ConvertError("Cannot convert audio to video.")

convert_formats = [
    ConvertFormat("mp4", ConvertFormat.Types.video),
    ConvertFormat("mp3", ConvertFormat.Types.audio),
]
