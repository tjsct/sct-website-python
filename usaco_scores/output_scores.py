#!/usr/bin/env python

from models import *

def main():
    query = Competitor.select(Competitor,
            SQL('score_dec15 + score_jan16 + score_feb16').alias('score_total_1516'),
            SQL('score_dec16 + score_jan17 + score_feb17').alias('score_total_1617'),
            SQL('score_dec15 + score_jan16 + score_feb16 + '
                'score_dec16 + score_jan17 + score_feb17').alias('score_total_all'))
    query = query.order_by(SQL('score_total_all').desc())
    for c in query:
        if c.country != 'USA':
            continue
        print('{:3} {:4} {:24} | {:4} {:4} {:4} >> {:4} | {:4} {:4} {:4} >> {:4} | {:4}'.format(
            c.country, c.gradyear, c.name,
            c.score_dec15, c.score_jan16, c.score_feb16, c.score_total_1516,
            c.score_dec16, c.score_jan17, c.score_feb17, c.score_total_1617,
            c.score_total_all
        ))

if __name__ == '__main__':
    main()

