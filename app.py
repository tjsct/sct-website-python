#!/usr/bin/env python3

import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/index.php', methods=['GET'])
def home2():
    return render_template('index.html')

@app.route('/competitions.php', methods=['GET'])
def competitions():
    return render_template('competitions.html')

@app.route('/lectures.php', methods=['GET'])
def lectures():
    return render_template('lectures.html')

@app.route('/schedule.php', methods=['GET'])
def schedule():
    return render_template('schedule.html')

@app.route('/links.php', methods=['GET'])
def links():
    return render_template('links.html')

@app.route('/styles.css', methods=['GET'])
def styles():
    return app.send_static_file('styles.css')


@app.route('/lectures/<path:path>')
def lecture_files(path):
    return send_from_directory('lectures', path)


@app.after_request
def after_request(response):
    response.headers['Server'] = 'nginx/1.8.1'
    return response


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000), host='0.0.0.0', debug=True)
