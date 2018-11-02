#!/usr/bin/python
#print("Content-type: text/html\n\n")
import cgi,cgitb,sqlite3


form = cgi.FieldStorage()
sname = form.getvalue('Quote')
qty = form.getvalue('qty')
conn = sqlite3.connect('users.db')


cursor = conn.execute("SELECT COUNT(*) FROM USERS WHERE UID='"+uid+"' and PSS='"+pss+"';")


cursor = conn.execute("insert into users values('"+uid+"','"+pss+"','"+fname+"','"+lname+"',"+accno+")")
conn.commit()
conn.close()
print("Location:../login.html\r\n\r\n")
