import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="webgui"
)

cursor = con.cursor()

cursor.execute("""
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id VARCHAR(20),
    name VARCHAR(100),
    mobile VARCHAR(15),
    salary FLOAT
)
""")

print("Table created successfully.")
con.close()
