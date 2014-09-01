"""author: Kelly Yu
date: August 31, 2014
purpose: BEARS parsing script
goal: take the data from the XML file from Cornell Qualtrics and separate into Python objects."""

from student import *
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("input.xml"), "xml")
chicken_noodle_soup = []
LIST_OF_STUDENTS = []

"""Separating Responses for Sanity of Mind"""
for res in soup.findAll('Response'):
	chicken_noodle_soup.append(res)

"""Takes each response and generates a student"""
for chicken in range(len(chicken_noodle_soup)):
	# print chicken_noodle_soup[chicken]
	# print type(chicken_noodle_soup[chicken])
	s = Student()
	french_onion_soup = BeautifulSoup(str(chicken_noodle_soup[chicken]), "xml")

	#NAMES
	n = french_onion_soup.find('Q3_1_TEXT')
	s.name = n.text
	print "NAME: " + s.name

	#NETID
	n = french_onion_soup.find('Q3_2_TEXT')
	s.netid = n.text
	print "NETID: " + s.netid

	#BIRTHDAY
	b = french_onion_soup.find('Q3_3_TEXT')
	s.birthday = b.text 
	print "BIRTHDAY: " + s.birthday

	#MENTOR VS MENTEE
	m = french_onion_soup.find('Q28')
	s.role = "mentor" if m.text == "1" else "mentee" #I LOVE TERNARY OPS
	print "ROLE: " + s.role

	#GENDER
	g = french_onion_soup.find('Q25')
	s.gender = "male" if g.text =="1" else "female"
	print "GENDER: " + s.gender

	#YEAR
	#I WISH PYTHON HAD SWITCH STATEMENTS
	y = french_onion_soup.find('Q2')
	year_name = ""
	if (y.text == "1"):
		year_name = "freshman"
	elif (y.text == "2"):
		year_name = "sophomore"
	elif (y.text == "3"):
		year_name = "junior"
	else:
		year_name = "senior"
	s.year = year_name
	print "YEAR: " + s.year


	#COLLEGE
	c = french_onion_soup.find('Q4')
	college_name = ''
	if (c.text == "1"):
		college_name = 'CALS'
	elif (c.text == "2"):
		college_name = 'AAP'
	elif (c.text == "3"):
		college_name = 'AS'
	elif (c.text == "4"):
		college_name = 'ENG'
	elif (c.text == "5"):
		college_name = 'HOT'
		# LIST_OF_STUDENTS[counter].major = 'hot'
	elif (c.text == "6"):
		college_name = 'HUM'
	elif (c.text == "7"):
		college_name = 'ILR'
		# LIST_OF_STUDENTS[counter].major = 'ilr'
	else:
		print "you done messed up"
	s.school = college_name
	print "SCHOOL: " + s.school

	#MAJOR
	major_counter = 0
	cals_majors = ['agsci', 'anisci', 'aem', 'atsci', 'bioeng', 'biosci', 'biosoc', 'btry', 'comm', 'devsoc', 'ent', 'enveng', 'envsci', 'foodsci', 'infosci', 'indstu', 'intag', 'landarch', 'nutsci', 'plantsci', 'sciear', 'viti']
	aap_majors = ['arch', 'fineart', 'urb']
	as_majors = ['afistu', 'amstu', 'anthr', 'arch', 'asistu', 'astro', 'biosci', 'biosoc', 'chembio', 'china', 'class', 'complit', 'cs', 'econ', 'eng', 'em', 'fren', 'gestu', 'gov', 'hist', 'histart', 'infosci', 'ital', 'ling', 'math', 'mus', 'eaststu', 'perf' 'phil', 'phys', 'psych', 'romstu', 'scitech', 'sciear', 'soc', 'stat']


	#there are some ways to write this more concisely...I'll put those in later
	if s.school == 'CALS':
		for q in french_onion_soup.findAll(re.compile('(Q5_[0-9]{1,2})')):
			if q.text == "1":
				# print 'FOUND IT'
				s.major = cals_majors[major_counter]
				major_counter = 0
				break;
			else:
				major_counter += 1
				# print "MAJOR COUNTER = " + str(major_counter)

	elif s.school == 'AAP':
		for onions in french_onion_soup.findAll(re.compile('(Q29_[0-9]{1})')):
			if onions.text == "1":
				s.major = aap_majors[major_counter]
				major_counter = 0
				break;
			else:
				major_counter += 1

	elif s.school == 'AS':
		for french in french_onion_soup.findAll(re.compile('(Q30_[0-9]{1,2})')):
			if french.text == "1":
				s.major = as_majors[major_counter]
				major_counter = 0
				break;
			else:
				major_counter += 1

	print "MAJOR: " + s.major

# print names


#This will make a list of names:
# names = []
# netid = []
# birthday = []
# role = []
# gender = []
# year = []
# school = []
# major = []
# ethnicity = []
# hometown = []
# religion = []
# career = []
# club = []
# sport = []
# music = []
# personality = []
# preference = []
# choice = []

