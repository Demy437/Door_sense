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

rsor = mariadb_connection.cursor()
green = (0, 255, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 0.9:
        sense.clear()
    else:
        #voegt een timestamp toe aan de database
        insert = "INSERT INTO sessions (data) VALUES ('OPEN');"
        cursor.execute(insert)
        sense.show_letter("✅", green)
        push.send_message("‎", title="Deur is open!")
        mariadb_connection.commit()
        sleep(10)
