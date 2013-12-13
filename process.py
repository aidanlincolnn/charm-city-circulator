#!/usr/bin/python

import sys
import MySQLdb
import cgi, cgitb
import os
import string
from util import processList, getMonth
from dbparams import myHost, myUser, myPasswd, myDb

cgitb.enable()

db = MySQLdb.connect(host = myHost, user = myUser, passwd = myPasswd, db = myDb)

print "Content-Type:text/html\r\n\r\n"

#Get the required parameter to process: option
#Based on this parameter, we execute some query
form = cgi.FieldStorage()
option = form.getvalue("option")

#Throw away any attacks against our database
def maliciousData(input):
    if(" " in input):
        print "Error Invalid Parameter, spaces in input"
        return False
    allowed_chars=string.ascii_letters + string.digits + '-'
    allowed_set = set(allowed_chars)
    not_allowed = ['select','from','join','on','where', 'sum', 'avg', 'stdev',';']

    hasIllegalChars = False
    onlyChars = set(input) - allowed_set
    if len(onlyChars) != 0:
        hasIllegalChars = True
    
    hasSql = False
    for statement in not_allowed:
        if statement in input.lower():
            hasSql = True
    if (hasSql or hasIllegalChars):
        print "Error Invalid Parameter: " +(input)
    return (not hasSql) and (not hasIllegalChars)

#Verify that our date inputs are formatted correctly
def verifyDate(input):
    input = str(input)
    date = True

    if (len(input) != 10):
        date = False
    else:
        if (not input[0].isdigit() or not input[1].isdigit()):
            date = False
        if (not input[3].isdigit() or not input[4].isdigit()):
            date = False
        if (not input[6].isdigit() or not input[7].isdigit() or not input[8].isdigit() or not input[9].isdigit()):
            date = False
        if (input[2] != '-' or input[5] != '-'):
            date = False

    if date == False:
        print "Incorrectly formatted date"

    return date


#find out the average CCC ridership when the Ravens play a particular team
if option == "1":
    data = form.getvalue("data")
    data = str(data)
    safe = maliciousData(data)
    if safe:
		cursor = db.cursor()
		cursor.execute("""select AVG(passengers) 
		                  from RIDES join SPORTS
				          on RIDES.date = SPORTS.date
				          where home_team = 'Ravens' 
				          and away_team = %s;""", (data))

		results = cursor.fetchone()
		print "The average ridership of the CCC when the Ravens play the " + data + " is: " + str(results[0])

#Show the average CCC ridership when the Ravens play 
if option == "2":
	cursor = db.cursor()
	cursor.execute("""select AVG(passengers)
		       	      from RIDES join SPORTS
		              on RIDES.date = SPORTS.date
		              where home_team = %s;""", ("Ravens"))

	results = cursor.fetchone()
	print "The average CCC ridership when the Ravens play is: " + str(results[0])

#Select the total number of CCC riders between two dates
if option == "3":
    data1 = form.getvalue("data1")
    data2 = form.getvalue("data2")
    data1 = str(data1)
    data2 = str(data2)
    correct = verifyDate(data1) and verifyDate(data2)
    safe = maliciousData(data1)
    safe = safe and maliciousData(data2)

    if safe and correct:
        cursor = db.cursor()
        query = "select SUM(passengers) from RIDES where RIDES.date >= STR_TO_DATE('" + data1 + "', '%m-%d-%Y') and RIDES.date <= STR_TO_DATE('" + data2 + "', '%m-%d-%Y');"
        cursor.execute(query)

        results = cursor.fetchone()
        print "The total riders on the CCC from " + data1 + " to " + data2 + " is: " + str(results[0])

#Select the total number of CCC riders on a particular route between two dates
if option == "4":
    data1 = str(form.getvalue("data1"))
    data2 = str(form.getvalue("data2"))
    data3 = str(form.getvalue("data3"))
    correct = verifyDate(data2) and  verifyDate(data1)
    safe = maliciousData(data1) and maliciousData(data2) and maliciousData(data3)

    if safe and correct:
        cursor = db.cursor()
        query = "select SUM(passengers) from RIDES join BUS on BUS.b_id = RIDES.b_id where RIDES.date >= STR_TO_DATE('" + data1 + "', '%m-%d-%Y') and RIDES.date <= STR_TO_DATE('" + data2 + "', '%m-%d-%Y') and BUS.route = '" + data3 + "';"

        cursor.execute(query)

        results = cursor.fetchone()
        print "The total riders on the " + data3 + " line from " + data1 + " to " + data2 + " is " + str(results[0])

#Select the average number of riders on the CCC on a given day
if option =="5":
    data1 = str(form.getvalue("data1"))
    data2 = str(form.getvalue("data2"))
    if (not data1.isdigit() or not data2.isdigit()):
        print "Day or Month is not valid"
    else:
        safe = maliciousData(data1)
        safe = safe and maliciousData(data2)

        if safe:
            cursor = db.cursor()
            cursor.execute("select AVG(passengers) from RIDES where DATE_FORMAT(RIDES.date,'%d') = '" + str(data1) + "' and DATE_FORMAT(RIDES.date,'%m') = '" + str(data2) + "';")

            results = cursor.fetchone()
            print "The average number of passengers riding the ccc on " + data2 + "/" + data1 + " is " + str(results[0])

#Get the average number of passengers riding the CCC in a given month
if option =="6":
    data1 = str(form.getvalue("data1"))
    safe = maliciousData(data1)
    if (not data1.isdigit()):
        print "That is not a valid month"
    else:
        if safe:
                cursor = db.cursor()
                cursor.execute("select AVG(passengers) from RIDES where DATE_FORMAT(RIDES.date,'%m') = '" + data1 + "';")

                results = cursor.fetchone()
                if (int(str(data1))>12 or int(str(data1))<1):
                    print "That is not a valid month"
                else:
                    print "The average daily number of passengers riding the ccc in "+ getMonth(data1)+ " is " + str(results[0])

#Get the average number of passengers riding the CCC in a given year
if option =="7":
    data1 = str(form.getvalue("data1"))
    safe = maliciousData(data1)
    if (not data1.isdigit()):
        print "That is not a valid year"
    else:
        if safe:
                cursor = db.cursor()
                cursor.execute("select AVG(passengers) from RIDES where DATE_FORMAT(RIDES.date,'%Y') = '" + data1 + "';")

                results = cursor.fetchone()
                print "The average daily number of passengers riding the CCC in  " + data1 + " is " + str(results[0])

#Select the maximum ridership on a given day between two dates for each CCC route
if option =="8":
    data1 = str(form.getvalue("data1"))
    data2 = str(form.getvalue("data2"))
    safe = maliciousData(data1)
    safe = safe and maliciousData(data2)
    correct = verifyDate(data1) and verifyDate(data2)
    if safe and correct:
            cursor = db.cursor()
            cursor.execute("select MAX(passengers) , BUS.route from RIDES join BUS on RIDES.b_id = BUS.b_id where RIDES.date >= STR_TO_DATE('" + data1 + "', '%m-%d-%Y') and RIDES.date <= STR_TO_DATE('" + data2 + "', '%m-%d-%Y')group by BUS.route;")
            results = cursor.fetchall()
            print "Line: " + str(results[0][1]) + ", Ridership: " + str(results[0][0])+"\nLine: " + str(results[1][1]) + ", Ridership: " + str(results[1][0])+"\nLine: " + str(results[2][1]) + ", Ridership: " + str(results[2][0])+"\nLine: " + str(results[3][1]) + ", Ridership: " + str(results[3][0])  
      
#Get the maximum average ridership of one route of the CCC between two dates
if option =="9":
    data1 = str(form.getvalue("data1"))
    data2 = str(form.getvalue("data2"))
    correct = verifyDate(data1) and verifyDate(data2)

    safe = maliciousData(data1)
    safe = safe and maliciousData(data2)
    
    if safe and correct:
            cursor = db.cursor()
            cursor.execute("select AVG(passengers) as A, BUS.route from RIDES join BUS on RIDES.b_id = BUS.b_id where RIDES.date >= STR_TO_DATE('" + data1 + "','%m-%d-%Y') and RIDES.date <= STR_TO_DATE('" + data2 + "', '%m-%d-%Y') group by BUS.route order by A desc;")
            #cursor.execute("select MAX(averages),route from (select AVG(passengers) as averages , BUS.route as route from RIDES join BUS on RIDES.b_id = BUS.b_id where RIDES.date >= STR_TO_DATE('" + data1 + "', '%m-%d-%Y') and RIDES.date <= STR_TO_DATE('" + data2 + "', '%m-%d-%Y')group by BUS.route) AS T1;")
            
            results = cursor.fetchone()
            print "Bus Line with maximum average ridership between " + data1 +" and " + data2 + ": " + str(results[1]) + ", Ridership: " + str(results[0])

#Get the average ridership on the CCC when the ravens play grouped by opponent
if option == "10":
    cursor = db.cursor()
    cursor.execute("""select AVG(passengers) as avg, SPORTS.away_team from RIDES join SPORTS on RIDES.date = SPORTS.date where home_team = 'Ravens' group by SPORTS.away_team order by avg;""")

    results = cursor.fetchall()
    for item in results:
        print "Away Team: " + item[1] + ", Ridership: " + str(item[0])

#Rank events in Baltimore sorted by total cc riders on that day
if option =="11":
    cursor = db.cursor()
    cursor.execute("select EVENTS.name, SUM(RIDES.passengers) as numpass, RIDES.date from RIDES join EVENTS on RIDES.date = EVENTS.date group by RIDES.date order by numpass DESC ;")
    results = cursor.fetchall()
    for item in results:
        print "Event: " + item[0] + ", Ridership: " + str(item[1])+ " Date: " + str(item[2])

#Compare ridership during the Baltimore Grand Prix between 2011 and 2012
if option =="12":
    cursor = db.cursor()
    
    cursor.execute("select SUM(passengers) , BUS.route ,RIDES.date from RIDES join BUS on RIDES.b_id = BUS.b_id join EVENTS on EVENTS.date = RIDES.date where EVENTS.name ='Grand Prix' group by RIDES.date, BUS.route order by BUS.route;")    
    results = cursor.fetchall()
    last = ["","",""]
    for item in results:
        print "Date: " + str(item[2]) + ", Line: "+ str(item[1]) + ", Ridership: " + str(item[0])
        if  str(last[1]) == str(item[1]):
            print "Difference between 2011 and 2012: " + str(item[0] - last[0])
        last = item

db.close()

