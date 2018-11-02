#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
email = form.getvalue('email')
msg = form.getvalue('msg')

#now we shall store them in a file
with open("feedback.txt",'a') as feed_file:
    feed_file.write(email+"\n")
    feed_file.write(msg+"\n\n")
print("Location:../contact.html?send=yes\r\n\r\n")
