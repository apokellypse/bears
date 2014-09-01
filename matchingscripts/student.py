"""author: Kelly Yu
date: August 31, 2014
purpose: student object for BEARS matching and parsing scripts
goal: store information about each person involved in BEARS in a happy, python manner"""

import re

class Student(object):
	"""Instance Attributes:
		name: the student's first and last name, separated by a space
		netid: the student's netid, which is 2-3 lowercase letters followed immediately by 2-3 numbers.
		role: mentor or mentee.
		school: what school the person is enrolled in at Cornell.
		major: what major(s) the person is considering or is familiar with.
		ethnicity: the ethnic background of the person.
		hometown: student's hometown
		religion: student's religion
		career: student's career interests (up to 3)
		club: student's extracurricular interests
		sport: favorite sports
		music: favorite genre
		personality: things like impulsiveness, organization, etc.
		preference:
		choice:
		"""

	def __init__(self, name="NA", 
		netid="na000", 
		birthday = "NA",
		role="NA", 
		school="NA", 
		major="NA", 
		ethnicity="NA", 
		hometown="NA", 
		religion="NA", 
		career="NA", 
		club='NA', 
		sport='NA', 
		music='NA', 
		personality='NA', 
		preference='NA', 
		choice='NA'):

		self.name = name
		self.netid = netid
		self.birthday = birthday
		self.role = role
		self.school = school
		self.major = major
		self.eth = ethnicity
		self.home = hometown
		self.rel = religion
		self.car = career
		self.club = club
		self.sport = sport
		self.music = music
		self.per = personality
		self.pref = preference
		self.cho = choice

		# assert 
		# add asserts later
		# re.match 



