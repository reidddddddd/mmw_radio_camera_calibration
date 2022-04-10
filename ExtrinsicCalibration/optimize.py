from ExtrinsicCalibration.calibrationProcess import CalibrationProcess


def joint_optimization(camera_sensor, radar_sensor):
    calibration = CalibrationProcess(camera_sensor, radar_sensor)
    calibration.optimize()
    Tms = calibration.convertXtoTms(calibration.getX())
    return Tms
