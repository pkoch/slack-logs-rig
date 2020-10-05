#!/usr/bin/env python3
from functools import reduce

from count_lines import count_stuff


def fill_in_blanks(dict_):
    channels = sorted({
        channel
        for week_info in stuff.values()
        for channel in week_info.keys()
    })

    for year in list(range(2016, 2021)):
        for week in range(1, 53):
            week_d = dict_.setdefault((year, week), {})
            for channel in channels:
                week_d.setdefault(channel, 0)

    return dict_


def filter_low_volume(stuff):
    def derp(acc, item):
        ((year, week), channel, count) = item
        acc.setdefault((year, week), {}).setdefault(channel, count)
        return acc

    stuff = reduce(
        derp,
        {
            ((year, week), channel, count)
            for (year, week), week_info in stuff.items()
            for channel, count in week_info.items()
            if (2016, 36) <= (year, week) <= (2018, 24)
        },
        {},
    )

    return stuff


def print_highcharts_stuff(stuff):
    stuff = fill_in_blanks(stuff)
    stuff = filter_low_volume(stuff)

    weeks = sorted(stuff.keys())
    print(
        "window.categories = ",
        [f"{year}-W{week:02}" for (year, week) in weeks],
        ";",
    )

    channels = sorted({
        channel
        for week_info in stuff.values()
        for channel in week_info.keys()
    })

    print(
        "window.series = ",
        [
            {
                'name': channel,
                'data': [stuff.get(week, {}).get(channel, 0) for week in weeks],
            }
            for channel in channels
        ],
        ";",
    )


if __name__ == '__main__':
    import sys
    stuff = count_stuff(sys.argv[1])
    print_highcharts_stuff(stuff)
