#!/usr/bin/env python3

import os

from peewee import *

dir_path = os.path.dirname(os.path.realpath(__file__))
db = SqliteDatabase(os.path.join(dir_path, 'scores.db'))


class Competitor(Model):
    name = CharField()
    country = CharField()
    gradyear = CharField()

    # 2015-16 scores
    score_dec15 = IntegerField(default=0)
    score_jan16 = IntegerField(default=0)
    score_feb16 = IntegerField(default=0)

    # 2016-17 scores
    score_dec16 = IntegerField(default=0)
    score_jan17 = IntegerField(default=0)
    score_feb17 = IntegerField(default=0)

    # attendance for 2016-17
    attendance = IntegerField(default=0)

    class Meta:
        indexes = (
            # this tuple should be unique
            (('name', 'country', 'gradyear'), True),
        )
        database = db


def clear_tables():
    table_list = [Competitor]
    db.connect()
    db.drop_tables(table_list, safe=True)
    db.create_tables(table_list)

