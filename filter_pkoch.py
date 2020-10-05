#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path
from glob import glob

def find(l, test):
    for i, e in enumerate(l):
        if test(e): return (i, e)
    return (None, None)

def get_pkochs_user_id(path):
    with open(path / 'users.json') as f:
        l = json.load(f)
    (i, e) = find(l, lambda e: e['name'])
    if i is None: raise Exception("Can't find pkoch on users.json")
    return e['id']


def filter_stuff_out(path):
    import pdb; pdb.set_trace()
    u = get_pkochs_user_id(path)
    for fn in glob(str(path / '*' / '*.json')):
        f = open(fn, 'r+')

        lines = [
            l
            for l in json.load(f)
            if l.get("user_id") == u
        ]

        if len(lines) > 0:
            f.seek(0)
            f.truncate()
            f.write(json.dump(lines, f))
            f.close()
        else:
            f.close()
            os.unlink(fn)

if __name__ == '__main__':
    filter_stuff_out(Path(sys.argv[1]))
