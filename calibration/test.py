import numpy as np
from Calibration import calibration
from Calibration import corner_detection as cd
from Calibration import util
from Visualization import util as v_util


def main():
    intrinsic_matrix, extrinsics_opt = calibration.calibration__camera(model=1)
    obj_points, img_points, img_shapes, img_names = cd.find_corners(model=1)

    test1 = np.dot(np.dot(util.to_homogeneous_3d_multiple_points(obj_points[0])
                          , extrinsics_opt[0].T), intrinsic_matrix.T)
    test = np.divide(test1, test1[:, 2].reshape(test1.shape[0], 1))
    v_util.draw_points_on_picture("./images/1080/IMG_001.jpg", test, "./images/1.jpg")


if __name__ == "__main__":
    main()
