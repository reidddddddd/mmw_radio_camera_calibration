import numpy as np
import cv2
from calibration import util
# aa = np.array([[1,2,3],[2,2,3]])
#
# gg = aa[:,1].reshape(2,1)
# a = np.divide(aa, gg)
#
# var = a[:, [0,1]]
#
# for ele in var:
#     print(ele[0])
#     print(ele[1])





# extr_answer = np.dot(util.to_homogeneous_3d_multiple_points(obj_points[0]), extrinsics_opt[0].T)
# inter_answer = np.dot(extr_answer, intrinsic_matrix.T)
#
#
# inter_answer = np.divide(inter_answer, inter_answer[:, 2].reshape(inter_answer.shape[0], 1))
#
#
# point_size = 1
# point_color = (0, 0, 255)  # BGR
# thickness = 4  # 0 、4、8
# image = cv2.imread("./images/IMG_001.jpg")
#
#
# for coor in inter_answer:
#     cv2.circle(image, (int(coor[0]), int(coor[1])), point_size, point_color, thickness)

width = 0.3875
height = 0.28
x = -(width/2)
y = -0.13
z = 0.4

a = util.create_sample_plane(width,height,x,y,z)

