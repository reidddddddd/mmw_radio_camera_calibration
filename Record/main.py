import cv2
import datetime
from subprocess import call

# 初始化摄像头


video_height = 1920
video_width = 1080
frame_per_second = 15
file_name = "video_result.avi"

cap = cv2.VideoCapture(0)  # 生成读取摄像头对象
cap.set(3, video_height)
cap.set(4, video_width)
cap.set(5, frame_per_second)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频的宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频的高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))  # 视频的编码
# 定义视频对象输出
writer = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

record_command =str(datetime.datetime.now())

with open('camera.txt', 'w') as f:
    f.write(record_command)
while cap.isOpened():
    # 采集一帧一帧的图像数据
    isSuccess, frame = cap.read()
    # 实时的将采集到的数据显示到界面上
    if isSuccess:
        cv2.imshow("My Capture", frame)
        writer.write(frame)
        # time.sleep(0.5)
    # 实现按下“q”键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# call(['exiftool', '-wcg', record_command, file_name])
# 释放摄像头资源
writer.release()
cap.release()

