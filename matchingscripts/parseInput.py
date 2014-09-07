"""author: Kelly Yu
date: August 31, 2014 - September 2, 2014
purpose: BEARS parsing script
goal: take the data from the XML file from Cornell Qualtrics and separate into Python objects."""

from student import *
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("input.xml"), "xml")
chicken_noodle_soup = []
mentors = []
mentees = []
mentor_count = 0
mentee_count = 0

#DATA
major_counter = 0
cals_majors = ['agsci', 'anisci', 'aem', 'atsci', 'bioeng', 
	'biosci', 'biosoc', 'btry', 'comm', 'devsoc', 
	'ent', 'enveng', 'envsci', 'foodsci', 'infosci', 
	'indstu', 'intag', 'landarch', 'nutsci', 'plantsci', 
	'sciear', 'viti']
aap_majors = ['arch', 'fineart', 'urb']
as_majors = ['africana', 'amurica', 'anthr', 'archae', 'asian', 
	'astro', 'biosci', 'biosoc', 'chembio', 'china', 
	'class', 'complit', 'cs', 'econ', 'eng', 
	'fem', 'french', 'german', 'gov', 'hist', 
	'histart', 'infosci', 'ital', 'ling', 'math', 
	'music', 'eaststu', 'perf', 'phil', 'phys', 
	'psych', 'relistu', 'romance', 'scitech', 'sciear', 
	'soc', 'stat']
eng_majors = ['bioeng', 'cheme', 'civeng', 'cs', 'ece', 
	'engphy', 'enveng', 'indmaj', 'infosci', 'matsci', 
	'meche', 'orie', 'sciear']
hum_majors = ['biosoc', 'desenv', 'fash', 'fiber', 'globheal', 
	'humbio', 'humdev', 'nutsci', 'polana']
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
club_options = ['greek', 'polt', 'env', 'dance', 'commserv', 
	'minority', 'proffrat', 'career', 'athletic', 'cultural', 
	'socialchange', 'other']
sports_list = ['archery', 'badminton', 'baseball', 'basketball', 'bowling', 
	'climbing', 'cycling', 'dance', 'equestrian', 'fishing', 
	'football', 'golf', 'gymnastics', 'lacrosse', 'martialarts', 
	'wrestling', 'skating', 'skiing', 'soccer', 'swimming', 
	'tennis', 'track', 'none', 'other']
music_list = ['alter', 'apop', 'classical', 'country', 'edm', 
	'euro', 'hiphop', 'jazz', 'latin', 'opera', 
	'pop', 'r&b', 'rock', 'none', 'other']
prefs_list = ['college + major', 'ethnicity', 'hometown', 'religion', 'career interests', 
	'club interests', 'sports', 'music', 'personality']

"""Separating Responses for Sanity of Mind"""
for res in soup.findAll('Response'):
	chicken_noodle_soup.append(res)

"""Takes each response and generates a student"""
for chicken in range(len(chicken_noodle_soup)):
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
	# assert re.search('([a-z^A-Z]{2,3}[0-9]{1,3}|[0-9]{7})', s.netid)

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
	y = french_onion_soup.find('Q2')
	year_name = ""
	if (y.text == "1"): year_name = "freshman"
	elif (y.text == "2"): year_name = "sophomore"
	elif (y.text == "3"): year_name = "junior"
	else: year_name = "senior"
	s.year = year_name
	print "YEAR: " + s.year

	#COLLEGE
	c = french_onion_soup.find('Q4')
	college_name = ''
	if (c.text == "1"): college_name = 'CALS'
	elif (c.text == "2"): college_name = 'AAP'
	elif (c.text == "3"): college_name = 'AS'
	elif (c.text == "4"): college_name = 'ENG'
	elif (c.text == "5"): college_name = 'HOT'
	elif (c.text == "6"): college_name = 'HUM'
	elif (c.text == "7"): college_name = 'ILR'
	else: print "you done messed up"
	s.school = college_name
	print "SCHOOL: " + s.school

	#MAJOR
	attribute = 'NA'
	def regexHandler(string_regex, majors_list):
		global attribute
		assert type(string_regex) == str
		assert type(majors_list) == list
		cloves_of_garlic = 0
		for onions in french_onion_soup.findAll(re.compile(string_regex)):
			if onions.text == "1":
				if type(attribute) != list:
					attribute = [majors_list[cloves_of_garlic]] #makes it a list
					assert type(attribute) == list
				else:
					attribute.append(majors_list[cloves_of_garlic])
			cloves_of_garlic += 1
			
	if s.school == "CALS": regexHandler('(Q5_[0-9]{1,2})', cals_majors)
	elif s.school == 'AAP': regexHandler('(Q29_[0-9]{1})', aap_majors)
	elif s.school == 'AS': regexHandler('(Q30_[0-9]{1,2})', as_majors)
	elif s.school == 'ENG': regexHandler('(Q31_[0-9]{1,2})', eng_majors)
	elif s.school == 'HOT': s.major = 'hotel'
	elif s.school == 'HUM': regexHandler('(Q33_[0-9]{1})', hum_majors)	
	elif s.school == 'ILR': s.school == 'ilr'
	else: print 'you are in trouble'
	s.major = attribute
	attribute = 'NA' #reset
	print 'MAJOR: ' + str(s.major)

	#ETHNICITY
	p = french_onion_soup.find('Q6')
	eth = ""
	if p.text == "1": eth = 'White'
	elif p.text == "11": eth = 'Middle Eastern'
	elif p.text == "2": eth = 'Black/African-American'
	elif p.text == "3": eth = 'Latino/Hispanic'
	elif p.text == "4": eth = 'East Asian'
	elif p.text == "5": eth = 'South Asian'
	elif p.text == "13": eth = 'Pacific Islander'
	elif p.text == "6": eth = 'Native American'
	elif p.text == "7": eth = 'Other'
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
	if r.text == "1": rel = 'Christian'
	elif r.text == "2": rel = 'Jewish'
	elif r.text == "3": rel = 'Muslim'
	elif r.text == "4": rel = 'Hindu'
	elif r.text == "5": rel = 'Buddhist'
	elif r.text == "6": rel = 'Atheist/Agnostic'
	elif r.text == "7": rel = 'Other'
	s.religion = rel

	rt = french_onion_soup.find('Q12_TEXT')
	if rt.text != '':
		s.religion = rt.text

	print 'RELIGION: ' + s.religion

	#CAREER INTERESTS
	regexHandler('(Q16_[0-9]{1,2})', career_options)
	s.career = attribute
	attribute = 'NA'
	# assert type(s.career) == list
	print 'CAREER: ' + str(s.career)
	# s.career = career_options[int(c.text)]

	#EXTRACURRICULAR INTERESTS
	regexHandler('(Q17_[0-9]{1,2})', club_options)

	s.club = attribute
	attribute = 'NA' #reset

	otherclub = french_onion_soup.find('Q17_12_TEXT')
	if otherclub.text != '':
		s.club[len(s.club)-1] = otherclub.text

	# assert type(s.club) == list
	print 'CLUB: ' + str(s.club)

	#SPORTS
	chosen_sport = french_onion_soup.find('Q15')

	if chosen_sport.text == '':
		print 'HE DID NOT FILL IT OUT'
	else:
		if chosen_sport.text == '24':
			other_sport = french_onion_soup.find('Q15_TEXT')
			s.sport = other_sport.text
		else:
			s.sport = sports_list[int(float(chosen_sport.text)) - 1]
	print 'SPORT: ' + str(s.sport)

	chosen_music = french_onion_soup.find('Q18')

	if chosen_music.text == '':
		print 'IF ONLY YOU LIKED MUSIC'
	else:
		if chosen_music.text == '15':
			other_music = french_onion_soup.find('Q18_TEXT')
			s.music = other_music.text
		else:
			s.music = music_list[int(float(chosen_music.text)) - 1]
	print 'MUSIC: ' + str(s.music)

	#PERSONALITY
	vert = french_onion_soup.find('Q20_1')
	action = french_onion_soup.find('Q20_2')
	worrymeter = french_onion_soup.find('Q20_3')
	neatness = french_onion_soup.find('Q20_4')
	thinking = french_onion_soup.find('Q20_5')

	#make a table to save space?

	shyornot = ''
	if vert.text == '1': shyornot = 'introverted'
	elif vert.text == '2': shyornot = 'neutralverted'
	elif vert.text == '3': shyornot = 'extraverted'
	else: print "are you shy or not?"

	actfast = ''
	if action.text == '1': actfast = 'thoughtful'
	elif action.text == '2': actfast = 'acts neither fast nor slow'
	elif action.text == '3': actfast = 'impulsive'
	else: print "are you thoughtful or impuslive?" 

	carelessful = ''
	if worrymeter.text == '1': carelessful = 'carefree'
	elif worrymeter.text == '2': carelessful = 'neither carefree nor worried'
	elif worrymeter.text == '3': carelessful = 'worried'
	else: print 'are you worried right now because I am'

	neatfreak = ''
	if neatness.text == '1': neatfreak = 'disorganized'
	elif neatness.text == '2': neatfreak = 'kinda messy but not really'
	elif neatness.text == '3': neatfreak = 'organized'
	else: print 'are you messy'

	brain = ''
	if thinking.text == '1': brain = 'practical'
	elif thinking.text == '2': brain = 'not that practical'
	elif thinking.text == '3': brain = 'idealistic'
	else: print 'is your head in the clouds'

	s.personality = [shyornot, actfast, carelessful, neatfreak, brain]
	print 'PERSONALITY: ' + str(s.personality)

	#PREFERENCES
	where = 0
	s.preference = ['', '', '', '', '', '', '', '', '']
	for baguette in french_onion_soup.findAll(re.compile('(Q19_[0-9]{1})')):
		# print baguette.text
		if baguette.text == '': 
			print 'what are you prefs son'
			break
		s.preference[int(float(baguette.text)) - 1] = prefs_list[where]
		where += 1
	print 'PREFERENCE: ' + str(s.preference)

	#SHIRTS
	sweats = french_onion_soup.find('Q18')
	tees = ''
	if sweats.text == '1': tees = 'S'
	elif sweats.text == '2': tees = 'M'
	elif sweats.text == '3': tees = 'L'
	elif sweats.text == '4': tees = 'XL'
	elif sweats.text == '5': tees = 'NONE'
	else: print 'stop refushing BEARS gear'

	s.tshirt = tees
	print 'TSHIRT SIZE: ' + tees

	#PARTNER REQUESTS
	guy1 = french_onion_soup.find('Q24_1_TEXT')
	guy2 = french_onion_soup.find('Q24_2_TEXT')
	s.request = [guy1.text, guy2.text]
	print 'REQUESTED: ' + str(s.request) + '\n'
	if str(s.request) == '': assert 3==2

	#SAVE
	if s.role == 'mentor': mentors.append(s)
	elif s.role == 'mentee': mentees.append(s)
	else: assert(1==2) #lol

def getMentees():
	return mentees

def getMentors():
	return mentors

if __name__ == '__main__':
	main()