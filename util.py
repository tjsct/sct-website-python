import collections, csv, datetime, io, glob
import requests

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1RH4JnXZZaV78hEnzDC_LRxR5wAsy7qhmTMJzpy8yoy8/pub?gid=0&single=true&output=csv"

def get_lectures_by_year():
    r = requests.get(SPREADSHEET_URL)
    r.encoding = "utf-8"
    f = io.StringIO(r.text)
    reader = csv.DictReader(f)

    # group lectures by year
    lectures_by_year = collections.defaultdict(list)
    for row in reader:
        year, date = row["year"], row["date"]
        if not year:
            continue

        # attempt to parse date
        if date:
            try:
                dt = datetime.datetime.strptime(date, "%Y-%m-%d")
                row["formatted_date"] = dt.strftime("%B %d, %Y")
            except:
                # standard lectures uses date as an ID
                row["formatted_date"] = date

        lectures_by_year[year].append(row)

    # reverse order of lectures
    for y in lectures_by_year:
        # make an exception for standard lectures
        if y != "Standard":
            lectures_by_year[y].reverse()

    # sort by year in reverse chronological order
    return collections.OrderedDict(
            sorted(lectures_by_year.items(), reverse=True))

def get_editorials_by_year():
    editorials = {}
    # sort by year in reverse chronological order
    # relies on the implicit insertion order of dictionaries in Python 3
    # should probably change to OrderedDict
    for fname in sorted(glob.glob("editorials/**/*.pdf", recursive=True), reverse=True):
        year, contest, file = fname.split("/")[1:]
        if year not in editorials:
            editorials[year] = []
        editorials[year].append((contest, file))

    # reverse order of editorials
    for y in editorials:
        editorials[y].reverse()

    return editorials

