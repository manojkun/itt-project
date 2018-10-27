#!/usr/bin/python
#print("Content-type: text/html\n\n")
import cgi,cgitb,sqlite3


form = cgi.FieldStorage()
uid = form.getvalue('uid')
pss = form.getvalue('pass')

conn = sqlite3.connect('users.db')
cursor = conn.execute("SELECT COUNT(*) FROM USERS WHERE PASS='"+pss+"';")
for row in cursor:
    count = int(row[0])
if count==1:
    print ("Set-Cookie:UserID = XYZ;")
    print("Location:../profile.html\r\n\r\n")
    #print ("Set-Cookie:Password = XYZ123;\r\n")


else:
    print("Location:../login.html\r\n\r\n")
conn.close()
