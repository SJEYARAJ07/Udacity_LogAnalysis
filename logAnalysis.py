#!/usr/bin/env python
# Project: Log Analysis (Udacity - Full Stack Nanodegree)

import psycopg2
import sys
from datetime import date

# Database name
DATABASENAME = 'news'

def connectDbAndReturnCursor():
    try:
        dbConnection = psycopg2.connect(dbname=DATABASENAME)
        #create DB cursor
        cursorDB = dbConnection.cursor()
        #return DB connection and curosor
        return dbConnection, cursorDB
    except psycopg2.OperationalError as e:
        print('Unable to connect to the database\n{0}').format(e)
        sys.exit(1)
    else:
        print('Connected to the database!')

def favorite_top_three_articles():
    query = """SELECT articles.title, COUNT(log.id) AS page_views FROM articles, log
                WHERE log.path = CONCAT('/article/', articles.slug)
                GROUP BY articles.title
                ORDER BY page_views desc
                LIMIT 3;"""
    dbConnection, cursorDB = connectDbAndReturnCursor()
    cursorDB.execute(query)
    favorite_top_three = cursorDB.fetchall()
    dbConnection.close()

    # Results
    print "\nMost popular three articles of all time"
    print "__________________________________________\n"
    for article, no_views in favorite_top_three:
        print '"{}" ---> {} views'.format(article,no_views)

def most_popular_authors():
    query = """SELECT name, sum(map_articlesview.views) AS views
            FROM map_articlesauthor, map_articlesview
            WHERE map_articlesauthor.title = map_articlesview.title
            GROUP BY name ORDER BY views desc;"""
    dbConnection, cursorDB = connectDbAndReturnCursor()
    cursorDB.execute(query)
    most_popular_authors = cursorDB.fetchall()
    dbConnection.close()

    # Results
    print "\nMost popular article authors of all time"
    print "__________________________________________\n"
    for name_of_author, no_views in most_popular_authors:
        print '"{}" ---> {} views'.format(name_of_author,no_views)

def elevated_error_days():
    query = """SELECT day, error_rate FROM elevated_error where error_rate > 1.0;"""
    dbConnection, cursorDB = connectDbAndReturnCursor()
    cursorDB.execute(query)
    elevated_error_days = cursorDB.fetchall()
    dbConnection.close()

    # Results
    print "\nDays where more than 1% of requests lead to errors"
    print "_____________________________________________________\n"
    for date, error_percent in elevated_error_days:
        print '"{}" ---> {} views'.format(date,error_percent)

if __name__ == '__main__':
    favorite_top_three_articles()
    most_popular_authors()
    elevated_error_days()
