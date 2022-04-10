import numpy as np
import math
import rmsd

method_angles = 'rodrigues'

class optimizer_parameters:
    stopping_tolerance = 1E-6
    maximum_iterations = 1000
    verbosity = False

def vector2rotm(v):
    # Generic function that converts vector to rotation matrix
    # This fucntion is meant as a wrapper for 2 options: euler angles or rodrigues matrix formula
    if method_angles == 'rodrigues':
        return rodrigues2rotm(v)
    elif method_angles == 'euler':
        return eul2rotm(v)
    else:
        print('Error unknown method for vector2rotm conversion')


def rodrigues2rotm(v):
    # https://en.wikipedia.org/wiki/Rotation_matrix

    theta = np.linalg.norm(v)
    if theta == 0:
        R = np.identity(3)
    else:
        v = v / theta
        ux = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
        R = np.cos(theta) * np.identity(3) + np.sin(theta) * ux + (1 - np.cos(theta)) * np.outer(v, v)

    return R


def eul2rotm(euler_angles):
    # Calculates Rotation Matrix (rotm) given euler angles (eul).
    # The results is the same as MATLAB function eul2rotm

    R_x = np.array([[1, 0, 0],
                    [0, math.cos(euler_angles[2]), -math.sin(euler_angles[2])],
                    [0, math.sin(euler_angles[2]), math.cos(euler_angles[2])]
                    ])

    R_y = np.array([[math.cos(euler_angles[1]), 0, math.sin(euler_angles[1])],
                    [0, 1, 0],
                    [-math.sin(euler_angles[1]), 0, math.cos(euler_angles[1])]
                    ])

    R_z = np.array([[math.cos(euler_angles[0]), -math.sin(euler_angles[0]), 0],
                    [math.sin(euler_angles[0]), math.cos(euler_angles[0]), 0],
                    [0, 0, 1]
                    ])

    R = np.dot(R_z, np.dot(R_y, R_x))

    return R


def compute_transformation_matrix(p, q, T0, correspondences, assignment_mode=0):
    if correspondences == 'unknown':
        pass
        # # Unknown correpondences for detections of the calibration board.
        # if assignment_mode == 0:
        #     # [Default] In this case the centroids of the calibraiton board are used to obtain initial estimate of T
        #     p0 = get_detection_centroid(p)
        #     q0 = get_detection_centroid(q)
        #     # Compute T1 using centroids:
        #     T1 = get_transformation_matrix_kabsch(p0, q0)
        #     # Compute final T using all points:
        #     T = get_transformation_matrix_ICP(p, q, T1)
        # elif assignment_mode == 1:
        #     # Use Kabsch - efficient for radar mode because correspondence are known since there is only one detection for every calibration board location
        #     T = get_transformation_matrix_kabsch(p, q)
        # elif assignment_mode == 2:
        #     # Use ICP and inital estimate of T. Note that ICP needs a good initial estimate!
        #     T = get_transformation_matrix_ICP(p, q, T0)
        # else:
        #     raise Exception('Unknown mode in compute_transformation_matrix')
    else:
        # For every calibration board locations, the corresponces between for instance lidar to stereo detections is
        # known.
        T = get_transformation_matrix_kabsch(p, q)

    return T

def rotm2vector(R):
    # Generic function that converts rotation matrix to a vector
    # This fucntion is meant as a wrapper for 2 options: euler angles or rodrigues matrix formula
    if method_angles == 'rodrigues':
        return rotm2rodrigues(R)
    elif method_angles == 'euler':
        return rotm2eul(R)
    else:
        print('Error unknown method for rotm2vector conversion')

def rotm2rodrigues(R):
    # https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation
    theta = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))  # arcos argument should be between -1 and 1

    if theta == 0:
        return np.zeros(3)
    else:
        temp = np.zeros(3)
        temp[0] = R[2, 1] - R[1, 2]
        temp[1] = R[0, 2] - R[2, 0]
        temp[2] = R[1, 0] - R[0, 1]
        uv = 1 / (2 * np.sin(theta)) * temp

        return theta * uv

def rotm2eul(R):
    # Calculates rotation matrix (rotm) to euler angles (eul)
    # The results is the same as MATLAB function rotm2eul
    assert(isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([z, y, x])


def get_transformation_matrix_kabsch(q, p):
    q = q.T
    p = p.T
    # compute centroids
    Pc = rmsd.centroid(p)
    Qc = rmsd.centroid(q)
    # Kabsch algorithm for estimating R and t
    T = np.identity(4)
    T[:3, :3] = rmsd.kabsch(p - Pc, q - Qc)
    T[:3, 3] = Pc - np.dot(T[:3, :3], Qc)

    return T
