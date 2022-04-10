import pandas as pd
import numpy as np
import datetime
from Visualization import util


def common_read(csv_dir: str, picture_dir: str):
    frame = pd.read_csv(csv_dir)
    frame['originTimestamp'] = frame[' Timestamp']
    frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'], unit='us').apply(
        lambda x: x + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    frame = frame[frame[' Timestamp'] == util.read_picture_time(picture_dir)]
    # print("all times are shown" + frame[' Timestamp'].unique())
    frame['union'] = 1
    return frame


def get_calibration_result(intrinsic_matrix, wwm_extrinsics_matrix, frame):
    posArray = frame[[' Xpos', ' YPos', ' ZPos', 'union']].to_numpy(dtype=float)

    test1 = np.dot(np.dot(posArray, wwm_extrinsics_matrix.T), intrinsic_matrix.T)
    # normalize z axis
    test = np.divide(test1, test1[:, 2].reshape(test1.shape[0], 1))
    return test


def inverse_image_point_camera_coor():
    pass