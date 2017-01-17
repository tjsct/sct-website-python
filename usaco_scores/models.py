#!/usr/bin/env python3

import os

from peewee import *

dir_path = os.path.dirname(os.path.realpath(__file__))
db = SqliteDatabase(os.path.join(dir_path, 'scores.db'))

class Competitor(Model):
    name = CharField()
    country = CharField()
    gradyear = CharField()

    score_dec = IntegerField(default=0)
    score_jan = IntegerField(default=0)
    score_feb = IntegerField(default=0)

    class Meta:
        indexes = (
            # this tuple should be unique
            (('name', 'country', 'gradyear'), True),
        )
        database = db

if __name__ == '__main__':
    db.connect()
    db.drop_tables([Competitor], safe=True)
    db.create_tables([Competitor])

