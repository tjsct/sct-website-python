#!/usr/bin/env python3

import collections

import bs4
import requests

from models import *

DEC15_PLATINUM = 'http://usaco.org/current/data/dec15_platinum_results.html'
JAN16_PLATINUM = 'http://usaco.org/current/data/jan16_platinum_results.html'
FEB16_PLATINUM = 'http://usaco.org/current/data/feb16_platinum_results.html'

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

            competitor, created = Competitor.get_or_create(
                country=cells[0],
                gradyear=cells[1],
                name=cells[2],
            )
            setattr(competitor, score_attr_name, int(cells[3]))
            competitor.save()


def main():
    get_scores(DEC15_PLATINUM, 'score_dec')
    get_scores(JAN16_PLATINUM, 'score_jan')
    get_scores(FEB16_PLATINUM, 'score_feb')


if __name__ == '__main__':
    db.connect()
    main()
    db.close()

