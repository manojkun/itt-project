#!/usr/bin/python
#print("Content-type: text/html\n\n")
import cgi,cgitb,sqlite3


form = cgi.FieldStorage()
uid = form.getvalue('uid')
pss = form.getvalue('pass')
accno = form.getvalue('bno')
fname = form.getvalue('fname')
lname = form.getvalue('lname')

conn = sqlite3.connect('users.db')
cursor = conn.execute("insert into users values('"+uid+"','"+pss+"','"+fname+"','"+lname+"',"+accno+")")
conn.commit()
conn.close()
print("Location:../login.html\r\n\r\n")
