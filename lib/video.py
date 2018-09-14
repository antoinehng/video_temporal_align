# -*- coding: utf-8 -*-

import os, errno
from math import floor

from .probe import Probe
from .thumbnail import Thumbnail


class Video(object):
    """This class defines a video"""

    def __init__(self, file_path):
        """Video init

        :param file_path: Video file path
        :type file_path: str
        """
        # Check if file exists and is accessible
        if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
            self.file_path = file_path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)

        self._probe()

    def _probe(self):
        probe_task = Probe(self.file_path)
        probe_task.execute()
        self.width = probe_task.width
        self.height = probe_task.height
        self.bitrate = probe_task.bitrate
        self.duration = probe_task.duration
        self.video_codec = probe_task.video_codec
        self.framerate = probe_task.framerate
        self.nb_of_frames = int(floor(self.duration * self.framerate))

    def generate_thumbnail(self, width, height, frame_number):
        time = float(frame_number * self.framerate / 1000)
        thumb_task = Thumbnail(self, width, height, str(time))
        thumb_task.execute()
