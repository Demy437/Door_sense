#eerst moet je de database in mysql maken in de command line

# CREATE DATABASE DoorSense;

# een gebruiker aanmaken

# CREATE USER ‘local_user’@’localhost’ IDENTIFIED BY ‘password’;

# nog die gebruiker even permissions geven

# GRANT ALL PRIVILEGES ON *.* TO 'local_user'@'localhost' IDENTIFIED BY "password";

# daarna in de database gaan

# USE DoorSense;

# daarna de table maken

# CREATE TABLE sessions (
# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# data VARCHAR(100),
# cur_timestamp TIMESTAMP(6)
# );

# om de database te zien

# SELECT * FROM sessions;

import MySQLdb as mariadb
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# connect to the database
mariadb_connection = mariadb.connect(
    user='local_user',
    password='password',
    host='localhost',
    database="DoorSense")

# create a cursor object for executing queries
cursor = mariadb_connection.cursor()
green = (0, 255, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

