CREATE DATABASE SensorDB;
USE SensorDB;

-- Table 1: SensorData (Stores sensor values over time)
CREATE TABLE SensorData (
    time_stamp DATETIME NOT NULL,
    `Sensor 1` FLOAT,
    `Sensor 2` FLOAT,
    `Sensor 3` FLOAT,
    `Sensor 4` FLOAT,
    `Sensor 5` FLOAT,
    `Sensor 6` FLOAT,
    `Sensor 7` FLOAT,
    `Sensor 8` FLOAT,
    `Sensor 9` FLOAT,
    `Sensor 10` FLOAT,
    `Sensor 11` FLOAT,
    `Sensor 12` FLOAT,
    `Sensor 13` FLOAT,
    `Sensor 14` FLOAT,
    `Sensor 15` FLOAT,
    `Sensor 16` FLOAT,
    `Sensor 17` FLOAT,
    `Sensor 18` FLOAT,
    `Sensor 19` FLOAT,
    `Sensor 20` FLOAT
);

-- Table 2: SensorStatus (Stores status of each sensor)
CREATE TABLE SensorStatus (
    sensor_name VARCHAR(20) PRIMARY KEY,
    status ENUM('Active', 'Inactive') NOT NULL
);

-- Insert initial sensor statuses (all active by default)
INSERT INTO SensorStatus (sensor_name, status)
VALUES 
    ('Sensor 1', 'Active'), ('Sensor 2', 'Active'), ('Sensor 3', 'Active'),
    ('Sensor 4', 'Active'), ('Sensor 5', 'Active'), ('Sensor 6', 'Active'),
    ('Sensor 7', 'Active'), ('Sensor 8', 'Active'), ('Sensor 9', 'Active'),
    ('Sensor 10', 'Active'), ('Sensor 11', 'Active'), ('Sensor 12', 'Active'),
    ('Sensor 13', 'Active'), ('Sensor 14', 'Active'), ('Sensor 15', 'Active'),
    ('Sensor 16', 'Active'), ('Sensor 17', 'Active'), ('Sensor 18', 'Active'),
    ('Sensor 19', 'Active'), ('Sensor 20', 'Active');
