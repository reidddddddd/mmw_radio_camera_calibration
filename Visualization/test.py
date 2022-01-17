import datetime

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import pyexifinfo as p
import json
import os
import subprocess
from subprocess import call
# a = os.system("exiftool -wcg -Date='1234:12:11 13:31:47.123456' ./testData/9e76f967a0b99a93ff2ac622264a97d8.mp4")

# cmd = ['exiftool', '-r', './testData/9e76f967a0b99a93ff2ac622264a97d8.mp4','-Date']
# s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
#
# gg = p.command_line(cmd)
# gg = gg.decode('utf-8').rstrip('\r\n')
# ss = json.load(gg)
# s=str(s)
# print(s.split(':')[1:])
# frame = pd.read_csv("./outData/1/pcl/pcl.csv")
# frame['orginTimestamp'] = frame[' Timestamp']
# tmp = frame['orginTimestamp'].unique()
# frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'], unit='us').apply(
#     lambda x: x + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
# # frame[' Timestamp'].apply(lambda x: x+datetime.timedelta(hours=8))
#
#
# # frame = frame[frame[' ZPos'] >= 0.3]
# # frame = frame[frame[' ZPos'] <= 1.0]
# # frame = frame[frame[' Xpos'] <= 0.5]
# # frame = frame[frame[' Xpos'] >= -0.5]
# # frame = frame[frame[' YPos'] <= 0.3]
# # frame = frame[frame[' YPos'] >= -0.3]
#
# print(frame.count())
#
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(frame[' Xpos'], frame[' YPos'], frame[' ZPos'])
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
#
# plt.show()
#
data = p.get_json("./testData/9e76f967a0b99a93ff2ac622264a97d8.mp4")
print(json.dumps(data, sort_keys=True,
                 indent=4, separators=(',', ': ')))

#
# print(datetime.datetime.strptime(var, "%Y:%m:%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S'))