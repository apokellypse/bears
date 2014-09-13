"""author: Kelly Yu
date: September 7th, 2014
purpose: BEARS paring script
goal: sort students and mentors into lists, have them rate each mentor (give a score), then apply the Gale-Shapely algorithm, which is known to produce excellent results."""

tracker = []
blacklist = []
from parseInput import *
import copy

def matchmaker(bear, cub):
	assert type(bear) == list
	assert type(bear[0]) != int
	assert type(cub) == list

#this gives the cubs "proposal preference"
	count = 0
	for c in cub:
		print 'Student ' + str(count)
		for b in bear:
			#scoring based on preferences
			# print 'BEAR ' + b
			# print b.preference
			score = 0
			if 'college + major' in b.preference and 'college + major' in c.preference:
				if b.major == c.major and b.school == c.school:
					score += (27 - 3*c.preference.index('college + major'))
				if b.ethnicity == c.ethnicity:
					score += (27 - 3*c.preference.index('ethnicity'))
				if b.hometown == c.hometown:
					score += (27 - 3*c.preference.index('hometown'))
				if b.religion == c.religion:
					score += (27 - 3*c.preference.index('religion'))
				if b.career == c.career:
					score += (27 - 3*c.preference.index('career'))
				if b.club == c.club:
					score += (27 - 3*c.preference.index('club'))
				if b.sport == c.sport:
					score += (27 - 3*c.preference.index('sports'))
				if b.music == c.music:
					score += (27 - 3*c.preference.index('music'))
				if b.personality == c.personality:
					score += (27 - 3*c.preference.index('personality'))
			else:
				blacklist.append(b) #for those who didn't put prefs

			c.scores.append(score) #keeps track of each bear's score, baed on index.
			b.scores.append(score)
			#So, bear[0] has socre c.scores[0]
		count += 1

#crashes here
	print 'Ranking starts here'	
	# print cub[90].name
	# print cub[90].scores
	#ranking
	for c in cub:
		# print '\n SCORE IS:' + str(c.scores)
		temp = copy.deepcopy(c.scores) #don't want to destroy anything

		while max(temp) != -1:
			highest = max(temp)
			where = temp.index(highest)
			c.rankings.append(where)
			temp[where] = -1
			# if c == cub[90]:
			# 	print temp
			# 	assert c.scores == temp
		tracker.append(False)

	for b in bear:

		temp = copy.deepcopy(b.scores) #don't want to destroy anything
		# print temp
		# import pdb;pdb.set_trace()
		while max(temp) != -1:
			highest = max(temp)
			where = temp.index(highest)
			b.rankings.append(where)
			temp[where] = -1
	# if c is an int, use it to index into cub

	#now we start proposing
	while tracker.count(False) > 0: #while there are unmatched cubs
		print '\n TODAY WE MATCH ' + str(len(cub)) + ' CUBS WITH ' + str(len(bear)) + ' BEARS'
		for c in range(len(cub)): #iterating through students' indices

			print '\n    CURRENTLY MATCHING CUB ' + str(c)
			assert type(cub[c] != int)
			if cub[c].partnerID == -1:
				choice = 0;
				while cub[c].partnerID == -1:
					thepick = cub[c].rankings[choice] #returns you the index of your top choice
					print 'Attempt No. ' + str(choice) + ', CUB ' + str(c) + ' WANTS BEAR ' + str(thepick)
					if bear[thepick].partnerID == -1: #bear has no partner
						#store IDs
						bear[thepick].partnerID = c
						cub[c].partnerID = thepick 
						tracker[c] = True
						print 'BEAR IS CUBLESS, MATCH SUCCESSFUL'
						# break #get outta the while loop
					elif thepick == 52: #if Steph is chosen (her index is 52)
						if cub[c].gender != 'female':
							print "Let's try again, Steph."
						choice += 1
					#if bear already has a partner
					elif bear[thepick].scores[bear[thepick].partnerID] < bear[thepick].scores[c]: #if bear would be happier switching
						print 'BEAR ' + str(thepick) + ' ALREADY HAS A CUB, SWAP? YES'
						#so the first part of the above statement is the score the bear gave its current cub
						#the second part of the statement is the score the bear has given to the prospective
						#abandon cub
						cub[bear[thepick].partnerID].partnerID = -1
						#so in the above we want to departner the previous cub.
						#we look inside the list of cubs with the current bear's partnerID
						cub[bear[thepick].happiness].partnerID = -1
						
						#before we change the parterID, we record that the previous cub is now bear-less
						tracker[bear[thepick].partnerID] = False

						#re-pair

						#store IDs
						bear[thepick].partnerID = c #now official a pointer to the new cub
						cub[c].partnerID = thepick
						tracker[c] = True
						# break
					else: #bear is satisfied, but cub still alone
						print 'BEAR ' + str(thepick) + ' ALREADY HAS A CUB, SWAP? NO'
						choice += 1
					# print str(cub[c].partnerID)



	#calculate happiness
	#calculate it here rather than elsewhere hehe
	avg = 0
	total_happiness = 0
	steph_partner = ''
	kelly_partner = ''

	for c in range(len(cub)): 
		# print type(cub)
		# print cub
		# print type(cub[0])
		# # print cub[c].scores
		# print cub[0].scores
		# print (cub[0]).scores
		total_happiness += cub[c].scores[cub[c].partnerID]

		# print c.scores[c.partnerID]
		avg = float(total_happiness) / len(cub)
	print 'AVERAGE CUB SATISFACTION IS: ' + str(avg)

	total_happiness = 0
	for b in range(len(bear)):
		if bear[b].netid == 'spc87': 
			steph_partner = cub[bear[b].partnerID].name
			print 'Steph has an index of ' + str(b)
		if bear[b].netid == 'kly24':
			kelly_partner = cub[bear[b].partnerID].name
		total_happiness += bear[b].scores[bear[b].partnerID]
		avg = float(total_happiness) / len(bear)
	print 'AVERAGE BEAR SATISFACTION IS: ' + str(avg)

			# i = -1
			# for t in xrange(n):
			# 	i = c.scores(bookmark, i + 1)

	#special case for Stephanie Chan
	print 'Stephanie Chan is paired with ' + steph_partner
	print 'Kelly Yu is paired with ' + kelly_partner

	print 'Number of special requests: ' + str(len(requested_pairs))
	# print 'Number of blacklisted forms: ' + str(len(blacklist))
	print 'Number of mentees: ' + str(len(mentees))
	print 'Number of mentors: ' + str(len(mentors))

def printInfo(netid, bear, cub):
	for c in cub:
		if c.netid == netid:
			print 'Hi, my name is ' + str(c.name) + ' and my major is ' + str(c.major) + ' in the college of ' + str(c.school) + '. I am a ' + str(c.religion) + ' and I am a ' + str(c.gender) + '.'
	for b in bear:
		if b.netid == netid:
			print 'Hi, my name is ' + str(b.name) + ' and my major is ' + str(b.major) + ' in the college of ' + str(b.school) + '. I am a ' + str(b.religion) + ' and I am a ' + str(b.gender) + '.'

if __name__ == '__main__':
	matchmaker(mentors, mentees)
	printInfo('st586', mentors, mentees)
	printInfo('yy544', mentors, mentees)

