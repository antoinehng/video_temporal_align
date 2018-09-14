# -*- coding: utf-8 -*-


class Frame(object):
    """This class defines a frame"""

    def __init__(self, position_number, thumbnail_path):
        """Frame init

        :param position_number: Frame position in the video source
        :type position_number: int
        :param thumbnail_path: Thumbnail file path
        :type thumbnail_path: str
        """
        self.position_number = position_number
        # Check if file exists and is accessible
        if os.path.isfile(thumbnail_path) and os.access(thumbnail_path, os.R_OK):
            self.thumbnail_path = thumbnail_path
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), thumbnail_path
            )

