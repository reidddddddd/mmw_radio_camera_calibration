import numpy as np

# height = 8
# width = 5
# square_size = 0.0275
# objp = np.zeros((height * width, 2), np.float32)
# objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)
# objp = objp * square_size
#
# objp[:, 0] = objp[:, 0] - 0.102
# objp[:, 1] = objp[:, 1] + 0.064
# objp = np.concatenate((objp,np.ones((objp.shape[0], 1), np.float32)*0.2318),axis=1)