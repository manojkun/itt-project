#!/usr/bin/python
import sqlite3,os
print("Content-type: text/html\r\n\r\n")
print('''<html>
<head>
  <link rel="stylesheet" type="text/css" href="../style.css">
<title>
Trade Online
</title>
</head>
<body>
<nav>
<a href="../profile.html">Home</a>
<a href="../buy.html">Buy</a>
<a href="../sell.html">Sell</a>
<a class="active" href="holdings.html">Holdings</a>
<a href="../funds.html">Add/Remove Funds</a>
</nav>
<div class="heading">Your Holdings</div></body></html>''')
conn = sqlite3.connect('holdings.db')
if 'HTTP_COOKIE' in os.environ:
   for cookie in map(str.strip, os.environ['HTTP_COOKIE'].split(";")):
      (key, value ) = cookie.split('=');
      if key == "UserID":
         uid = value
cursor = conn.execute("SELECT * FROM Holdings where uid='"+uid+"'")
print("<table><tr><th>Stock</th><th>Qty</th></tr>")
for row in cursor:
    print("<tr>")
    print("<td>"+row[0]+"</td>")
    print("<td>"+str(row[1])+"</td>")
    print("</tr>")
print("</table>")
