import datetime
import cv2
from cv2.cv2 import CAP_V4L2

if __name__ == "__main__":
    # find the webcam
    capture = cv2.VideoCapture(0)
    fourcc = int(capture.get(cv2.CAP_PROP_FOURCC))
    # video recorder
    video_writer = cv2.VideoWriter("output.wmv", fourcc, 15, (1920, 1080))

    # record video
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            video_writer.write(frame)
            cv2.imshow('Video Stream', frame)

        else:
            break

    capture.release()
    video_writer.release()
    cv2.destroyAllWindows()