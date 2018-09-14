# -*- coding: utf-8 -*-

import os
import json
import subprocess
import uuid


class Task(object):
    """This class defines a processing task"""

    def __init__(self, input_file_path):
        """Task initialization

        :param input_file_path: The input video file path
        :type input_file_path: str
        """
        if os.path.isfile(input_file_path) is True:
            self.input_file_path = input_file_path
        else:
            raise ValueError("Cannot access the file: {}".format(input_file_path))

        self.subprocess_pid = None
        self.subprocess_out = None
        self.subprocess_err = None

    def execute(self, command):
        """Launch a subprocess task

        :param command: Arguments array for the subprocess task
        :type command: List[str]
        """
        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.subprocess_pid = proc.pid

        try:
            self.subprocess_out, self.subprocess_err = proc.communicate()
        except:
            print(self.subprocess_err)
            # TODO: error management
