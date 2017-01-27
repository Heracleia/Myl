mongoexport --db myo --collection imu_reduced --type=csv --fields "_id,value.roll,value.pitch,value.yaw,value.gyro_x,value.gyro_y,value.gyro_z,value.accel_x,value.accel_y,value.accel_z" --out imu.csv

pause