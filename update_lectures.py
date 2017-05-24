import os.path
import requests
import sys
import time
import util

DRIVE_URL = "https://drive.google.com/uc?export=download&id={file_id}"
PATH = "lectures/{year_name}/{file_name}"


lectures = util.get_lectures_by_year()
for year in lectures:
	for lecture in lectures[year]:
		if "link" not in lecture or len(lecture["link"]) == 0:
			continue
		file_name = lecture["link"][lecture["link"].rfind("/")+1:]
		x, y = lecture["year"].split("-")[-2:]
		year_name = x[-2:]+y[-2:]
		
		os.makedirs(PATH.format(year_name=year_name, file_name=''), exist_ok=True)
		my_path = PATH.format(year_name=year_name, file_name=file_name)
		
		if not os.path.isfile(my_path):
			time.sleep(2)
			print("Downloading {} ".format(file_name), end='')
			sys.stdout.flush()
			r = requests.get(DRIVE_URL.format(file_id=lecture["google_drive_id"]))
			with open(my_path, "wb") as f:
				f.write(r.content)
			print("-- OK")

