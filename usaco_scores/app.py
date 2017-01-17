#!/usr/bin/env python3

from flask import Blueprint, render_template
from .models import *

page = Blueprint('usaco_scores', __name__)

@page.route('/')
def home():
    query = Competitor.select(Competitor,
        SQL('score_dec + score_jan + score_feb').alias('score_total'))
    query = query.order_by(SQL('score_total').desc())
    return render_template('scores.html', query=query)


@page.before_request
def _db_connect():
    db.connect()

@page.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

