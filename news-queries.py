#!/usr/bin/env python
import psycopg2

# Query to find most popular articles of all time?
Query1 = """select count(*) as num, articles.title
from log, articles
where log.path = \'/article/\' || articles.slug
group by articles.title
order by num desc
limit 3"""

# Query to find most popular articles authors of all time
Query2 = """select sum(pageviews.num) as sums, authors.name
from pageviews, authors
where authors.id = pageviews.author
group by pageviews.author, authors.name
order by sums desc"""

# Query to find percent error
Query3 = """select count(status),
round((count(status) filter (where status = '404 NOT FOUND') *
100.0 / count(status)  ),2),
date(time)
from log
group by date(time)
having round((count(status) filter (where status = '404 NOT FOUND') *
100.0 / count(status)  ),2) >= 1.0
"""


# Function to run queries
def connect_db():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    get_Query1(cursor)
    get_Query2(cursor)
    get_Query3(cursor)


def get_Query1(cursor):
    results = run_Queries(cursor, Query1)
    print "Top 3 Articles:"
    for row in results:
        print " ", row[1], " - ", row[0], "views"


def get_Query2(cursor):
    results = run_Queries(cursor, Query2)
    print
    print "Most popular Authors"
    for row in results:
        print " ", '%-32s' % (row[1],), " - ", '%6s' % (row[0],), "views"


def get_Query3(cursor):
    results = run_Queries(cursor, Query3)
    print
    print "Days where HTTP requests errors were greater than 1%"
    for row in results:
        print " ", (row[2]), "- Error:", str(row[1]) + "%"


def run_Queries(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    connect_db()
