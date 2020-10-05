#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path
from glob import glob


def find(list_, test):
    for i, e in enumerate(list_):
        if test(e):
            return (i, e)
    return (None, None)


def get_pkochs_user_id(path):
    with open(path / 'users.json') as f:
        list_ = json.load(f)
    (i, e) = find(list_, lambda e: e['name'] == 'pkoch')
    if i is None:
        raise Exception("Can't find pkoch on users.json")
    return e['id']


def filter_stuff_out(path):
    u = get_pkochs_user_id(path)
    for fn in glob(str(path / '*' / '*.json')):
        f = open(fn, 'r+')

        lines = [
            line
            for line in json.load(f)
            if line.get("user") == u
        ]

        if len(lines) > 0:
            f.seek(0)
            f.truncate()
            json.dump(lines, f, sort_keys=True, indent=2)
            f.close()
        else:
            f.close()
            os.unlink(fn)


if __name__ == '__main__':
    filter_stuff_out(Path(sys.argv[1]))
