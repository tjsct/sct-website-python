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

# pages

def make_page(url: str, file_name: str, **kwargs: dict) -> None:
    """ Makes a simple page. """
    f = lambda: render_template(f"{file_name}{FILE}", **kwargs)
    # Need distinct function names for Flask not to error
    f.__name__ = url if url != "" else "index"
    app.route(f"/{url}")(f)

def make_lectures_pages(start: int, end: int) -> None:
    """ Makes a different handler for each year. """
    for y in range(start, end + 1):
        years = f"20{y}-{y + 1}"
        make_page(f"{y}{y + 1}lectures", "lectures", lectures_by_year={years: lectures_by_year[years]})

pages = [("", "index"), ("about", "about"), ("schedule", "schedule"),
         ("links", "links"), ("1920history", "1920history")
        ]
for url, fname in pages:
    make_page(url, fname)

make_lectures_pages(15, 19)

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
    return redirect("https://activities.tjhsst.edu/sct/")

@app.route("/competitions")
def competitions():
    return redirect(url_for("about"))

# serve lecture files
@app.route("/lectures/<path:path>")
def lecture_files(path):
    return send_from_directory("lectures", path)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", 5000), host="0.0.0.0", debug=True)

