#!/usr/bin/env python3
import os, collections, json
from flask import Flask, request, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)

# globals
FILE = ".html.j2" # file extention
CONFIG = json.load(open("files/config.json")) # config

@app.context_processor
def globals() -> dict:
    """ Returns all the global variables passed to every template. """
    return CONFIG

# set up usaco scores
import usaco_scores.app
app.register_blueprint(usaco_scores.app.page, url_prefix="/usaco_scores")

# retrieve lectures on startup
import util
lectures_by_year = util.get_lectures_by_year()

@app.route("/")
def home():
    return render_template(f"index{FILE}")

@app.route("/about")
def about():
    return render_template(f"about{FILE}")

@app.route("/schedule")
def schedule():
    return render_template(f"schedule{FILE}")

@app.route("/links")
def links():
    return render_template(f"links{FILE}")

@app.route("/1920lectures")
def lectures_6():
    return render_template(f"lectures{FILE}",lectures_by_year = {"2019-20":lectures_by_year["2019-20"]})

@app.route("/1819lectures")
def lectures_1():
    return render_template(f"lectures{FILE}",lectures_by_year = {"2018-19":lectures_by_year["2018-19"]})

@app.route("/1718lectures")
def lectures_2():
    return render_template(f"lectures{FILE}",lectures_by_year = {"2017-18":lectures_by_year["2017-18"]})

@app.route("/1617lectures")
def lectures_3():
    return render_template(f"lectures{FILE}",lectures_by_year = {"2016-17":lectures_by_year["2016-17"]})

@app.route("/1516lectures")
def lectures_4():
    return render_template(f"lectures{FILE}",lectures_by_year = {"2015-16":lectures_by_year["2015-16"]})

@app.route("/1920history")
def history1920():
	return render_template(f"1920history{FILE}")

@app.route("/otherlectures")
def lectures_5():
    used_keys = ["2019-20","2018-19", "2017-18", "2016-17","2015-16"]
    temp_dict = {}
    for k in lectures_by_year:
        if k not in used_keys:
            temp_dict[k] = lectures_by_year[k]
    return render_template(f"lectures{FILE}",
            lectures_by_year=collections.OrderedDict(sorted(temp_dict.items(), reverse=True)))

# redirects
@app.route("/index")
def home2():
    return redirect(url_for("home"))

@app.route("/competitions")
def competitions():
    return redirect(url_for("about"))

# serve lecture files
@app.route("/lectures/<path:path>")
def lecture_files(path):
    return send_from_directory("lectures", path)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", 5000), host="0.0.0.0", debug=True)

