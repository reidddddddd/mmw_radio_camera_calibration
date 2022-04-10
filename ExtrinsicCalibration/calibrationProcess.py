import copy
import numpy as np
from ExtrinsicCalibration.helper_function import *
from scipy import optimize


def extrinsic_mapping(T, xmap):
    return np.dot(T[:3, :], np.vstack([xmap, np.ones([1, xmap.shape[1]])]))  # xmap should contains ones


class CalibrationProcess:
    def __init__(self, camera_sensor, radar_sensor, correspondences='known'):
        self.camera_sensor = camera_sensor
        self.radar_sensor = radar_sensor
        self.nr_elements_pose = 6
        self.assignment = correspondences
        self.parameters_optimizer = optimizer_parameters
        # get initial X
        self.X = np.zeros(self.nr_elements_pose)
        self.X = self.compute_pairwise_poses(self.X)

    def getX(self):
        return self.X

    def compute_pairwise_poses(self, X):
        Tm = self.convertXtoTms(X)
        T = compute_transformation_matrix(self.camera_sensor.sensor_data,
                                          self.radar_sensor.sensor_data,
                                          Tm, self.assignment)
        angles = rotm2vector(T[:3, :3])
        translation = T[:3, 3]
        X = np.concatenate([angles, translation])
        return X

    def convertXtoTms(self, X):
        n = 0
        Tm = []
        Tm = np.identity(4)
        Tm[:3, :3] = vector2rotm(X[0:3:1])
        Tm[:3, 3] = X[3:6:1]
        return Tm

    def optimize(self):
        self.unconstrained_optimization()

    def unconstrained_optimization(self):
        # print('Run Unconstrained Optimization')
        self.X = optimize.fmin_slsqp(self.objective_function, self.X, iter=self.parameters_optimizer.maximum_iterations,
                                     acc=self.parameters_optimizer.stopping_tolerance,
                                     disp=self.parameters_optimizer.verbosity)

    def objective_function(self, X):
        # Get current estimate of transformation matrices
        Tms = self.convertXtoTms(X)
        # Compute individual errors
        sensor_error = self.compute_calibration_errors(Tms)
        # Return total error:
        return self.compute_total_error(sensor_error)

    def compute_calibration_errors(self, Tms):
        Y = self.project2camera(Tms, self.radar_sensor.sensor_data)
        return self.compute_sensor_errors(Y, self.camera_sensor.sensor_data, self.camera_sensor.W)

    def compute_sensor_errors(self, Y, data, W):
        if self.assignment == 'known':
            e = np.sum(np.dot(W, (Y - data) ** 2), axis=0)
        else:
            e = self.a2b_assignment(Y, data, W)

        return e

    def project2camera(self, T, xmap):
        return extrinsic_mapping(T, xmap)

    def extrinsic_mapping(self, T, xmap):
        return np.dot(T[:3, :], np.vstack([xmap, np.ones([1, xmap.shape[1]])]))  # xmap should contains ones

    def compute_total_error(self, errors):
        return np.sum(errors)