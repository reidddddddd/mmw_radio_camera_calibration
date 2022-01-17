from Calibration import calibration
from Visualization import clean_radar_data
from Visualization import util
import numpy as np

picture_dir = "./outData/3/IMG_001.jpg"
csv_dir = "./outData/3/pcl/pcl.csv"
out_dir = "./outData/3/pcl/1.jpg"
intrinsic_matrix, wwm_extrinsics_matrix = calibration.calibration_mmw_radar_camera(model=1)


model = clean_radar_data.common_read(csv_dir, picture_dir)

calibration_points = clean_radar_data.get_calibration_result(intrinsic_matrix, wwm_extrinsics_matrix, model)

util.draw_points_on_picture(picture_dir, calibration_points, out_dir)








