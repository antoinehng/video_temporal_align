# -*- coding: utf-8 -*-

import os


class TemporalAlign(object):
    """This class defines a temporal align task provider"""

    def __init__(self, video_ref, video_list):
        """TemporalAlign task init

        :param video_ref: Reference video
        :type video_ref: Video
        :param video_list: Video list to be align
        :type video_list: List[Video]
        """
        self.video_ref = video_ref
        self.video_list = video_list

    def process(self):
        """Temporal align process"""

        for ref_idx in range(1, self.video_ref.nb_of_frames + 1):
            self.video_ref.generate_thumbnail(
                self.video_ref.width, self.video_ref.height, ref_idx
            )
            for video in self.video_list:
                for v_idx in range(1, video.nb_of_frames + 1):
                    video.generate_thumbnail(
                        self.video_ref.width, self.video_ref.height, v_idx
                    )
                    break
            break

