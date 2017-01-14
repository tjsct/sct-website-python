#!/usr/bin/env python3

import collections
import csv
import datetime
import io
import requests

SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1RH4JnXZZaV78hEnzDC_LRxR5wAsy7qhmTMJzpy8yoy8/pub?gid=0&single=true&output=csv'

def get_lectures_by_year():
    r = requests.get(SPREADSHEET_URL)
    f = io.StringIO(r.text)
    reader = csv.DictReader(f)

    # group lectures by year
    lectures_by_year = collections.defaultdict(list)
    for row in reader:
        year, date = row['year'], row['date']
        if not year:
            continue

        # attempt to parse date
        if date:
            try:
                dt = datetime.datetime.strptime(date, '%Y-%m-%d')
                row['formatted_date'] = dt.strftime('%B %d, %Y')
            except:
                pass

        lectures_by_year[year].append(row)

    # reverse order of lectures
    for y in lectures_by_year:
        lectures_by_year[y].reverse()

    # sort by year in reverse chronological order
    return collections.OrderedDict(
            sorted(lectures_by_year.items(), reverse=True))

