# -*- coding: utf-8 -*-

from lib.video import *
from lib.temporal_align import *

v = Video("D:\\Dowloads\\temp_align\\VID_20180824_134138.mp4")

v2 = Video("D:\\Dowloads\\temp_align\\toto.mp4")
v3 = Video("D:\\Dowloads\\temp_align\\toto2.mp4")
lv = []
lv.append(v2)
lv.append(v3)
tempalign = TemporalAlign(v, lv)
tempalign.process()

