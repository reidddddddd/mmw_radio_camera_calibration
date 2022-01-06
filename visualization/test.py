import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

frame = pd.read_csv("./data/pcl2.csv")
frame['orginTimestamp'] = frame[' Timestamp']
tmp = frame['orginTimestamp'].unique()
frame[' Timestamp'] = pd.to_datetime(frame[' Timestamp'] / 1000, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
aa = tmp[2]-tmp[1]
# frame = frame[frame[' ZPos'] >= 0.3]
# frame = frame[frame[' ZPos'] <= 1.0]
# frame = frame[frame[' Xpos'] <= 0.5]
# frame = frame[frame[' Xpos'] >= -0.5]
# frame = frame[frame[' YPos'] <= 0.3]
# frame = frame[frame[' YPos'] >= -0.3]

print(frame.count())

frame = frame[frame[' Timestamp'] <= '2022-01-06 09:48:02']
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(frame[' Xpos'], frame[' YPos'], frame[' ZPos'])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
