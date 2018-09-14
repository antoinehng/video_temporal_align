# -*- coding: utf-8 -*-

import json

from .task import *


class Probe(Task):
    """This class defines a Probing task"""

    def __init__(self, input_file_path):
        """Probe initialization

        :param input_file_path: The input video file path
        :type input_file_path: str
        """
        Task.__init__(self, input_file_path)

        self.width = None
        self.height = None
        self.bitrate = None
        self.duration = None
        self.video_codec = None
        self.framerate = None

    def execute(self):
        """Using FFprobe to get input video file informations"""
        command = [
            "ffprobe",
            "-hide_banner",
            "-i",
            self.input_file_path,
            "-show_format",
            "-show_streams",
            "-print_format",
            "json",
        ]
        Task.execute(self, command)

        # Parse output data
        try:
            response = self.subprocess_out
            data = json.loads(response.decode("utf-8"))
            for stream in data["streams"]:
                if stream["codec_type"] == "video":
                    self.width = int(stream["width"])
                    self.height = int(stream["height"])
                    self.bitrate = int(stream["bit_rate"])
                    self.duration = float(stream["duration"])
                    self.video_codec = stream["codec_name"]
                    self.framerate = int(stream["r_frame_rate"].replace("/1", ""))
        except:
            # TODO: error management
            pass
