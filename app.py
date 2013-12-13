#!/usr/bin/python

import sys
import MySQLdb
import cgi, cgitb
import os
from dbparams import myHost, myUser, myPasswd, myDb
import jinja2
from util import processList

cgitb.enable()

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

db = MySQLdb.connect(host = myHost, user = myUser, passwd = myPasswd, db = myDb)

print "Content-Type:text/html\r\n\r\n"

cursor = db.cursor()

#execute our static queries
cursor.execute("""select BUS.route, SUM(passengers)
		          from RIDES join BUS
		          on RIDES.b_id = BUS.b_id
		          where RIDES.passengers > 0
	    	      group by BUS.route;""")

totalTable = processList(["Route", "Total Riders"], cursor.fetchall())

cursor.execute("""select BUS.route, AVG(passengers) as 'Average Passengers' 
		          from RIDES join BUS
		          on RIDES.b_id = BUS.b_id
		          where RIDES.passengers > 0
		          group by BUS.route;""")

averageTable = processList(["Route", "Average Passengers"], cursor.fetchall()) 

cursor.execute("""select BUS.route, AVG(A.passengers) 
		          from
		          (select b_id, passengers, low_temp
		          from RIDES join WEATHER
		          on RIDES.date = WEATHER.date) as A		  
		          join BUS
		          on BUS.b_id = A.b_id
		          where A.low_temp < 30
		          group by BUS.route;""") 

temp30Table = processList(["Route", "Average Passengers"], cursor.fetchall())

cursor.execute("""select BUS.route, AVG(A.passengers)
		          from
		          (select b_id, passengers, low_temp
		          from RIDES join WEATHER
		          on RIDES.date = WEATHER.date) as A
		          join BUS
	 	          on BUS.b_id = A.b_id
		          where A.low_temp < 40
		          group by BUS.route;""")

temp40Table = processList(["Route", "Average Passengers"], cursor.fetchall())

cursor.execute("""select BUS.route, AVG(A.passengers)
                  from
                  (select b_id, passengers, low_temp
                  from RIDES join WEATHER
                  on RIDES.date = WEATHER.date) as A
                  join BUS
                  on BUS.b_id = A.b_id
                  where A.low_temp < 50
                  group by BUS.route;""")

temp50Table = processList(["Route", "Average Passengers"], cursor.fetchall())

cursor.execute("""select BUS.route, AVG(A.passengers)
                  from
                  (select b_id, passengers, low_temp
                  from RIDES join WEATHER
                  on RIDES.date = WEATHER.date) as A
                  join BUS
                  on BUS.b_id = A.b_id
                  where A.low_temp < 60
                  group by BUS.route;""")

temp60Table = processList(["Route", "Average Passengers"], cursor.fetchall())

cursor.execute("""select * from
                  (select A.route, A.passengers, A.date, B.avg from
                  (select BUS.route, RIDES.passengers, RIDES.date
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where RIDES.passengers > 0) as A
                  join (select AVG(passengers) as avg, BUS.route
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where passengers > 0
                  group by BUS.route) as B
                  on A.route = B.route) as C
                  where C.passengers > 2 * C.avg;""")

actual2xAverage = processList(["Route", "Passengers", "Date", "Route Average"], cursor.fetchall())

cursor.execute("""select * from
                  (select A.route, A.passengers, A.date, B.avg from
                  (select BUS.route, RIDES.passengers, RIDES.date
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where RIDES.passengers > 0) as A
                  join (select AVG(passengers) as avg, BUS.route
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where passengers > 0
                  group by BUS.route) as B
                  on A.route = B.route) as C
                  where C.passengers > 3 * C.avg;""")

actual3xAverage = processList(["Route", "Passengers", "Date", "Route Average"], cursor.fetchall())


cursor.execute("""select * from
                  (select A.route, A.passengers, A.date, B.avg from
                  (select BUS.route, RIDES.passengers, RIDES.date
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where RIDES.passengers > 0) as A
                  join (select AVG(passengers) as avg, BUS.route
                  from RIDES join BUS
                  on RIDES.b_id = BUS.b_id
                  where passengers > 0
                  group by BUS.route) as B
                  on A.route = B.route) as C
                  where C.passengers < 0.25 * C.avg;""")

actualHalfAverage = processList(["Route", "Passengers", "Date", "Route Average"], cursor.fetchall())

cursor.execute("""select HOLIDAYS.name, AVG(RIDES.passengers)
                  from RIDES join HOLIDAYS
                  on RIDES.date = HOLIDAYS.date
                  where RIDES.passengers > 0
                  group by HOLIDAYS.name""")

holidays = processList(["Holiday", "Average Passengers"], cursor.fetchall())

temp_vals = {}

template = jinja_environment.get_template("app.html")
print template.render(temp_vals)

print "1: CCC Routes and Total Riders For 2010-2012"
print totalTable
print "<br>"

print "2: CCC Routes and Average Riders Per Day For 2010-2012"
print averageTable
print "<br>"

print "3: Average CCC Ridership Based on Temperature <br>"
print "a. Average ridership when the low temperature is less than 30 degrees Fahrenheit"
print temp30Table
print "<br>"

print "b. Average ridership when the low temperature is less than 40 degrees Fahrenheit"
print temp40Table
print "<br>"

print "c. Average ridership when the low temperature is less than 50 degrees Fahrenheit"
print temp50Table
print "<br>"

print "d. Average ridership when the low temperature is less than 60 degrees Fahrenheit"
print temp60Table
print "<br>"

print "4: Ridership On Unusual Days (Average Ridership is Not Near Normal) <br>"
print "a. Days when the actual ridership is more than twice the average"
print actual2xAverage
print "<br>"

print "b. Days when the actual ridership is more than thrice the average"
print actual3xAverage
print "<br>"

print "c. Days when the actual ridership is less than one-quarter the average"
print actualHalfAverage
print "<br>"

print "5: The average CCC ridership during Holidays"
print holidays
print "<br>"

template = jinja_environment.get_template("rest.html")
print template.render()

db.close()








