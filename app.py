#!/usr/bin/env python3

import os
import collections


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


@app.route('/schedule.php')
def schedule():
    return render_template('schedule.html')

@app.route('/links.php')
def links():
    return render_template('links.html')

#@app.route('/styles.css')
#def styles():
#    return app.send_static_file('styles.css')
    
@app.route('/1920lectures.php')
def lectures_6():
    return render_template('lectures.html',lectures_by_year = {"2019-20":lectures_by_year["2019-20"]})
    
@app.route('/1819lectures.php')
def lectures_1():
    return render_template('lectures.html',lectures_by_year = {"2018-19":lectures_by_year["2018-19"]})
    
@app.route('/1718lectures.php')
def lectures_2():
    return render_template('lectures.html',lectures_by_year = {"2017-18":lectures_by_year["2017-18"]})
    
@app.route('/1617lectures.php')
def lectures_3():
    return render_template('lectures.html',lectures_by_year = {"2016-17":lectures_by_year["2016-17"]})
    
@app.route('/1516lectures.php')
def lectures_4():
    return render_template('lectures.html',lectures_by_year = {"2015-16":lectures_by_year["2015-16"]})
    
@app.route('/1920history.php')
def history1920():
	return render_template('1920history.html')
    
@app.route('/otherlectures.php')
def lectures_5():
    used_keys = ["2019-20","2018-19", "2017-18", "2016-17","2015-16"]
    temp_dict = {}
    for k in lectures_by_year:
        if k not in used_keys:
            temp_dict[k] = lectures_by_year[k]
    return render_template('lectures.html',
            lectures_by_year=collections.OrderedDict(sorted(temp_dict.items(), reverse=True)))
    


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
