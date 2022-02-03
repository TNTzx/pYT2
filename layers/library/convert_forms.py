"""Contains convert formats."""


import os
import moviepy.editor as mpy
import proglog as plg
import shutil as shut

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

    def convert(self, original_type: str, original_path: str, original_ext: str, new_path: str, logger: plg.ProgressBarLogger = None):
        """Convert"""
        if original_ext == self.file_ext:
            shut.copy2(original_path, new_path)
            return

        output_path_tup = os.path.split(new_path)
        filename_tup = os.path.splitext(output_path_tup[1])
        new_path = os.path.join(output_path_tup[0], f"{filename_tup[0]}.{self.file_ext}")

        if original_type == ConvertFormat.Types.video:
            clip = mpy.VideoFileClip(original_path)
        elif original_type == ConvertFormat.Types.audio:
            clip = mpy.AudioFileClip(original_path)

        if isinstance(clip, mpy.VideoFileClip):
            if self.type == ConvertFormat.Types.video:
                clip.write_videofile(new_path, logger=logger)
            if self.type == ConvertFormat.Types.audio:
                clip.audio.write_audiofile(new_path, logger=logger)
        elif isinstance(clip, mpy.AudioFileClip):
            if self.type == ConvertFormat.Types.audio:
                clip.write_audiofile(new_path, logger=logger)
            else:
                clip.close()
                raise ConvertError("Cannot convert audio to video.")

        clip.close()


convert_formats = [
    ConvertFormat("mp4", ConvertFormat.Types.video),
    ConvertFormat("mp3", ConvertFormat.Types.audio),
]
