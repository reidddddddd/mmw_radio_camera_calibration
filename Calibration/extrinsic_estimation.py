import numpy as np
import cv2
from Calibration import util


def compute_extrinsics(A, homography):
    util.info("Computing extrinsic parameters...")
    h1 = util.column(homography, 0)
    h2 = util.column(homography, 1)
    h3 = util.column(homography, 2)

    A_inv = np.linalg.inv(A)

    # We have lambda defined in the page 6. h1, h2 or h3 can be used in the calculation of lambda.
    lmbda = 1. / np.linalg.norm(np.dot(A_inv, h1))

    # Compute r1, r2, r3 and t with the values given above.
    r1 = lmbda * np.dot(A_inv, h1)
    r2 = lmbda * np.dot(A_inv, h2)
    # r3 can be calculated with the orthogonality between r1 and r2.
    r3 = np.cross(r1, r2)
    t = lmbda * np.dot(A_inv, h3)

    # Reconstitute the rotation component of the extrinsics and reorthogonalize.
    # R = [r1, r2, r3]
    R = np.vstack((r1, r2, r3)).T
    R = util.reorthogonalize(R)


    # Reconstitute full extrinsics
    E = np.hstack((R, t[:, np.newaxis]))


    util.info("DONE.")

    return E


def compute_wwm_extrinsics(camera_point, radar_points, t):
    # radar_points = np.concatenate((radar_points, np.ones((radar_points.shape[0], 1), np.float32)), axis=1)
    # u = camera_point[:, 0].T
    # v = camera_point[:, 1].T
    # w = radar_points[:, 2].T
    # i = np.ones([1,camera_point.shape[0]])
    # T1 = (np.linalg.inv(radar_points.T.dot(radar_points)).dot(radar_points.T).dot(u.T)).T
    # T2 = (np.linalg.inv(radar_points.T.dot(radar_points)).dot(radar_points.T).dot(v.T)).T
    # T3 = (np.linalg.inv(radar_points.T.dot(radar_points)).dot(radar_points.T).dot(w.T)).T
    # T4 = (np.linalg.inv(radar_points.T.dot(radar_points)).dot(radar_points.T).dot(i.T)).T
    # T = np.vstack((T1, T2, T3, T4))
    # return T
    R = np.identity(3)
    E = np.hstack((R,t[:, np.newaxis]))
    return E
