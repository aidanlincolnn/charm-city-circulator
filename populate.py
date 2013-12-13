import MySQLdb
from dbparams import myHost, myUser, myPasswd, myDb
import sys
import os

db = MySQLdb.connect(host = myHost, user = myUser, passwd = myPasswd, db = myDb)
cursor = db.cursor()

queries = []

#populate the buses
queries.append("insert into BUS (b_id, route) values (0, 'orange');")
queries.append("insert into BUS (b_id, route) values (1, 'purple');")
queries.append("insert into BUS (b_id, route) values (2, 'green');")
queries.append("insert into BUS (b_id, route) values (3, 'banner');")

#populate the holidays (we use FEDERAL holidays)
#sourced from http://archive.opm.gov/operating_status_schedules/fedhol/2013.asp
queries.append("insert into HOLIDAYS (h_id, date, name) values (0, STR_TO_DATE('01-01-2010', '%m-%d-%Y'), 'New Years Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (1, STR_TO_DATE('01-18-2010', '%m-%d-%Y'), 'MLK Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (2, STR_TO_DATE('02-15-2010', '%m-%d-%Y'), 'Washingtons Birthday');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (3, STR_TO_DATE('05-31-2010', '%m-%d-%Y'), 'Memorial Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (4, STR_TO_DATE('07-05-2010', '%m-%d-%Y'), 'Independence Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (5, STR_TO_DATE('09-06-2010', '%m-%d-%Y'), 'Labor Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (6, STR_TO_DATE('10-11-2010', '%m-%d-%Y'), 'Columbus Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (7, STR_TO_DATE('11-11-2010', '%m-%d-%Y'), 'Veterans Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (8, STR_TO_DATE('11-25-2010', '%m-%d-%Y'), 'Thanksgiving Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (9, STR_TO_DATE('12-25-2010', '%m-%d-%Y'), 'Christmas Day');")

queries.append("insert into HOLIDAYS (h_id, date, name) values (10, STR_TO_DATE('12-31-2010', '%m-%d-%Y'), 'New Years Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (11, STR_TO_DATE('01-17-2011', '%m-%d-%Y'), 'MLK Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (12, STR_TO_DATE('02-21-2011', '%m-%d-%Y'), 'Washingtons Birthday');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (13, STR_TO_DATE('05-30-2011', '%m-%d-%Y'), 'Memorial Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (14, STR_TO_DATE('07-04-2011', '%m-%d-%Y'), 'Independence Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (15, STR_TO_DATE('09-05-2011', '%m-%d-%Y'), 'Labor Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (16, STR_TO_DATE('10-10-2011', '%m-%d-%Y'), 'Columbus Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (17, STR_TO_DATE('11-11-2011', '%m-%d-%Y'), 'Veterans Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (18, STR_TO_DATE('11-24-2011', '%m-%d-%Y'), 'Thanksgiving Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (19, STR_TO_DATE('12-26-2011', '%m-%d-%Y'), 'Christmas Day');")

queries.append("insert into HOLIDAYS (h_id, date, name) values (20, STR_TO_DATE('01-02-2012', '%m-%d-%Y'),'New Years Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (21, STR_TO_DATE('01-16-2012', '%m-%d-%Y'), 'MLK Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (22, STR_TO_DATE('02-20-2012', '%m-%d-%Y'), 'Washingtons Birthday');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (23, STR_TO_DATE('05-28-2012', '%m-%d-%Y'), 'Memorial Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (24, STR_TO_DATE('07-04-2012', '%m-%d-%Y'), 'Independence Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (25, STR_TO_DATE('09-03-2012', '%m-%d-%Y'), 'Labor Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (26, STR_TO_DATE('10-08-2012', '%m-%d-%Y'), 'Columbus Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (27, STR_TO_DATE('11-12-2012', '%m-%d-%Y'), 'Veterans Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (28, STR_TO_DATE('11-22-2012', '%m-%d-%Y'), 'Thanksgiving Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (29, STR_TO_DATE('12-25-2012', '%m-%d-%Y'), 'Christmas Day');")

queries.append("insert into HOLIDAYS (h_id, date, name) values (30, STR_TO_DATE('01-01-2013', '%m-%d-%Y'), 'New Years Day');") 
queries.append("insert into HOLIDAYS (h_id, date, name) values (31, STR_TO_DATE('01-21-2013', '%m-%d-%Y'), 'MLK Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (32, STR_TO_DATE('02-18-2013', '%m-%d-%Y'), 'Washingtons Birthday');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (33, STR_TO_DATE('05-27-2013', '%m-%d-%Y'), 'Memorial Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (34, STR_TO_DATE('07-04-2013', '%m-%d-%Y'), 'Independence Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (35, STR_TO_DATE('09-02-2013', '%m-%d-%Y'), 'Labor Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (36, STR_TO_DATE('10-14-2013', '%m-%d-%Y'), 'Columbus Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (37, STR_TO_DATE('11-11-2013', '%m-%d-%Y'), 'Veterans Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (38, STR_TO_DATE('11-28-2013', '%m-%d-%Y'), 'Thanksgiving Day');")
queries.append("insert into HOLIDAYS (h_id, date, name) values (39, STR_TO_DATE('12-25-2013', '%m-%d-%Y'), 'Christmas Day');")

#populate the sports (Football for now, maybe Baseball later)
#Sourced from http://www.fbschedules.com/nfl-10/2010-baltimore-ravens-football-schedule.php (and 2011, 2012, 2013)
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (0, 'football', STR_TO_DATE('09-26-2010', '%m-%d-%Y'), 'Ravens', 'Browns');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (1, 'football', STR_TO_DATE('10-10-2010', '%m-%d-%Y'), 'Ravens', 'Broncos');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (2, 'football', STR_TO_DATE('10-24-2010', '%m-%d-%Y'), 'Ravens', 'Bills');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (3, 'football', STR_TO_DATE('11-07-2010', '%m-%d-%Y'), 'Ravens', 'Dolphins');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (4, 'football', STR_TO_DATE('11-28-2010', '%m-%d-%Y'), 'Ravens', 'Buccaneers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (5, 'football', STR_TO_DATE('12-05-2010', '%m-%d-%Y'), 'Ravens', 'Steelers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (6, 'football', STR_TO_DATE('12-19-2010', '%m-%d-%Y'), 'Ravens', 'Saints');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (7, 'football', STR_TO_DATE('01-02-2011', '%m-%d-%Y'), 'Ravens', 'Bengals');")

queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (8, 'football', STR_TO_DATE('09-11-2011', '%m-%d-%Y'), 'Ravens', 'Steelers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (9, 'football', STR_TO_DATE('10-02-2011', '%m-%d-%Y'), 'Ravens', 'Jets');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (10, 'football', STR_TO_DATE('10-16-2011', '%m-%d-%Y'), 'Ravens', 'Texans');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (11, 'football', STR_TO_DATE('10-30-2011', '%m-%d-%Y'), 'Ravens', 'Cardinals');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (12, 'football', STR_TO_DATE('11-20-2011', '%m-%d-%Y'), 'Ravens', 'Bengals');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (13, 'football', STR_TO_DATE('11-24-2011', '%m-%d-%Y'), 'Ravens', '49ers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (14, 'football', STR_TO_DATE('12-11-2011', '%m-%d-%Y'), 'Ravens', 'Colts');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (15, 'football', STR_TO_DATE('12-24-2011', '%m-%d-%Y'), 'Ravens', 'Browns');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (16, 'football', STR_TO_DATE('01-15-2012', '%m-%d-%Y'), 'Ravens', 'Texans');")

queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (17, 'football', STR_TO_DATE('09-10-2012', '%m-%d-%Y'), 'Ravens', 'Bengals');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (18, 'football', STR_TO_DATE('09-23-2012', '%m-%d-%Y'),'Ravens', 'Patriots');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (19, 'football', STR_TO_DATE('09-27-2012', '%m-%d-%Y'), 'Ravens', 'Browns');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (20, 'football', STR_TO_DATE('10-14-2012', '%m-%d-%Y'), 'Ravens', 'Cowboys');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (21, 'football', STR_TO_DATE('11-11-2012', '%m-%d-%Y'), 'Ravens', 'Raiders');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (22, 'football', STR_TO_DATE('12-02-2012', '%m-%d-%Y'), 'Ravens', 'Steelers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (23, 'football', STR_TO_DATE('12-16-2012', '%m-%d-%Y'), 'Ravens', 'Broncos');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (24, 'football', STR_TO_DATE('12-23-2012', '%m-%d-%Y'), 'Ravens', 'Giants');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (25, 'football', STR_TO_DATE('01-06-2013', '%m-%d-%Y'), 'Ravens', 'Colts');")

queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (26, 'football', STR_TO_DATE('09-15-2013', '%m-%d-%Y'), 'Ravens', 'Browns');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (27, 'football', STR_TO_DATE('09-22-2013', '%m-%d-%Y'), 'Ravens', 'Texans');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (28, 'football', STR_TO_DATE('10-13-2013', '%m-%d-%Y'), 'Ravens', 'Packers');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (29, 'football', STR_TO_DATE('11-10-2013', '%m-%d-%Y'), 'Ravens', 'Bengals');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (30, 'football', STR_TO_DATE('11-24-2013', '%m-%d-%Y'), 'Ravens', 'Jets');")
queries.append("insert into SPORTS (s_id, sport, date, home_team, away_team) values (31, 'football', STR_TO_DATE('11-28-2013', '%m-%d-%Y'), 'Ravens', 'Steelers');")

#Populate the events
#Sourced from Wikipedia
queries.append("insert into EVENTS (e_id, name, date) values (0, 'Otakon', STR_TO_DATE('07-30-2010', '%m-%d-%Y'));") 
queries.append("insert into EVENTS (e_id, name, date) values (1, 'Otakon', STR_TO_DATE('07-31-2010', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (2, 'Otakon', STR_TO_DATE('08-01-2010', '%m-%d-%Y'));")

queries.append("insert into EVENTS (e_id, name, date) values (3, 'Otakon', STR_TO_DATE('07-29-2011', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (4, 'Otakon', STR_TO_DATE('07-30-2011', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (5, 'Otakon', STR_TO_DATE('07-31-2011', '%m-%d-%Y'));")

queries.append("insert into EVENTS (e_id, name, date) values (6, 'Otakon', STR_TO_DATE('07-27-2012', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (7, 'Otakon', STR_TO_DATE('07-28-2012', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (8, 'Otakon', STR_TO_DATE('07-29-2012', '%m-%d-%Y'));")

queries.append("insert into EVENTS (e_id, name, date) values (9, 'Otakon', STR_TO_DATE('08-09-2013', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (10, 'Otakon', STR_TO_DATE('08-10-2013', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (11, 'Otakon', STR_TO_DATE('08-11-2013', '%m-%d-%Y'));")

queries.append("insert into EVENTS (e_id, name, date) values (12, 'Grand Prix', STR_TO_DATE('09-04-2011', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (13, 'Grand Prix', STR_TO_DATE('09-02-2012', '%m-%d-%Y'));")
queries.append("insert into EVENTS (e_id, name, date) values (14, 'Grand Prix', STR_TO_DATE('09-01-2013', '%m-%d-%Y'));")

#populate the circulator data
#Sourced from https://data.baltimorecity.gov/Transportation/Charm-City-Circulator-Ridership/wwvu-583r
#Replaced all null values with 0
csv = open("circulator.csv", "r")
csv.readline()

count = 0
for line in csv.readlines():
	current = line.split(",")
	date = current[1].replace("/", "-")
	
	queries.append("insert into RIDES (r_id, b_id, date, passengers) values (" + str(count) + ", 0, STR_TO_DATE(\'" + date + "\', '%m-%d-%Y'), " + current[4] + ");")
	count = count + 1

	queries.append("insert into RIDES (r_id, b_id, date, passengers) values (" + str(count) + ", 1, STR_TO_DATE(\'" + date + "\', '%m-%d-%Y')," + current[7] + ");")
	count = count + 1

	queries.append("insert into RIDES (r_id, b_id, date, passengers) values (" + str(count) + ", 2, STR_TO_DATE(\'" + date + "\', '%m-%d-%Y')," + current[10] + ");")
	count = count + 1

	queries.append("insert into RIDES (r_id, b_id, date, passengers) values (" + str(count) + ", 3, STR_TO_DATE(\'" + date + "\', '%m-%d-%Y')," + current[13] + ");")
	count = count + 1

csv.close()

#Get a selection of weather
#Sourced from the National Climatic Data Center (National Oceanic and Atmospheric Administration
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (0, STR_TO_DATE('01-11-2011', '%m-%d-%Y'), 38, 30);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (1, STR_TO_DATE('01-18-2010', '%m-%d-%Y'), 57, 49);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (2, STR_TO_DATE('01-19-2010', '%m-%d-%Y'), 59, 48);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (3, STR_TO_DATE('01-20-2010', '%m-%d-%Y'), 44, 41);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (4, STR_TO_DATE('01-30-2010', '%m-%d-%Y'), 23, 20);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (5, STR_TO_DATE('01-31-2010', '%m-%d-%Y'), 32, 24);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (6, STR_TO_DATE('02-01-2010', '%m-%d-%Y'), 37, 25);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (7, STR_TO_DATE('02-02-2010', '%m-%d-%Y'), 37, 28);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (8, STR_TO_DATE('02-03-2010', '%m-%d-%Y'), 44, 31);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (9, STR_TO_DATE('02-07-2010', '%m-%d-%Y'), 32, 19);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (10, STR_TO_DATE('07-05-2010', '%m-%d-%Y'), 101, 76);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (11, STR_TO_DATE('07-06-2010', '%m-%d-%Y'), 105, 83);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (12, STR_TO_DATE('07-07-2010', '%m-%d-%Y'), 102, 85);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (13, STR_TO_DATE('07-08-2010', '%m-%d-%Y'), 95, 79);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (14, STR_TO_DATE('07-09-2010', '%m-%d-%Y'), 93, 77);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (15, STR_TO_DATE('07-10-2010', '%m-%d-%Y'), 81, 73);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (16, STR_TO_DATE('02-01-2011', '%m-%d-%Y'), 35, 30);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (17, STR_TO_DATE('02-02-2011', '%m-%d-%Y'), 49, 34);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (18, STR_TO_DATE('02-03-2011', '%m-%d-%Y'), 36, 29);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (19, STR_TO_DATE('02-04-2011', '%m-%d-%Y'), 43, 28);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (20, STR_TO_DATE('02-05-2011', '%m-%d-%Y'), 42, 34);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (21, STR_TO_DATE('02-06-2011', '%m-%d-%Y'), 48, 37);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (22, STR_TO_DATE('06-01-2012', '%m-%d-%Y'), 84, 63);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (23, STR_TO_DATE('06-02-2012', '%m-%d-%Y'), 77, 63);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (24, STR_TO_DATE('06-03-2012', '%m-%d-%Y'), 83, 62);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (25, STR_TO_DATE('06-04-2012', '%m-%d-%Y'), 77, 62);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (26, STR_TO_DATE('06-05-2012', '%m-%d-%Y'), 73, 59);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (27, STR_TO_DATE('06-09-2012', '%m-%d-%Y'), 95, 70);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (28, STR_TO_DATE('06-10-2012', '%m-%d-%Y'), 96, 75);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (29, STR_TO_DATE('06-11-2012', '%m-%d-%Y'), 94, 76);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (30, STR_TO_DATE('06-12-2012', '%m-%d-%Y'), 80, 71);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (31, STR_TO_DATE('11-12-2012', '%m-%d-%Y'), 71, 51);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (32, STR_TO_DATE('11-13-2012', '%m-%d-%Y'), 64, 43);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (33, STR_TO_DATE('11-14-2012', '%m-%d-%Y'), 50, 40);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (34, STR_TO_DATE('11-15-2012', '%m-%d-%Y'), 51, 42);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (35, STR_TO_DATE('11-16-2012', '%m-%d-%Y'), 54, 44);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (36, STR_TO_DATE('11-17-2012', '%m-%d-%Y'), 58, 43);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (37, STR_TO_DATE('12-07-2012', '%m-%d-%Y'), 51, 39);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (38, STR_TO_DATE('12-08-2012', '%m-%d-%Y'), 58, 49);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (39, STR_TO_DATE('12-09-2012', '%m-%d-%Y'), 54, 48);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (40, STR_TO_DATE('12-10-2012', '%m-%d-%Y'), 63, 48);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (41, STR_TO_DATE('02-04-2013', '%m-%d-%Y'), 35, 27);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (42, STR_TO_DATE('02-05-2013', '%m-%d-%Y'), 41, 35);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (43, STR_TO_DATE('02-06-2013', '%m-%d-%Y'), 43, 37);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (44, STR_TO_DATE('02-07-2013', '%m-%d-%Y'), 40, 33);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (45, STR_TO_DATE('02-08-2013', '%m-%d-%Y'), 51, 37);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (46, STR_TO_DATE('02-09-2013', '%m-%d-%Y'), 43, 32);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (47, STR_TO_DATE('02-10-2013', '%m-%d-%Y'), 39, 30);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (48, STR_TO_DATE('09-03-2011', '%m-%d-%Y'), 84, 72);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (49, STR_TO_DATE('09-04-2011', '%m-%d-%Y'), 88, 75);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (50, STR_TO_DATE('09-05-2011', '%m-%d-%Y'), 84, 75);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (51, STR_TO_DATE('09-06-2011', '%m-%d-%Y'), 77, 64);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (52, STR_TO_DATE('09-07-2011', '%m-%d-%Y'), 79, 66);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (53, STR_TO_DATE('09-08-2011', '%m-%d-%Y'), 77, 73);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (54, STR_TO_DATE('04-08-2012', '%m-%d-%Y'), 72, 50);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (55, STR_TO_DATE('04-09-2012', '%m-%d-%Y'), 69, 53);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (56, STR_TO_DATE('04-10-2012', '%m-%d-%Y'), 66, 59);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (57, STR_TO_DATE('04-11-2012', '%m-%d-%Y'), 56, 43);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (58, STR_TO_DATE('04-12-2012', '%m-%d-%Y'), 61, 45);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (59, STR_TO_DATE('04-13-2012', '%m-%d-%Y'), 66, 50);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (60, STR_TO_DATE('10-13-2010', '%m-%d-%Y'), 73, 51);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (61, STR_TO_DATE('10-14-2010', '%m-%d-%Y'), 62, 53);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (62, STR_TO_DATE('10-15-2010', '%m-%d-%Y'), 62, 50);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (63, STR_TO_DATE('10-16-2010', '%m-%d-%Y'), 66, 53);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (64, STR_TO_DATE('10-17-2010', '%m-%d-%Y'), 77, 50);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (65, STR_TO_DATE('10-18-2010', '%m-%d-%Y'), 73, 54);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (66, STR_TO_DATE('10-29-2012', '%m-%d-%Y'), 60, 52);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (67, STR_TO_DATE('10-30-2012', '%m-%d-%Y'), 51, 44);")
queries.append("insert into WEATHER (w_id, date, high_temp, low_temp) values (68, STR_TO_DATE('10-31-2012', '%m-%d-%Y'), 55, 45);")

#Perform all of my queries
for query in queries:
	cursor.execute(query)

#Disconnect from the database
db.commit()
db.close()
