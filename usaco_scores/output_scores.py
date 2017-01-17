#!/usr/bin/env python

from models import *

def main():
    query = Competitor.select(Competitor,
        SQL('score_dec + score_jan + score_feb').alias('score_total'))
    query = query.order_by(SQL('score_total').desc())
    for c in query:
        if c.country != 'USA':
            continue
        print('{:3} {:4} {:20} | {:4} {:4} {:4} | {:4}'.format(
            c.country, c.gradyear, c.name,
            c.score_dec, c.score_jan, c.score_feb, c.score_total))

if __name__ == '__main__':
    main()

