import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

frame = pd.read_csv("./data/pcl1.csv")
frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'] / 1000, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')


frame = frame[frame[' Timestamp'] <= '2022-01-05 06:50:38']


tmp = frame[[' Xpos', ' YPos', ' ZPos']].to_numpy(dtype=float)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(frame[' Xpos'], frame[' YPos'], frame[' ZPos'])
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
#
# plt.show()
