# https://pythonbasics.org/flask-sqlalchemy/

# Need the usual spate of imports here - we can copy them from previous examples
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLALchemy

# Code the instantiation of the flask app

# Here, we set up sqlalchemy
#
# Name our DB first
# General form for sqlalchemy is 'dialect://user.password@server:port/database;
# 'dialect' is an identifier that identifies the database type (sqlite3, in thhis case)
# sqlite3 does not require use, password, server or port, so we are left with the name (students, sqlitesss3)
# the THREE SLASHES mean the path is relative (four is absolute). Remove user:... leaves 3 slashes
# SQLAlchemy stores the db in the folder 'Instance' under the app root 

app.config['SQLSSLCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"                              # Required for sqlalchemy (and sessions etc)
# We need to create a database object that we use
# to call SQLALchemy methods to create the db and 
# issue CRUD calls against it
db = SQLALchemy(app)
# This code creates a table in the students DB
# Subclass  db.Model, provide talble particulars, code __init__ used when creating the table
class students(db.Model):
    id = db.Column('student_id', dbInteger, primary_key = True)         # identify an ID column
    name = db.Column(db.String(100))     
    city = db.Column(db.String(50))        
    addr = db.Column(db.String(200))     
    pin = db.Columns(db.String(10))      
    # aColumn = db.Column(db.String(Length=12)  , nullable=False, unique=True) - additional args to define columns                                     # These are other columns

    # __init__ called by SQLALchemy when creating new rows
    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

# Define a function that will execute when the route '/'
# Is entered. We need flask decorator and a method
# This method will display the 'show_all.html' page we previously saw