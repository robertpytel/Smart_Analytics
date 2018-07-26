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
import matplotlib.pyplot as plot
import math

"""use pandas for data"""
data = pan.read_csv("Sensor_mini.csv")
#print(data.dtypes)

#array = data[field]
linearAccelX = data['LINEAR ACCELERATION X (m/s^2)']
linearAccelY = data['LINEAR ACCELERATION Y (m/s^2)']
linearAccelZ = data['LINEAR ACCELERATION Z (m/s^2)']
gyroX = data['GYROSCOPE X (rad/s)']
gyroY = data['GYROSCOPE Y (rad/s)']
gyroZ = data['GYROSCOPE Z (rad/s)']
TIME = data['Time since start in ms']

#plot three graphs in one plot
plot.plot(TIME, gyroX,'r')
plot.plot(TIME, gyroY,'b')
plot.plot(TIME, gyroZ,'g')
# Put a nicer background color on the legend.
legend = plot.legend(loc='best', shadow=True, fontsize='larger')
legend.get_frame().set_facecolor('#99ff99')
plot.show()

"""FIGURE 2"""
plot.figure(2)
fig, axes = plot.subplots(nrows=3, ncols=1)
# -- subplot 1 --
data['GYROSCOPE X (rad/s)'].plot(ax=axes[0], figsize=(15,15))
axes[0].set_title("GYRO X vs TIME")
axes[0].set_xlabel("TIME")
axes[0].set_ylabel("GYRO X")
axes[0].legend(loc='best', shadow=True, fontsize='xx-large')\
.get_frame().set_facecolor('#ff99ff')
axes[0].plot(TIME, gyroX, 'r')

# -- subplot 2 --
data['GYROSCOPE Y (rad/s)'].plot(ax=axes[1], figsize=(15,15))
axes[1].set_title("GYRO Y vs TIME")
axes[1].set_xlabel("TIME")
axes[1].set_ylabel("GYRO Y")
axes[1].legend(loc='best', shadow=True, fontsize='xx-large')\
.get_frame().set_facecolor('#ffffb3')
axes[1].plot(TIME, gyroY, 'b')

# -- suplot 3 --
data['GYROSCOPE Z (rad/s)'].plot(ax=axes[2], figsize=(15,15))
axes[2].set_title("GYRO Z vs TIME")
axes[2].set_xlabel("TIME")
axes[2].set_ylabel("GYRO Z")
axes[2].legend(loc='best', shadow=True, fontsize='xx-large')\
.get_frame().set_facecolor('#ccffdd')
axes[2].plot(TIME, gyroZ, 'g')
"""END FIGURE 2"""

#linear acceleration in meters per second squared in x, y, z directions
#https://stackoverflow.com/questions/15490990/
#obtaining-orientation-using-gyroscope-and-accelerometer
#Why Use Kalman filters?https://www.youtube.com/watch?v=mwn8xhgNpFY
