# LogAnalysis
Log Analysis Project - Udacity Full Stack Nanodegree

# Project Overview:
Create a reporting tool that prints out reports (in plain text) based on the data in a database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

# Assignment
The reporting tool needed to answer the following questions:

Q> What are the most popular three articles of all time?
Q> Who are the most popular article authors of all time?
Q> On which days did more than 1% of requests lead to errors?

# Steps to Run the Code
This section will describe the SQL views I created for the code to function properly and how to run the program.

# Instructions to run the Program

Place the below files within the same directory as the VM and SQL file provided by Udacity.
logAnalysis.py
createViews.py

Start the Virtual Machine(VM)
=> vagrant up

SSH into the VM
=> vagrant ssh

Navigate to /vagrant
=> cd /vagrant

Create the database schema and load the data by running
=> psql -d news -f newsdata.sql 

Create views listed above by running the command
=> psql -d news -f createViews.sql

Execute the python file:
=> python logAnalysis.py

# Below is the output I received:

Most popular three articles of all time
__________________________________________

"Candidate is jerk, alleges rival" ---> 338647 views
"Bears love berries, alleges bear" ---> 253801 views
"Bad things gone, say good people" ---> 170098 views

Most popular article authors of all time
__________________________________________

"Ursula La Multa" ---> 507594 views
"Rudolf von Treppenwitz" ---> 423457 views
"Anonymous Contributor" ---> 170098 views
"Markoff Chaney" ---> 84557 views

Days where more than 1% of requests lead to errors
_____________________________________________________

"2016-07-17" ---> 2.26 views
