# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:39:27 2018
@author: robertp
Sources:
https://stackoverflow.com/questions/37598991/how-
to-plot-two-specific-columns-from-a-csv-file-in-python
"""
import numpy as np
import pandas as pan
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
import math
"""
    Table of Contents
    1: DATA
    2: GYROSCOPES
    3: LINEAR ACCELERATION
"""

"""1: DATA"""
# This just in!
data = pan.read_csv("Sensor_mini.csv")

# We. have. Dataaaaa!
linearAccelX = data['LINEAR ACCELERATION X (m/s^2)']
linearAccelY = data['LINEAR ACCELERATION Y (m/s^2)']
linearAccelZ = data['LINEAR ACCELERATION Z (m/s^2)']
gyroX = data['GYROSCOPE X (rad/s)']
gyroY = data['GYROSCOPE Y (rad/s)']
gyroZ = data['GYROSCOPE Z (rad/s)']
TIME = np.array(data['Time since start in ms'])
# we us numpy so we can manipulate Time freely, eg. "TIME/1000"

"""*********************************************************"""
"""*********************************************************"""

"""2: GYROSCOPES"""
"""FIGURE 1: Separate Gyroscope Data"""
# -- subplot 1 --
plot.figure(1)
plot.subplot(111)
plot.plot(TIME/1000, gyroX, 'r')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
# Put a nicer background color on the legend.
plot.title("Delta Gyro X vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Gyro in radians/sec')
plot.show()

# -- subplot 2 --
plot.figure(2)
plot.subplot(111)
plot.plot(TIME/1000, gyroY, 'g')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
# Put a nicer background color on the legend.
plot.title("Delta Gyro Y vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Gyro in radians/sec')
plot.show()

# -- suplot 3 --
# data['GYROSCOPE Z (rad/s)'].plot(ax=axes[2], figsize=(15,15))
plot.figure(3)
plot.subplot(111)
plot.plot(TIME/1000, gyroZ, 'b')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
# Put a nicer background color on the legend.
plot.title("Delta Gyro Z vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Gyro in radians/sec')
plot.show()

"""FIGURE 2: Gyroscopes X, Y, Z"""
# Plot 3 gyroscopes, x, y, z, in one plot against seconds
plot.figure(4)
plot.plot(TIME/1000, gyroX, 'r')
plot.plot(TIME/1000, gyroY, 'b')
plot.plot(TIME/1000, gyroZ, 'g')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
# Put a nicer background color on the legend.
plot.title("Delta Gyro X,Y,Z vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Gyro in radians/sec')
plot.show()

"""FIGURE 3: Gyroscope Magnitude"""
# Get magnitude of gyro x, y, z together. (1/2)
# Got equation from Internet...
gyroMagnitude = []
# Use the shortest list as a limit!
MIN = min(len(gyroX), len(gyroY), len(gyroZ))
for xyz in range(0, MIN):
    gyroMagnitude.append(math.sqrt(
                 gyroX[xyz]**2 + gyroY[xyz]**2 + gyroZ[xyz]**2))
# Now convert it to a pandas array!
gyroMagnitude = pan.Series(gyroMagnitude)

# Plot the magnitude of the gyroscopes. (2/2)
plot.figure(5)
plot.plot(TIME/1000, gyroMagnitude, '#fdaa48')
plot.title("Magnitude of Gyro vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('||Gyro|| in radians/sec')
plot.show()

"""*********************************************************"""
"""*********************************************************"""

"""3: LINEAR ACCELERATION"""
"""FIGURE 1: Separate Linear Acceleration Data"""
plot.figure(6)
plot.subplot(111)
plot.plot(TIME/1000, linearAccelX, 'r')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
plot.title("Delta Linear Acceleration X vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Linear Acceleration in radians/sec')
plot.show()

# -- subplot 2 --
plot.figure(7)
plot.subplot(111)
plot.plot(TIME/1000, linearAccelY, 'g')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
plot.title("Delta Linear Acceleration Y vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Linear Acceleration in radians/sec')
plot.show()

# -- suplot 3 --
plot.figure(8)
plot.subplot(111)
plot.plot(TIME/1000, linearAccelZ, 'b')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
plot.title("Delta Linear Acceleration Z vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Linear Acceleration in radians/sec')
plot.show()

"""FIGURE 2: Linear Acceleration X, Y, Z"""
# Plot 3 linear accelerations, x, y, zed, in one plot against seconds"""
plot.figure(9)
plot.plot(TIME/1000, linearAccelX, 'r')
plot.plot(TIME/1000, linearAccelY, 'b')
plot.plot(TIME/1000, linearAccelZ, 'g')
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
plot.title("Delta Linear Acceleration X,Y,Z vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('Delta Linear Acceleration in m/s^2')
plot.show()

"""FIGURE 3: Linear Acceleration Magnitude"""
# Get magnitude of linear acceleration x, y, z together. (1/2)
# Got equation from Internet...
linearMagnitude = []
# Use the shortest list as a limit!
MIN = min(len(linearAccelX), len(linearAccelY), len(linearAccelZ))
for xyz in range(0, MIN):
    linearMagnitude.append(math.sqrt(
      linearAccelX[xyz]**2 + linearAccelY[xyz]**2 + linearAccelZ[xyz]**2))
# Now convert it to a pandas array!
linearMagnitude = pan.Series(linearMagnitude)

"""Plot the magnitude of the linear accelerations. (2/2)"""
plot.figure(10)
plot.plot(TIME/1000, linearMagnitude, '#fdaa48')
plot.title("Magnitude of Linear Acceleration vs. Time")
plot.xlabel('Time in Seconds')
plot.ylabel('||Linear Acceleration|| in m/s^2')
plot.show()
