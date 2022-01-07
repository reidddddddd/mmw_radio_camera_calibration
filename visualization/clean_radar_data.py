import pandas as pd
import numpy as np
def common_read(path):
    frame = pd.read_csv(path)
    frame['originTimestamp'] = frame[' Timestamp']
    frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'] / 1000, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
    print("all times are shown" + frame[' Timestamp'].unique())
    frame['union'] = 1
    return frame

def get_calibration_result(intrinsic_matrix, wwm_extrinsics_matrix, frame):
    posArray = frame[[' Xpos', ' YPos', ' ZPos', 'union']].to_numpy(dtype=float)
    tmp1 = np.dot(posArray, wwm_extrinsics_matrix.T)
    test1 = np.dot(np.dot(posArray, wwm_extrinsics_matrix.T), intrinsic_matrix.T)
    # normalize z axis
    test = np.divide(test1, test1[:, 2].reshape(test1.shape[0], 1))
    return test