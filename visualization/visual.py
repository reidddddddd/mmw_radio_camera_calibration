import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


frame = pd.read_csv("./data/pcl.csv")

indexs = frame[' Timestamp'].unique()[1:10]

for ele in indexs:
    tmp = frame[frame[' Timestamp'] == ele]
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(tmp[' Xpos'], tmp[' YPos'], tmp[' ZPos'])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(ele)

    plt.show()


