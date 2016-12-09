def get_lectures():
	import csv, datetime, requests

	l = []
	labels = []
	url = "https://docs.google.com/spreadsheets/d/1RH4JnXZZaV78hEnzDC_LRxR5wAsy7qhmTMJzpy8yoy8/pub?gid=0&single=true&output=csv"
	f = requests.get(url).content.decode("utf-8")

	reader = csv.reader(f.splitlines(), delimiter=',', quotechar='"')
	first = True
	for row in reader:
		if first:
			labels = row
			first = False
			continue
		if len("".join(row)) == 0:
			continue
		l.append(row)

	years = {}
	for r in l:
		if r[0] not in years:
			years[r[0]] = []
		row = {}
		for i in range(len(r)):
			row[labels[i]] = r[i]
		try:
			row['Date'] = \
				datetime.datetime.strptime(row['Date'], "%Y/%m/%d") \
					.strftime("%B %d, %Y")
		except:
			pass
		years[r[0]].append(row)
	for year in years:
		years[year].reverse()
	return years
