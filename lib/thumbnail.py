# -*- coding: utf-8 -*-

import os
import uuid

from .task import *


class Thumbnail(Task):
    """This class defines a Thumbnail encoding task"""

    def __init__(self, video, width, height, frame_time):
        """Thumbnail task initialization

        :param video: Video object
        :type video: video
        :param width: Width of the thumbnails
        :type width: int
        :param height: Height of the thumbnails
        :type height: int
        :param frame_time: In seconds or hh:mm:ss.ms
        :type frame_time: str
        """
        Task.__init__(self, video.file_path)

        self.definition = f"{width}x{height}"
        self.frame_time = frame_time

        # Generate a temporary file name for the task output
        self.output_file_path = os.path.join(
            os.path.dirname(self.input_file_path),
            os.path.splitext(os.path.basename(self.input_file_path))[0]
            + f"_{self.frame_time}.jpg",
        )

    def execute(self):
        """Using FFmpeg to generate the thumbnail"""
        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "quiet",
            "-nostats",
            "-ss",
            self.frame_time,
            "-i",
            self.input_file_path,
            "-s",
            self.definition,
            "-vframes",
            "1",
            "-y",
            self.output_file_path,
        ]
        Task.execute(self, command)
