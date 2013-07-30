import re


gj = open ("spots.geojson")
spotslist = open("spots.txt", 'wt')

for line in gj.readlines():
	if re.search('id', line):
		print line
		spotslist.write(line)
