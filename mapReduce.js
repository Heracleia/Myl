var mapAccel, mapGyro, reduce;

imu_reduced.remove({});

mapAccel = function() {
    var values = {
        accel_x: this.x,
        accel_y: this.y,
        accel_z: this.z
    };
    emit(this.timestamp, values);
};

mapGyro = function() {
    var values = {
        gyro_x: this.x,
        gyro_y: this.y,
        gyro_z: this.z
    };
    emit(this.timestamp, values);
};

mapEmg = function() {
    var values = {
        emg1: this.emg1,
        emg2: this.emg2,
        emg3: this.emg3,
        emg4: this.emg4,
        emg5: this.emg5,
        emg6: this.emg6,
        emg7: this.emg7,
        emg8: this.emg8
    };
    emit(this.timestamp, values);
}

mapOrientation = function() {
	var values = {
		roll: this.roll,
		pitch: this.pitch,
		yaw: this.yaw
	};
	emit(this.timestamp, values);
}

reduce = function(k, values) {
    var out = {};
    values.forEach(function(value) {        
        var field;
        for(field in value) {
            if(field != 'timestamp')
                out[field] = value[field];
        }
    });
    return out;
}

db.accel.mapReduce(mapAccel, reduce, {out: {reduce: "imu_reduced"}});
db.gyro.mapReduce(mapGyro, reduce, {out: {reduce: "imu_reduced"}});
db.orientation.mapReduce(mapOrientation, reduce, {out: {reduce: "imu_reduced"}});