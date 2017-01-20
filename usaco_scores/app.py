#!/usr/bin/env python3

from flask import Blueprint, request, render_template
from .models import *

page = Blueprint('usaco_scores', __name__)

@page.route('/')
def home():
    international = request.args.get('international', type=bool)
    query = Competitor.select(Competitor,
            SQL('score_dec15 + score_jan16 + score_feb16').alias('score_total_1516'),
            SQL('score_dec16 + score_jan17 + score_feb17').alias('score_total_1617'),
            SQL('score_dec15 + score_jan16 + score_feb16 + '
                'score_dec16 + score_jan17 + score_feb17').alias('score_total_all'))
    if not international:
        query = query.where(Competitor.country == 'USA')
    query = query.order_by(SQL('score_total_all').desc())
    return render_template('scores.html', query=query)


@page.before_request
def _db_connect():
    db.connect()

@page.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

