# Udacity Full Stack Web Developer Logs Analysis Project

This Project uses python DB-API to connect to a psql database with over a million rows of data. and runs 3 queries which are printed to the console. The queries print out the top articles, top authors, and days with HTTP request errors greater than 1%. The data i

#### View Made
```
create view pageviews as
select count(*) as num, articles.title, articles.author
from log, articles
where log.path = '/article/' || articles.slug
group by articles.title, articles.author
order by num desc;
```
## Requirements

* Python 2
* Vagrant
* Virtual Box

## Instructions

* Install Vagrant and Virtual Box
* Clone the project
* Run virtual machine with `vagrant up`
* Connect to VM with `vagrant ssh`
* Load Database with `psql -d news -f newsdata.sql`
* Run program with `news-queries.py`

## Creator
Dylan Ellison
