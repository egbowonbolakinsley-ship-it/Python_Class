# DBMS - Database management system is a system that help manage a digital database ( a place where data are stored, retrieve or managed. )

# Types of DBMS
# 1. RDBMS - (Relational DBMS) / SQL - Structured Query Language
# i. data are in tabular form 
# ii. the tables are relatable using key
# e.g MySQL, PostgreSQL, Oracle, SQLLITE, MSSQL, MariaDB

# 1. create a database
# 2. create a table (rows and column)

# relationships between tables in SQL


# 2. NON-RDBMS / NoSQL
# 1. data are in key-value pair, documents or tree like structure
# e.g MongoDB, redis, firebase




# scripts -  is a file with executable code
# module - is a scripts that contains variables, or functions or classes
# library - is a collection of two or more modules
# framework - use to streamline workflow in a domain e.g django, keras, scikit , bootstrap, laravel, angular



import time, random, pyttsx3

# print("loading....")
# time.sleep(3)
# print("done")

# print(random.choice([1, 2, 4, 5]))
# print(random.randint(1000000000, 1099999999))

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()


import mysql.connector as sql

conn = sql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "password",
    port = "3306",
    database = "aug26_db"
)

cursor = conn.cursor()
conn.autocommit = True


# DDL - Data Definition Language e.g CREATE, DROP, ALTER, TRUNCATE 
# query = "DROP DATABASE aug26_db"
# query = "CREATE DATABASE IF NOT EXISTS aug26_db"
query = """
    CREATE TABLE customer(
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(50),
        email VARCHAR(50) UNIQUE,
        password VARCHAR(100),
        account_no VARCHAR(10) UNIQUE,
        balance DECIMAL(10, 2),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""

# query = "ALTER TABLE customer ADD COLUMN address TEXT AFTER password"
# query = "ALTER TABLE customer CHANGE address location TEXT"
# query = "ALTER TABLE customer DROP COLUMN location"
# query = "ALTER TABLE customer CHANGE balance balance DECIMAL(10, 2) DEFAULT 0.0"


query = "SHOW DATABASES"
# cursor.execute(query)
# print(cursor.fetchall())


# DML - Data Manipulation Language e.g INSERT, DELETE, UPDATE

def validate_email():
    email = input("Email: ").strip().lower()
    if "@" in email and "." in email:
        return email
    
    print("Invalid Email.")
    return validate_email()


def check_password():
    pass1 = input("Password: ")
    pass2 = input("Confirm Password: ")
    if pass1 == pass2:
        return pass1
    
    print("Password doesn't match")
    return check_password()


def register():
    fullname = input("Fullname: ")
    email = validate_email()
    password = check_password()
    account_no = random.randint(1000000000, 1099999999)
    address = input("Address: ")
    
    # print(fullname, email, password, account_no, address)
    query = "INSERT INTO customer(fullname, email, password, account_no, address) VALUES(%s, %s, %s, %s, %s)"
    values = (fullname, email, password, account_no, address)
    cursor.execute(query, values)
    
    print("Registration successfull")
    
# register()

def change_password():
    email = validate_email()
    old_password = input("Old Password: ")
    new_password = check_password()
    
    query = "UPDATE customer SET password=%s WHERE email=%s AND password=%s"
    values = (new_password, email, old_password)
    cursor.execute(query, values)
    print("Password changed if user is found")

# change_password()


def delete_account():
    email = validate_email()
    password = input("Password: ")
    query = "DELETE FROM customer WHERE email=%s AND password=%s"
    values = (email, password)
    cursor.execute(query, values)
    print("Account deleted if credentials are correct")
    
# delete_account()

# cursor.execute(query)


# DQL - Data Query Language e.g SELECT

# query = "SELECT * FROM customer"
# query = "SELECT fullname, email, account_no FROM customer"
# query = "SELECT fullname, email, account_no FROM customer WHERE balance > 0"
# query = "SELECT fullname, email, account_no FROM customer WHERE balance >= 0"
# query = "SELECT fullname, email, account_no FROM customer WHERE address LIKE 'OYO%'" # startwith
# query = "SELECT fullname, email, account_no FROM customer WHERE address LIKE '%Abuja%'" # endswith
# query = "SELECT fullname, email, account_no FROM customer WHERE address LIKE '%Abuja%'" # startwith or endswith
cursor.execute(query)
users = cursor.fetchall()
print(users)
# for user in users:
    # print(user[1], user[2])

# query = "SELECT fullname, email, account_no FROM customer WHERE id = 3"
# cursor.execute(query)
# user = cursor.fetchone()
# print(user)


from pwinput import pwinput

def login():
    email = validate_email()
    password = pwinput()
    
    query = "SELECT * FROM customer WHERE email=%s AND password=%s"
    values = (email, password)
    cursor.execute(query, values)
    user = cursor.fetchone()
    
    if user:
        print("Login Successfull")
    else:
        print("Invalid Email or Password")
    
# login()


def deposit():
    pass