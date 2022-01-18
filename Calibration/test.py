import numpy as np
from Calibration import calibration
from Calibration import corner_detection as cd
from Calibration import util
from Visualization import util as v_util


def main():
    intrinsic_matrix, extrinsics_opt = calibration.calibration__camera(model=1)
    obj_points, img_points, img_shapes, img_names = cd.find_corners(model=1)
    aa = np.dot(util.to_homogeneous_3d_multiple_points(obj_points[1])
                          , extrinsics_opt[8].T)
    test1 = np.dot(np.dot(util.to_homogeneous_3d_multiple_points(obj_points[8])
                          , extrinsics_opt[8].T), intrinsic_matrix.T)
    test = np.divide(test1, test1[:, 2].reshape(test1.shape[0], 1))
    test = test[0:8, :]
    v_util.draw_points_on_picture("./images/1080/IMG_radar.jpg", test, "./images/3.jpg")


if __name__ == "__main__":
   inv, outv =  calibration.calibration_mmw_radar_camera(model=1)
   intrinsic_matrix, extrinsics_opt = calibration.calibration__camera(model=1)
   obj_points, img_points, img_shapes, img_names = cd.find_corners(model=1)
   camera_points = np.dot(util.to_homogeneous_3d_multiple_points(obj_points[8])
                          , extrinsics_opt[8].T)
   radar_points = util.create_sample_plane(camera_points)

   tmp = np.dot(radar_points
                         , outv.T)

   test1 = np.dot(np.dot(radar_points
                         , outv.T), inv.T)

   test = np.divide(test1, test1[:, 2].reshape(test1.shape[0], 1))
   test = test[0:8]
   v_util.draw_points_on_picture("./images/1080/IMG_radar.jpg", test, "./images/2.jpg")
   main()
