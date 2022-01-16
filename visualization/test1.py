# from exif import Image
#
# # with open('testData/1.png', 'rb') as image_file:
#
# my_image = Image('testData/1.png')
#
# print(my_image.list_all())】
import cv2
import pyexifinfo as p
import json
import pandas as pd
import datetime
import time

# videoCapture = cv2.VideoCapture("./outData/5/2022-01-13-142247.webm")
#
#
# def save_image(image, addr, num):
#     address = addr + str(num) + '.jpg'
#     cv2.imwrite(address, image)
#
#
# # 读帧
# success = True
# i = 0
# while success:
#     success, frame = videoCapture.read()
#     i = i + 1
#     if success:
#         save_image(frame, './outData/image', i)

vidcap = cv2.VideoCapture('./testData/video_result.avi')
fps = vidcap.get(cv2.CAP_PROP_FPS)
success,image = vidcap.read()
count = 0
success = True
print(fps)
while success:
    success,frame = vidcap.read()
    # if success:
        # cv2.imwrite("./testData/11.jpg", frame)
    count+=1
    print("time stamp current frame:",count/fps)


# p.ver()
# data = p.get_json('./outData/5/2022-01-13-142247.webm')
# print(json.dumps(data, sort_keys=True,
#                  indent=4, separators=(',', ': ')))


# frame = pd.read_csv("./testData/pcl.csv")
# frame['originTimestamp'] = frame[' Timestamp']
# frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'], unit='us').apply(
#         lambda x: x + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-6]
#
# aa = frame['originTimestamp'].unique()
# for ele in range(0,aa.shape[0]):
#     print(aa[ele+1] - aa[ele])