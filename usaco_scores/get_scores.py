#!/usr/bin/env python3

import collections

import bs4
import requests

from models import *

DEC15_PLATINUM = 'http://usaco.org/current/data/dec15_platinum_results.html'
JAN16_PLATINUM = 'http://usaco.org/current/data/jan16_platinum_results.html'
FEB16_PLATINUM = 'http://usaco.org/current/data/feb16_platinum_results.html'

DEC16_PLATINUM = 'http://usaco.org/current/data/dec16_platinum_results.html'
JAN17_PLATINUM = 'http://usaco.org/current/data/jan17_platinum_results.html'

def get_scores(url, score_attr_name):
    r = requests.get(url)
    assert r.status_code == 200

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    table = soup('table')[0]
    assert table.previous_sibling.string == 'Pre-College Participants (Full List):'

    with db.atomic():
        for tr in table('tr')[1:]:
            cells = [td.get_text(strip=True) for td in tr('td')]
            assert all(n is not None for n in cells), tr

            # normalize name
            name = ' '.join(cells[2].split())
            score = int(cells[3])

            competitor, created = Competitor.get_or_create(
                    country=cells[0],
                    gradyear=cells[1],
                    name=name)
            setattr(competitor, score_attr_name, score)
            competitor.save()


def main():
    get_scores(DEC15_PLATINUM, 'score_dec15')
    print('got december 2015')
    get_scores(JAN16_PLATINUM, 'score_jan16')
    print('got january 2016')
    get_scores(FEB16_PLATINUM, 'score_feb16')
    print('got february 2016')

    get_scores(DEC16_PLATINUM, 'score_dec16')
    print('got december 2016')
    get_scores(JAN17_PLATINUM, 'score_jan17')
    print('got january 2017')


if __name__ == '__main__':
    db.connect()
    main()
    db.close()

