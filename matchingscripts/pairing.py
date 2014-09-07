"""author: Kelly Yu
date: September 7th, 2014
purpose: BEARS paring script
goal: sort students and mentors into lists, have them rate each mentor (give a score), then apply the Gale-Shapely algorithm, which is known to produce excellent results."""

def matchmaker(bear, cub):
	assert type(bear) == list
	assert type(cub) == list)

#this gives the cubs "proposal preference"
	for c in cub:
		for b in bear:
			#scoring based on preferences
			score = 0
			if b.major == c.major && b.college == c.college:
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

	for b in bear:
		temp = b.scores #don't want to destroy anything
		while max(temp) != -1:
			highest = max(temp)
			where = temp.index(highest)
			b.rankings.append(where)
			temp[where] = -1


	#now we start proposing

	for c in range(len(cub)): #iterating through students' indices
		if cub[c].partnerID == -1:
			choice = 0;
			while cub[c].parterID = -1:
				thepick = cub[c].rankings[choice] #returns you the index of your top choice
				if bear[thepick].partnerID == -1: #bear has no partner
					#store IDs
					bear[thepick].partnerID = c
					cub[c].partnerID = thepick 
					break #get outta the while loop

				else: #bear has a partner
					if bear[thepick].happiness < bear[thepick].scores[cub[c].partnerID]: #if bear would be happier switching
						#abandon cub
						cub[bear[thepick]].partnerID = -1
						cub[bear[thepick]].happiness = -1

						#re-pair

						#store IDs
						bear[thepick].partnerID = c
						cub[c].partnerID = thepick 
						break
					else: #bear is satisfied, but cub still alone
						choice += 1

	#calculate happiness
	

			# i = -1
			# for t in xrange(n):
			# 	i = c.scores(bookmark, i + 1)

