#!/usr/bin/python

#Convert a list of headers and the result of a query (list of tuples)
#into an HTML table
def processList(headers, values):
	table = "<table border = '1', cellpadding = '4'>"
	table += "<tr>"

	#Setup the first row of our table
	for val in headers:
		table += "<th>" + val + "</th>"

	table+= "</tr>"

	#Populate the rest of the rows of our table
	for vals in values:
		table += "<tr>"
		for item in vals:
			table += "<td><center>" + str(item) + "</center></td>"		
		
		table += "</tr>"		

	table += "</table>"
	return table

#Get the month based on an input string
def getMonth(num):
    num = str(num)
    if num =="01":
        return "January"
    elif num =="02":
        return "February"
    elif num =="03":
        return "March"
    elif num =="04":
        return "April"
    elif num =="05":
        return "May"
    elif num =="06":
        return "June"
    elif num =="07":
        return "July"
    elif num =="08":
        return "August"
    elif num =="09":
        return "September"
    elif num =="10":
        return "October"
    elif num =="11":
        return "November"
    elif num =="12":
        return "December"
    else:
        return "BAD INPUT"

