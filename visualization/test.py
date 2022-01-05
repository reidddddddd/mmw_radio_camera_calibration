import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

frame = pd.read_csv("./data/pcl.csv")
frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'] / 1000, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
# frame[' ZPos'] = 0.4
frame = frame[frame[' ZPos'] >= 0.3]
frame = frame[frame[' ZPos'] <= 1.0]
frame = frame[frame[' Xpos'] <= 0.5]
frame = frame[frame[' Xpos'] >= -0.5]
frame = frame[frame[' YPos'] <= 0.3]
frame = frame[frame[' YPos'] >= -0.3]
frame[' ZPos'] = 0.4
print(frame.count())

frame = frame[frame[' Timestamp'] <= '2022-01-05 07:26:36']
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(frame[' Xpos'], frame[' YPos'], frame[' ZPos'])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
