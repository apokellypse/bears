"""author: Kelly Yu
date: September 7th, 2014
purpose: BEARS paring script
goal: sort students and mentors into lists, have them rate each mentor (give a score), then apply the Gale-Shapely algorithm, which is known to produce excellent results."""

tracker = []

def matchmaker(bear, cub):
	assert type(bear) == list
	assert type(cub) == list

#this gives the cubs "proposal preference"
	for c in cub:
		for b in bear:
			#scoring based on preferences
			score = 0
			if b.major == c.major and b.college == c.college:
				score += c.preference.index('college + major')
			if b.ethnicity == c.ethnicity:
				score += c.preference.index('ethnicity')
			if b.hometown == c.hometown:
				score += c.preference.index('hometown')
			if b.religion == c.religion:
				score += c.preference.index('religion')
			if b.career == c.career:
				score += c.preference.index('career')
			if b.club == c.club:
				score += c.preference.index('career')
			if b.sports == c.sports:
				score += c.preference.index('sports')
			if b.music == c.music:
				score += c.preference.index('music')
			if b.personality == c.personality:
				score += c.preference.index('personality')
			c.scores.append(score) #keeps track of each bear's score, baed on index.
			#So, bear[0] has socre c.scores[0]

	#ranking
	for c in cub:
		temp = c.scores #don't want to destroy anything
		while max(temp) != -1:
			highest = max(temp)
			where = temp.index(highest)
			c.rankings.append(where)
			temp[where] = -1
		tracker.append(False)

	for b in bear:
		temp = b.scores #don't want to destroy anything
		while max(temp) != -1:
			highest = max(temp)
			where = temp.index(highest)
			b.rankings.append(where)
			temp[where] = -1


	#now we start proposing
	while tracker.count(False) > 0: #while there are unmatched cubs
		for c in range(len(cub)): #iterating through students' indices
			if cub[c].partnerID == -1:
				choice = 0;
				while cub[c].partnerID == -1:
					thepick = cub[c].rankings[choice] #returns you the index of your top choice
					if bear[thepick].partnerID == -1: #bear has no partner
						#store IDs
						bear[thepick].partnerID = c
						cub[c].partnerID = thepick 
						tracker[c] = True
						break #get outta the while loop

					#if bear already has a partner
					elif bear[thepick].scores[bear[thepick].partnerID] < bear[thepick].scores[cub[c]]: #if bear would be happier switching
						#abandon cub
						cub[bear[thepick]].partnerID = -1
						cub[bear[thepick]].happiness = -1
						tracker[c] = False

						#re-pair

						#store IDs
						bear[thepick].partnerID = c
						cub[c].partnerID = thepick 
						tracker[c] = True
						break
					else: #bear is satisfied, but cub still alone
						choice += 1



	#calculate happiness
	happiness = 0
	avg = 0
	for c in cub:
		happiness += c.scores[c.partnerID]
		avg = float(happiness) / len(cub)
	print 'AVERAGE CUB SATISFACTION IS: ' + str(avg)
	happiness = 0
	for b in bear:
		happiness += b.scores[b.partnerID]
		avg = float(happiness) / len(bear)
	print 'AVERAGE BEAR SATISFACTION IS: ' + str(avg)

			# i = -1
			# for t in xrange(n):
			# 	i = c.scores(bookmark, i + 1)

