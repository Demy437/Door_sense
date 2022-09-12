#eerst moet je de database in mysql maken in de command line

# CREATE DATABASE DoorSense;

# daarna de table maken

# CREATE TABLE sessions (
# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# data VARCHAR(100),
# cur_timestamp TIMESTAMP(6)
# );



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
    sense.show_letter("!", green)

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 0.9:
        sense.clear()
    else:
        insert = "INSERT INTO sessions (data) VALUES ('OPEN');"
        cursor.execute(insert)
        sense.show_letter("✅", green)
        mariadb_connection.commit()
        mariadb_connection.close()
        sleep(10)
