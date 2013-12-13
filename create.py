import MySQLdb
from dbparams import myHost, myUser, myPasswd, myDb
import sys

db = MySQLdb.connect(host = myHost, user = myUser, passwd = myPasswd, db = myDb)

print "Are you sure you want to re-create the database?  ALL data will be lost: "
answer = sys.stdin.readline().strip("\n")

#Always ask if we want to run this.  This will drop EVERYTHING
if answer == "yes" or answer == "Yes":
	print "Resetting the database"

	#Create our cursor to access the database
	cursor = db.cursor()

	#Drop all of our tables
	try:
		cursor.execute("DROP TABLE RIDES")
		cursor.execute("DROP TABLE BUS")
		cursor.execute("DROP TABLE HOLIDAYS")
		cursor.execute("DROP TABLE SPORTS")
		cursor.execute("DROP TABLE EVENTS")
		cursor.execute("DROP TABLE WEATHER")
	except:
		print "No tables to delete"	

	#Create our new, blank tables
	rides = """
		 CREATE TABLE RIDES(
		 	r_id int not null primary key,
			b_id int not null,
            foreign key(b_id) references BUS(b_id),
			date date,
			passengers int
		 );
		 """

	bus = """
	      CREATE TABLE BUS(
	        b_id int not null primary key,
		    route text
	      );
	      """

	holidays = """
		   CREATE TABLE HOLIDAYS(
		   	h_id int not null primary key,
			date date,
			name text
		   );
		   """

	sports = """
		 CREATE TABLE SPORTS(
		 	s_id int not null primary key,
			sport text,
			date date,
			home_team text,
			away_team text
		 );
		 """
	
	events = """
		 CREATE TABLE EVENTS(
		 	e_id int not null primary key,
			date date,
			name text
		 );
		 """

	weather = """
		  CREATE TABLE WEATHER(
		  	w_id int not null primary key,
			date date,
			high_temp int,
			low_temp int
		  );
		  """
	
	cursor.execute(rides)
	cursor.execute(bus)
	cursor.execute(holidays)
	cursor.execute(sports)
	cursor.execute(events)
	cursor.execute(weather)	

	#Disconnect from the database
	db.commit()
	db.close()
