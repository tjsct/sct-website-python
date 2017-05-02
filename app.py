#!/usr/bin/env python3

import os

from flask import Flask, request, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)

# set up usaco scores
import usaco_scores.app
app.register_blueprint(usaco_scores.app.page, url_prefix='/usaco_scores')

# retrieve lectures on startup
import util
lectures_by_year = util.get_lectures_by_year()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.php')
def about():
    return render_template('about.html')

@app.route('/lectures.php')
def lectures():
    return render_template('lectures.html',
            lectures_by_year=lectures_by_year)

@app.route('/schedule.php')
def schedule():
    return render_template('schedule.html')

@app.route('/links.php')
def links():
    return render_template('links.html')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')


# redirects
@app.route('/index.php')
def home2():
    return redirect(url_for('home'))

@app.route('/competitions.php')
def competitions():
    return redirect(url_for('about'))


# serve lecture files

@app.route('/lectures/<path:path>')
def lecture_files(path):
    return send_from_directory('lectures', path)


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000), host='0.0.0.0', debug=True)
