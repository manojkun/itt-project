#!/usr/bin/python
#print("Content-type: text/html\n\n")
import cgi,cgitb,sqlite3,os,string


form = cgi.FieldStorage()
sname = form.getvalue('quote')
qty = int(form.getvalue('qty'))
conn = sqlite3.connect('holdings.db')

if 'HTTP_COOKIE' in os.environ:
   for cookie in map(str.strip, os.environ['HTTP_COOKIE'].split(";")):
      (key, value ) = cookie.split('=');
      if key == "UserID":
         uid = value

count=0
cursor = conn.execute("select qty from holdings where UID='"+uid+"' and sname='"+sname+"' ")
for row in cursor:
    count += 1
    qty_old = int(row[0])
if count==0:
    #stock is not in user's Holdings (Error)
    print("Location:../sell.html?err=1\r\n\r\n")
else:
    #stock in holdings
    qty = qty_old - qty
    if qty<0:
        #selling more than owned
        print("Location:../sell.html?err=2\r\n\r\n")
    elif qty==0:
        #selling everything owned by user
        conn.execute("delete from holdings where UID='"+uid+"' and sname='"+sname+"' ")
    else:
        #update quantity
        conn.execute("update holdings set qty="+str(qty)+" where UID='"+uid+"' and sname='"+sname+"' ")

conn.commit()
conn.close()
print("Location:../sell.html?err=0\r\n\r\n")
