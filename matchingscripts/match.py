
names = []
netid = []
role = []
school = []
major = []
ethnicity = []
hometown = []
religion = []
career = []
club = []
sport = []
music = []
personality = []
preference = []
choice = []


f = open('Export.php.txt')
linenum = 0
for line in f:
	if (linenum < 212):
		linenum += 1
		pass
	else:
		linenum += 1
		if (linenum == 213):
			names.append(line)
		elif (linenum == 214):
			netid.append(line)
		elif (linenum == 215):
			pass
		elif (linenum == 216):
			if ('1' in line):
				role.append("mentor")
			else:
				role.append("mentee")
		elif (linenum == 219):
			if ('1' in line):
				school.append('ALS')
			elif ('2' in line):
				school.append('AAP')
			elif ('3' in line):
				school.append('AS')
			elif ('4' in line):
				school.append('ENG')
			elif ('5' in line):
				school.append('HOT')
				major.append('hot')
			elif ('6' in line):
				school.append('HUM')
			elif ('7' in line):
				school.append('ILR')
				major.append('ilr')
		elif (linenum == 220):
			if ('1' in line):
				major.append('agsci')
			else:
				pass
		elif (linenum == 221):
			if ('1' in line):
				major.append('anisci')
			else:
				pass
		elif (linenum == 222):
			if ('1' in line):
				major.append('aem')
			else:
				pass
		elif (linenum == 223):
			if ('1' in line):
				major.append('atsci')
			else:
				pass
		elif (linenum == 224):
			if ('1' in line):
				major.append('bioeng')
			else:
				pass
		elif (linenum == 225):
			if ('1' in line):
				major.append('biosci')
			else:
				pass
		elif (linenum == 226):
			if ('1' in line):
				major.append('biosoc')
			else:
				pass
		elif (linenum == 227):
			if ('1' in line):
				major.append('btry')
			else:
				pass
		elif (linenum == 228):
			if ('1' in line):
				major.append('comm')
			else:
				pass
		elif (linenum == 229):
			if ('1' in line):
				major.append('devsoc')
			else:
				pass
		elif (linenum == 230):
			if ('1' in line):
				major.append('ent')
			else:
				pass
		elif (linenum == 231):
			if ('1' in line):
				major.append('enveng')
			else:
				pass
		elif (linenum == 232):
			if ('1' in line):
				major.append('envsci')
			else:
				pass
		elif (linenum == 233):
			if ('1' in line):
				major.append('foodsci')
			else:
				pass
		elif (linenum == 234):
			if ('1' in line):
				major.append('infosci')
			else:
				pass
		elif (linenum == 235):
			if ('1' in line):
				major.append('indstu')
			else:
				pass
		elif (linenum == 236):
			if ('1' in line):
				major.append('intag')
			else:
				pass
		elif (linenum == 237):
			if ('1' in line):
				major.append('landarch')
			else:
				pass
		elif (linenum == 238):
			if ('1' in line):
				major.append('nutsci')
			else:
				pass
		elif (linenum == 239):
			if ('1' in line):
				major.append('plantsci')
			else:
				pass
		elif (linenum == 240):
			if ('1' in line):
				major.append('sciear')
			else:
				pass
		elif (linenum == 241):
			if ('1' in line):
				major.append('viti')
			else:
				pass
		elif (linenum == 242):
			if ('1' in line):
				major.append('arch')
			else:
				pass
		elif (linenum == 243):
			if ('1' in line):
				major.append('fineart')
			else:
				pass
		elif (linenum == 244):
			if ('1' in line):
				major.append('urb')
			else:
				pass
		elif (linenum == 245):
			if ('1' in line):
				major.append('afistu')
			else:
				pass
		elif (linenum == 246):
			if ('1' in line):
				major.append('amstu')
			else:
				pass
		elif (linenum == 247):
			if ('1' in line):
				major.append('anthr')
			else:
				pass
		elif (linenum == 248):
			if ('1' in line):
				major.append('arch')
			else:
				pass
		elif (linenum == 249):
			if ('1' in line):
				major.append('asistu')
			else:
				pass
		elif (linenum == 250):
			if ('1' in line):
				major.append('astro')
			else:
				pass
		elif (linenum == 251):
			if ('1' in line):
				major.append('biosci')
			else:
				pass
		elif (linenum == 252):
			if ('1' in line):
				major.append('biosoc')
			else:
				pass
		elif (linenum == 253):
			if ('1' in line):
				major.append('chembio')
			else:
				pass
		elif (linenum == 254):
			if ('1' in line):
				major.append('china')
			else:
				pass
		elif (linenum == 255):
			if ('1' in line):
				major.append('class')
			else:
				pass
		elif (linenum == 256):
			if ('1' in line):
				major.append('complit')
			else:
				pass
		elif (linenum == 257):
			if ('1' in line):
				major.append('cs')
			else:
				pass
		elif (linenum == 258):
			if ('1' in line):
				major.append('econ')
			else:
				pass
		elif (linenum == 259):
			if ('1' in line):
				major.append('eng')
			else:
				pass
		elif (linenum == 260):
			if ('1' in line):
				major.append('fem')
			else:
				pass
		elif (linenum == 261):
			if ('1' in line):
				major.append('fren')
			else:
				pass
		elif (linenum == 262):
			if ('1' in line):
				major.append('gestu')
			else:
				pass
		elif (linenum == 263):
			if ('1' in line):
				major.append('gov')
			else:
				pass
		elif (linenum == 264):
			if ('1' in line):
				major.append('hist')
			else:
				pass
		elif (linenum == 265):
			if ('1' in line):
				major.append('histart')
			else:
				pass
		elif (linenum == 266):
			if ('1' in line):
				major.append('infosci')
			else:
				pass
		elif (linenum == 267):
			if ('1' in line):
				major.append('ital')
			else:
				pass
		elif (linenum == 268):
			if ('1' in line):
				major.append('ling')
			else:
				pass
		elif (linenum == 269):
			if ('1' in line):
				major.append('math')
			else:
				pass
		elif (linenum == 270):
			if ('1' in line):
				major.append('mus')
			else:
				pass
		elif (linenum == 271):
			if ('1' in line):
				major.append('eaststu')
			else:
				pass
		elif (linenum == 272):
			if ('1' in line):
				major.append('perf')
			else:
				pass
		elif (linenum == 273):
			if ('1' in line):
				major.append('phil')
			else:
				pass
		elif (linenum == 274):
			if ('1' in line):
				major.append('phys')
			else:
				pass
		elif (linenum == 275):
			if ('1' in line):
				major.append('psych')
			else:
				pass
		elif (linenum == 276):
			if ('1' in line):
				major.append('relstu')
			else:
				pass
		elif (linenum == 277):
			if ('1' in line):
				major.append('romstu')
			else:
				pass
		elif (linenum == 278):
			if ('1' in line):
				major.append('scitech')
			else:
				pass
		elif (linenum == 279):
			if ('1' in line):
				major.append('sciear')
			else:
				pass
		elif (linenum == 280):
			if ('1' in line):
				major.append('soc')
			else:
				pass
		elif (linenum == 281):
			if ('1' in line):
				major.append('stat')
			else:
				pass
		elif (linenum == 282):
			if ('1' in line):
				major.append('bioeng')
			else:
				pass
		elif (linenum == 283):
			if ('1' in line):
				major.append('chemeng')
			else:
				pass
		elif (linenum == 284):
			if ('1' in line):
				major.append('civeng')
			else:
				pass
		elif (linenum == 285):
			if ('1' in line):
				major.append('cs')
			else:
				pass
		elif (linenum == 286):
			if ('1' in line):
				major.append('ece')
			else:
				pass
		elif (linenum == 287):
			if ('1' in line):
				major.append('engphy')
			else:
				pass
		elif (linenum == 288):
			if ('1' in line):
				major.append('enveng')
			else:
				pass
		elif (linenum == 289):
			if ('1' in line):
				major.append('indmaj')
			else:
				pass
		elif (linenum == 290):
			if ('1' in line):
				major.append('inosci')
			else:
				pass
		elif (linenum == 291):
			if ('1' in line):
				major.append('matsci')
			else:
				pass
		elif (linenum == 292):
			if ('1' in line):
				major.append('mecheng')
			else:
				pass
		elif (linenum == 293):
			if ('1' in line):
				major.append('orie')
			else:
				pass
		elif (linenum == 294):
			if ('1' in line):
				major.append('sciear')
			else:
				pass
		elif (linenum == 295):
			if ('1' in line):
				major.append('biosoc')
			else:
				pass
		elif (linenum == 296):
			if ('1' in line):
				major.append('desenv')
			else:
				pass
		elif (linenum == 297):
			if ('1' in line):
				major.append('fash')
			else:
				pass
		elif (linenum == 298):
			if ('1' in line):
				major.append('fiber')
			else:
				pass
		elif (linenum == 299):
			if ('1' in line):
				major.append('globheal')
			else:
				pass
		elif (linenum == 300):
			if ('1' in line):
				major.append('humbio')
			else:
				pass
		elif (linenum == 301):
			if ('1' in line):
				major.append('humdev')
			else:
				pass
		elif (linenum == 302):
			if ('1' in line):
				major.append('nutsci')
			else:
				pass
		elif (linenum == 303):
			if ('1' in line):
				major.append('polana')
			else:
				pass
		elif (linenum == 304):
			if ('1' in line):
				ethnicity.append('white')
			elif ('2' in line):
				ethnicity.append('middleeastern')
			elif ('3' in line):
				ethnicity.append('black')
			elif ('4' in line):
				ethnicity.append('latino')
			elif ('5' in line):
				ethnicity.append('eastasian')
			elif ('6' in line):
				ethnicity.append('southasian')
			elif ('7' in line):
				ethnicity.append('pacificislander')
			elif ('8' in line):
				ethnicity.append('nativeamerican')
		elif (linenum == 305):
			if ('&nbsp;' in line):
				pass
			else:
				ethnicity.append(line)
		elif (linenum == 306):
			hometown.append(line)
		elif (linenum == 307):
			if ('1' in line):
				religion.append('christian')
			elif ('2' in line):
				religion.append('jewish')
			elif ('3' in line):
				religion.append('muslim')
			elif ('4' in line):
				religion.append('hindu')
			elif ('5' in line):
				religion.append('buddhist')
			elif ('6' in line):
				religion.append('atheist')
		elif (linenum == 308):
			if ('&nbsp;' in line):
				pass
			else:
				religion.append(line)
		elif (linenum == 309):
			if ('1' in line):
				career.append('broadcasting')
			else:
				pass
		elif (linenum == 310):
			if ('1' in line):
				career.append('journalism')
			else:
				pass
		elif (linenum == 311):
			if ('1' in line):
				career.append('publishing')
			else:
				pass
		elif (linenum == 312):
			if ('1' in line):
				career.append('architechture')
			else:
				pass
		elif (linenum == 313):
			if ('1' in line):
				career.append('culinaryart')
			else:
				pass
		elif (linenum == 314):
			if ('1' in line):
				career.append('fineart')
			else:
				pass
		elif (linenum == 315):
			if ('1' in line):
				career.append('photo')
			else:
				pass
		elif (linenum == 316):
			if ('1' in line):
				career.append('performingart')
			else:
				pass
		elif (linenum == 317):
			if ('1' in line):
				career.append('music')
			else:
				pass
		elif (linenum == 318):
			if ('1' in line):
				career.append('design')
			else:
				pass
		elif (linenum == 319):
			if ('1' in line):
				career.append('marketing')
			else:
				pass
		elif (linenum == 320):
			if ('1' in line):
				career.append('pubrel')
			else:
				pass
		elif (linenum == 321):
			if ('1' in line):
				career.append('finance')
			else:
				pass
		elif (linenum == 322):
			if ('1' in line):
				career.append('accounting')
			else:
				pass
		elif (linenum == 323):
			if ('1' in line):
				career.append('entre')
			else:
				pass
		elif (linenum == 324):
			if ('1' in line):
				career.append('managementcounsel')
			else:
				pass
		elif (linenum == 325):
			if ('1' in line):
				career.append('HR')
			else:
				pass
		elif (linenum == 326):
			if ('1' in line):
				career.append('realestate')
			else:
				pass
		elif (linenum == 327):
			if ('1' in line):
				career.append('hotel')
			else:
				pass
		elif (linenum == 328):
			if ('1' in line):
				career.append('fashion')
			else:
				pass
		elif (linenum == 329):
			if ('1' in line):
				career.append('stat/math')
			else:
				pass
		elif (linenum == 330):
			if ('1' in line):
				career.append('sports')
			else:
				pass
		elif (linenum == 331):
			if ('1' in line):
				career.append('teachingk12')
			else:
				pass
		elif (linenum == 332):
			if ('1' in line):
				career.append('uni')
			else:
				pass
		elif (linenum == 333):
			if ('1' in line):
				career.append('administration')
			else:
				pass
		elif (linenum == 334):
			if ('1' in line):
				career.append('research')
			else:
				pass
		elif (linenum == 335):
			if ('1' in line):
				career.append('coaching')
			else:
				pass
		elif (linenum == 336):
			if ('1' in line):
				career.append('meche')
			else:
				pass
		elif (linenum == 337):
			if ('1' in line):
				career.append('ece')
			else:
				pass
		elif (linenum == 338):
			if ('1' in line):
				career.append('cive')
			else:
				pass
		elif (linenum == 339):
			if ('1' in line):
				career.append('cheme')
			else:
				pass
		elif (linenum == 340):
			if ('1' in line):
				career.append('aeroe')
			else:
				pass
		elif (linenum == 341):
			if ('1' in line):
				career.append('manufac')
			else:
				pass
		elif (linenum == 342):
			if ('1' in line):
				career.append('infosci')
			else:
				pass
		elif (linenum == 343):
			if ('1' in line):
				career.append('cs')
			else:
				pass
		elif (linenum == 344):
			if ('1' in line):
				career.append('proddes')
			else:
				pass
		elif (linenum == 345):
			if ('1' in line):
				career.append('envsci')
			else:
				pass
		elif (linenum == 346):
			if ('1' in line):
				career.append('geo')
			else:
				pass
		elif (linenum == 347):
			if ('1' in line):
				career.append('energ')
			else:
				pass
		elif (linenum == 348):
			if ('1' in line):
				career.append('forest')
			else:
				pass
		elif (linenum == 349):
			if ('1' in line):
				career.append('parks')
			else:
				pass
		elif (linenum == 350):
			if ('1' in line):
				career.append('nurse')
			else:
				pass
		elif (linenum == 351):
			if ('1' in line):
				career.append('pharm')
			else:
				pass
		elif (linenum == 352):
			if ('1' in line):
				career.append('diet')
			else:
				pass
		elif (linenum == 353):
			if ('1' in line):
				career.append('doctor')
			else:
				pass
		elif (linenum == 354):
			if ('1' in line):
				career.append('labresearch')
			else:
				pass
		elif (linenum == 355):
			if ('1' in line):
				career.append('vet')
			else:
				pass
		elif (linenum == 356):
			if ('1' in line):
				career.append('pubheal')
			else:
				pass
		elif (linenum == 357):
			if ('1' in line):
				career.append('emecare')
			else:
				pass
		elif (linenum == 358):
			if ('1' in line):
				career.append('langtrans')
			else:
				pass
		elif (linenum == 359):
			if ('1' in line):
				career.append('forserv')
			else:
				pass
		elif (linenum == 360):
			if ('1' in line):
				career.append('internongov')
			else:
				pass
		elif (linenum == 361):
			if ('1' in line):
				career.append('intertrade')
			else:
				pass
		elif (linenum == 362):
			if ('1' in line):
				career.append('attorney')
			else:
				pass
		elif (linenum == 363):
			if ('1' in line):
				career.append('judge')
			else:
				pass
		elif (linenum == 364):
			if ('1' in line):
				career.append('pubserv')
			else:
				pass
		elif (linenum == 365):
			if ('1' in line):
				career.append('corporate')
			else:
				pass
		elif (linenum == 366):
			if ('1' in line):
				career.append('legal')
			else:
				pass
		elif (linenum == 367):
			if ('1' in line):
				career.append('socialwork')
			else:
				pass
		elif (linenum == 368):
			if ('1' in line):
				career.append('psych/couns')
			else:
				pass
		elif (linenum == 369):
			if ('1' in line):
				career.append('clergy')
			else:
				pass
		elif (linenum == 370):
			if ('1' in line):
				career.append('nonprofit')
			else:
				pass
		elif (linenum == 371):
			if ('1' in line):
				career.append('gov/pol')
			else:
				pass
		elif (linenum == 372):
			if ('1' in line):
				career.append('natsec')
			else:
				pass
		elif (linenum == 373):
			if ('1' in line):
				career.append('other')
			else:
				pass
		elif (linenum == 374):
			if ('1' in line):
				club.append('greek')
			else:
				pass
		elif (linenum == 375):
			if ('1' in line):
				club.append('polt')
			else:
				pass
		elif (linenum == 376):
			if ('1' in line):
				club.append('env')
			else:
				pass
		elif (linenum == 377):
			if ('1' in line):
				club.append('dance')
			else:
				pass
		elif (linenum == 378):
			if ('1' in line):
				club.append('commserv')
			else:
				pass
		elif (linenum == 379):
			if ('1' in line):
				club.append('minority')
			else:
				pass
		elif (linenum == 380):
			if ('1' in line):
				club.append('proffrat')
			else:
				pass
		elif (linenum == 381):
			if ('1' in line):
				club.append('career')
			else:
				pass
		elif (linenum == 382):
			if ('1' in line):
				club.append('athletic')
			else:
				pass
		elif (linenum == 383):
			if ('1' in line):
				club.append('cultural')
			else:
				pass
		elif (linenum == 384):
			if ('1' in line):
				club.append('socialchange')
			else:
				pass
		elif (linenum == 385):
			if ('1' in line):
				pass
			else:
				pass
		elif (linenum == 386):
			if ('&nbsp;' in line):
				pass
			else:
				club.append(line)
		elif (linenum == 387):
			if ('>1<' in line):
				sport.append('archery')
			elif ('>2<' in line):
				sport.append('badminton')
			elif ('>3<' in line):
				sport.append('baseball')
			elif ('>4<' in line):
				sport.append('basketball')
			elif ('>5<' in line):
				sport.append('bowling')
			elif ('>6<' in line):
				sport.append('climbing')
			elif ('>7<' in line):
				sport.append('cycling')
			elif ('>8<' in line):
				sport.append('dance')
			elif ('>9<' in line):
				sport.append('equestrian')
			elif ('10' in line):
				sport.append('fishing')
			elif ('11' in line):
				sport.append('football')
			elif ('12' in line):
				sport.append('golf')
			elif ('13' in line):
				sport.append('gymnastics')
			elif ('14' in line):
				sport.append('lacrosse')
			elif ('15' in line):
				sport.append('martialarts')
			elif ('16' in line):
				sport.append('wrestling')
			elif ('17' in line):
				sport.append('skating')
			elif ('18' in line):
				sport.append('skiing')
			elif ('19' in line):
				sport.append('soccer')
			elif ('20' in line):
				sport.append('swimming')
			elif ('21' in line):
				sport.append('tennis')
			elif ('22' in line):
				sport.append('track')
			elif ('23' in line):
				sport.append('none')
		elif (linenum == 388):
			if ('&nbsp;' in line):
				pass
			else:
				sport.append('line')
		elif (linenum == 389):
			if ('>1<' in line):
				music.append('alter')
			elif ('>2<' in line):
				music.append('apop')
			elif ('>3<' in line):
				music.append('classical')
			elif ('>4<' in line):
				music.append('country')
			elif ('>5<' in line):
				music.append('edm')
			elif ('>6<' in line):
				music.append('euro')
			elif ('>7<' in line):
				music.append('hiphop')
			elif ('>8<' in line):
				music.append('jazz')
			elif ('>9<' in line):
				music.append('latin')
			elif ('10' in line):
				music.append('opera')
			elif ('11' in line):
				music.append('pop')
			elif ('12' in line):
				music.append('r&b')
			elif ('13' in line):
				music.append('rock')
			elif ('14' in line):
				music.append('non')
			elif ('15' in line):
				pass
		elif (linenum == 390):
			if ('&nbsp;' in line):
				pass
			else:
				music.append('line')
		elif (linenum == 391):
			if ('1' in line):
				personality.append(1)
			elif ('2' in line):
				personality.append(2)
			elif ('3' in line):
				personality.append(3)
		elif (linenum == 392):
			if ('1' in line):
				personality.append(1)
			elif ('2' in line):
				personality.append(2)
			elif ('3' in line):
				personality.append(3)
		elif (linenum == 393):
			if ('1' in line):
				personality.append(1)
			elif ('2' in line):
				personality.append(2)
			elif ('3' in line):
				personality.append(3)
		elif (linenum == 394):
			if ('1' in line):
				personality.append(1)
			elif ('2' in line):
				personality.append(2)
			elif ('3' in line):
				personality.append(3)
		elif (linenum == 395):
			if ('1' in line):
				personality.append(1)
			elif ('2' in line):
				personality.append(2)
			elif ('3' in line):
				personality.append(3)
		elif (linenum == 396):
			preference.append(line)
		elif (linenum == 397):
			preference.append(line)
		elif (linenum == 398):
			preference.append(line)
		elif (linenum == 399):
			preference.append(line)
		elif (linenum == 400):
			preference.append(line)
		elif (linenum == 401):
			preference.append(line)
		elif (linenum == 402):
			preference.append(line)
		elif (linenum == 403):
			preference.append(line)
		elif (linenum == 404):
			preference.append(line)
		elif (linenum == 405):
			pass
		elif (linenum == 406):
			choice.append(line)
		elif (linenum == 407):
			choice.append(line)
		elif (linenum == 414):
			linenum -= 202

print major

