import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harshey@@256"
)

cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")

cursor.execute("USE college_db")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    course VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    dept_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
)
""")

conn.commit()

print("Database and tables created successfully!")

cursor.close()
conn.close()