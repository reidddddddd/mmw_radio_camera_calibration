import os
import numpy as np
from os import path
from os import listdir
from os.path import isfile, join


class Sensor:
    def __init__(self, name, type, sensor_data):
        self.name = name
        self.type = type
        self.sensor_data = sensor_data
        self.W = np.identity(3)


def get_sensor_setup(camera_path, radar_path):
    camera_sensors = get_camera(load_data(camera_path), sensor_name="camera")

    radar_sensors = get_radar(load_data(radar_path), sensor_name="radar")

    return camera_sensors, radar_sensors


def get_camera(Xc, sensor_name='camera'):
    camera_sensor = Sensor(name=sensor_name,
                           type='camera',
                           sensor_data=Xc)
    return camera_sensor


def get_radar(Xc, sensor_name='radar'):
    radar_sensor = Sensor(name=sensor_name,
                          type='radar',
                          sensor_data=Xc)
    return radar_sensor

def load_data(path):
    if os.path.isdir(path):
        data = read_from_folder(path)
    elif os.path.isfile(path):
        data = read_file(path)
    else:
        raise Exception('Cannot load data because is neither a valid folder or a valid file (YAML/CSV): %s' % path)
    return data


def read_from_folder(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # Read first file to determine the number of detections per board
    nr_cols, nr_rows = read_file(mypath + onlyfiles[0]).shape
    # Initalise output array
    detector_data = np.zeros((nr_cols, nr_rows * len(onlyfiles)))
    # Loop over all files
    for i, file in enumerate(sorted(onlyfiles)):
        detector_data[:, i * nr_rows:i * nr_rows + nr_rows] = read_file(mypath + file)

    return detector_data


def read_file(name):
    base, extension = path.splitext(name)
    if extension == '.csv':
        return read_csv_file(name)
    raise Exception('Cannot load file ', name, ' extension should be yaml, yml or csv.')


def read_csv_file(name):
    with open(name, 'rb') as f:
        data = np.loadtxt(f, delimiter=",")
    return data
