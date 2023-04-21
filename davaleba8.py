import sqlite3
conn = sqlite3.connect("books_db.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE books,
( id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR (50),
author VARCHAR (60),
release_year INT;
""")
cursor.execute(""" INSERT INTO books(title,author,relace_year)VALUES("ნუ მოკლავ ჯაფარას", "ჰარპერ ლი",1960)""")
conn.commit()
books_list = [
    ("ალქიმიკოსი", "პაულო კოელიო", 1988)
    ("დანაშაულის თანამონაწილენი","აგათა კრისტი", 1890)
    ("ჯეინ ეარი", "შარლოტ ბრონტე", 1847)
    ("მე,ბებია,ილიკო და ილარიონი", "ნოდარ დუმბაძე", 1960)
]
cursor.executemanty("""INSERT INTO books(title,uathor,relace_year)VALUE(*,*,*)""",books_list)
conn.commit()
#2davaleba
import sqlite3
conn = sqlite3.connect("titanic.sqlite3")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE titanic 
( id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR (40),
age INT,
sex VARCHAR (50),
ticket INT,
cabin INT;
""")
name = input("passengers name")
age = input("passenger age")
sex = input("passengers gender")
ticket = input("ticket price")
cabin = input("passengers cabin")
cursor.execute("INSERT INTO titanic (passenger_name,age,sex, ticket,cabin)VALUES(name,age,sex,ticket,cabin)")
conn.commit()
n,a,s,t,c = input("enter passengers name:"), input("enter passengers age:"), input("enter gender:"),input("ticket price:"),input("cabin:")
N,A,S,T,C = input("enter passengers name:"), input("enter passengers age:"), input("enter gender:"),input("ticket price:"),input("cabin:")
Nn,Aa,Ss,Tt,Cc = input("enter passengers name:"), input("enter passengers age:"), input("enter gender:"),input("ticket price:"),input("cabin:")
print(n,a,s,t,c)
print(N,A,S,T,C)
print(Nn,Aa,Ss,Tt,Cc)
print(" entered succesfully ")
conn.close()
if (conn):
    conn.close()
print("sqlite connection is closed")
conn.commit()
#davaleba3

class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"title: {self.title}, genre: {self.genre}, year: {self.year}, imdb: {self.imdb}"

    import sqlite3
    conn = sqlite3.connect("movies.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE movies,
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    genre VARCHAR(50),
    year INT,
    imdb INT;

    """)
    cursor.execute("""INSERT INTO movies(title,genre,year,imdb)VALUES("escape","mystery",1999,10) """)
    conn.commit()
    


     

