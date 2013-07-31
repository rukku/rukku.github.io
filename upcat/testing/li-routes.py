import operator
destinations = [ 
			"as",
			"bio",
			"cal",
			"cba-se",
			"che", 
			"cmc-cm",
			"engg",
			"mh-lc",
			"nigs",
			"scicomplex"

		  ]
origins = {
			"commonwealth":"Commonwealth Avenue",
			"katips" : "Katipunan Avenue",
			"philcoa": "Philcoa",
			"qave":"Quezon Avenue",
			"smn": "North Avenue"
		   }


lines = '''<li><a href="%s-%s.html">%s</a></li>'''

            
outfile = open('elements.txt', 'wt')

sorted_x = sorted(origins.iteritems(), key=operator.itemgetter(1))

for destination in destinations:
	for k,v in sorted_x:
		outfile.write(lines % ( k, destination, v) + "\n")

outfile.close()







