"""author: Kelly Yu
date: August 31, 2014
purpose: BEARS parsing script
goal: take the data from the XML file from Cornell Qualtrics and separate into Python objects."""

"""
CONCERNS:
1. IF THE STUDENT PICKED MORE THAN ONE MAJOR, ONLY THE FIRST ONE WILL BE DISPLAYED
3. use indicies to save line space. I want it around 250 lines.
"""

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
	as_majors = ['africana', 'amurica', 'anthr', 'archae', 'asian', 'astro', 'biosci', 'biosoc', 'chembio', 'china', 'class', 'complit', 'cs', 'econ', 'eng', 'fem', 'french', 'german', 'gov', 'hist', 'histart', 'infosci', 'ital', 'ling', 'math', 'music', 'eaststu', 'perf', 'phil', 'phys', 'psych', 'relistu', 'romance', 'scitech', 'sciear', 'soc', 'stat']
	eng_majors = ['bioeng', 'cheme', 'civeng', 'cs', 'ece', 'engphy', 'enveng', 'indmaj', 'infosci', 'matsci', 'meche', 'orie', 'sciear']
	# hot_majors = ['hotel']
	hum_majors = ['biosoc', 'desenv', 'fash', 'fiber', 'globheal', 'humbio', 'humdev', 'nutsci', 'polana']
	# ilr_majors = ['ilr']


	def determine_major(string_regex, majors_list):
	#there are some ways to write this more concisely...I'll put those in later
		assert type(string_regex) == str
		assert type(majors_list) == list
		major_counter = 0
		for onions in french_onion_soup.findAll(re.compile(string_regex)):
			if onions.text == "1":
				if s.major == 'NA':
					s.major = [majors_list[major_counter]] #makes it a list
				else:
					s.major.append(majors_list[major_counter])
			major_counter += 1
		print "MAJOR: " + str(s.major)

	if s.school == "CALS":
		determine_major('(Q5_[0-9]{1,2})', cals_majors)
	elif s.school == 'AAP':
		determine_major('(Q29_[0-9]{1})', aap_majors)
	elif s.school == 'AS':
		determine_major('(Q30_[0-9]{1,2})', as_majors)
	elif s.school == 'ENG':
		determine_major('(Q31_[0-9]{1,2})', eng_majors)
	elif s.school == 'HOT':
		s.major = 'hotel'
	elif s.school == 'HUM':
		determine_major('(Q33_[0-9]{1})', hum_majors)	
	elif s.school == 'ILR':
		s.school == 'ilr'
	else:
		print 'you are in trouble'


	"""if s.school == 'CALS':
		major_counter = 0
		for q in french_onion_soup.findAll(re.compile('(Q5_[0-9]{1,2})')):
			if q.text == "1":
				if s.major == 'NA':
					s.major = cals_majors[major_counter]
				else:
					s.major.append(cals_majors[major_counter])

			major_counter += 1

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
	elif s.school == 'ENG':
		for noodles in french_onion_soup.findAll(re.compile('(Q31_[0-9]{1,2})')):
			if noodles.text == "1":
				s.major = eng_majors[major_counter]
				major_counter = 0
				break;
			else: 
				major_counter += 1

	elif s.school == 'HOT':
		s.major = 'hotel'

	elif s.school == 'HUM':
		for ramen in french_onion_soup.findAll(re.compile('(Q33_[0-9]{1})')):
			if ramen.text == "1":
				s.major = hum_majors[major_counter]
				major_counter = 0
				break;
			else:
				major_counter += 1
	elif s.school == 'ILR':
		s.major = 'ilr'
	else:
		print 'SOMETHING WRONG HAPPENED HERE'

	print "MAJOR: " + s.major"""

	#ETHNICITY
	p = french_onion_soup.find('Q6')
	eth = ""
	if p.text == "1":
		eth = 'White'
	elif p.text == "11":
		eth = 'Middle Eastern'
	elif p.text == "2":
		eth = 'Black/African-American'
	elif p.text == "3":
		eth = 'Latino/Hispanic'
	elif p.text == "4":
		eth = 'East Asian'
	elif p.text == "5":
		eth = 'South Asian'
	elif p.text == "13":
		eth = 'Pacific Islander'
	elif p.text == "6":
		eth = 'Native American'
	elif p.text == "7":
		eth = 'Other'
	s.ethnicity = eth

	pt = french_onion_soup.find('Q6_TEXT')
	if pt.text != "":
		s.ethnicity = pt.text;

	print 'ETHNICITY: ' + s.ethnicity

	#HOMETOWN
	h = french_onion_soup.find('Q17')
	s.hometown = h.text

	print 'HOMETOWN: ' + s.hometown

	#RELIGION
	r = french_onion_soup.find('Q12')
	rel = ""
	if r.text == "1":
		rel = 'Christian'
	elif r.text == "2":
		rel = 'Jewish'
	elif r.text == "3":
		rel = 'Muslim'
	elif r.text == "4":
		rel = 'Hindu'
	elif r.text == "5":
		rel = 'Buddhist'
	elif r.text == "6":
		rel = 'Atheist/Agnostic'
	elif r.text == "7":
		rel = 'Other'
	s.religion = rel

	rt = french_onion_soup.find('Q12_TEXT')
	if rt.text != '':
		s.religion = rt.text

	print 'RELIGION: ' + s.religion

	#CAREER INTERESTS
	career_options = ['broadcasting', 'journalism', 'publishing', 'architecture', 'culinaryart', 
	'fineart', 'photography', 'performingarts', 'music','design', 
	'marketing/adv', 'pr', 'finance', 'accounting', 'entre', 
	'mgmtcounsel', 'hr', 'realestate', 'hotelmgmt', 'fashion', 
	'stat/math', 'sports', 'teachingk12', 'university/coll', 'administration', 
	'research', 'coaching', 'meche', 'ece', 'cive', 
	'cheme', 'aeroe', 'manufac', 'infosci', 'cs', 
	'productdes', 'envsci', 'geo', 'energy', 'forestry/wild', 
	'parks/rec', 'nurse', 'pharm', 'diet', 'doctor', 
	'labresearch', 'vet', 'pubheal', 'emecare', 'langtrans', 
	'foreignserv', 'internongov', 'intertrade', 'attorney', 'judge', 
	'pubserv', 'corporate', 'legal', 'socialwork', 'psych/couns', 
	'clergy', 'nonprofit', 'gov/pol', 'natsec', 'other']

	career_counter = 0
	for broth in french_onion_soup.findAll(re.compile('(Q16_[0-9]{1,2})')):
		if broth.text == '1':
			# print career_counter
			# print len(career_options)
			if s.career == "NA": 
				s.career = [career_options[career_counter]]
			else:
				s.career.append(career_options[career_counter])
		career_counter += 1
	print 'CAREER: ' + str(s.career)
	# s.career = career_options[int(c.text)]









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

