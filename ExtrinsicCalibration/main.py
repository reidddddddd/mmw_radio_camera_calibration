import argparse
from ExtrinsicCalibration.config import *
from ExtrinsicCalibration.optimize import joint_optimization
if __name__ == '__main__':

    parser = argparse.ArgumentParser("Experiments for extrinsic calibration")
    parser.add_argument('--camera', type=str, action='append', default="./data/camera.csv")
    parser.add_argument('--radar', type=str, action='append', default="./data/radar.csv")

    args = parser.parse_args()

    (camera_sensor, radar_sensor) = get_sensor_setup(args.camera, args.radar)

    Tms = joint_optimization(camera_sensor, radar_sensor)

    print(Tms)

