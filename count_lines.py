#!/usr/bin/env python3
import json
from datetime import date
from pathlib import Path


IGNORED_CHANNELS = (
    '112',
    'random-omnishambles',
    'general',
    'golds',
    'math',
    'good-reads',
    'life-on-mars-lda',
    'infra-talk',
    'community',
    'office',
    'tempos-bot',
    'happy-and-frustrated',
    'culture',
    'summer-internships',
    'programação',
    'blockchain',
)


def print_stuff(stuff):
    for (year, week), e0 in sorted(stuff.items()):
        print(f"{year}-W{week:02}")
        for channel, count in sorted(
            e0.items(),
            key=lambda e: e[1],
            reverse=True,
        )[:5]:
            if channel in IGNORED_CHANNELS:
                continue
            if count == 0:
                continue
            # 29 was counted manually, 4 seemed good enough for msg counts
            print(f"  {channel:>29}: {count:4}")


def count_stuff(path):
    path = Path(path)
    result = {}

    for fn in path.glob('*/*.json'):
        year, week, _day = date.fromisoformat(fn.stem).isocalendar()
        channel = fn.parent.name
        msg_count = len(json.load(open(fn)))

        result[(year, week)][channel] = (
            result.
            setdefault((year, week), {}).
            setdefault(channel, 0)
        ) + msg_count

    return result


if __name__ == '__main__':
    import sys
    stuff = count_stuff(sys.argv[1])
    print_stuff(stuff)
