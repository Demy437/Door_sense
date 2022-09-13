import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='local_user', password='password',
                              host='localhost',database='DoorSense')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_employee = """SELECT * FROM sessions"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()

p = []

tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)



contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

filename = 'webbrowser.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")    
