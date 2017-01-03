@echo off
set /p dir="Enter directory name: "
mongoimport -d myo -c accel --type csv --file %dir%\accelerometer.csv --headerline
mongoimport -d myo -c gyro --type csv --file %dir%\gyro.csv --headerline
mongoimport -d myo -c emg --type csv --file %dir%\emg.csv --headerline
mongoimport -d myo -c orientation --type csv --file %dir%\orientationEuler.csv --headerline

pause