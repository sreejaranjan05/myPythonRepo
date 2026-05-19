import mysql.connector as sql

con = sql.connect(host="localhost", user="root", password="Patna@123", database="SchoolDB")
cur = con.cursor()

cur.execute("SELECT * FROM Students")
data = cur.fetchall()

for row in data:
    print(row)

con.close()
