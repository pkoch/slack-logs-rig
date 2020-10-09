# pkoch's experiments with Slack logs

Get your hands on a relevant Slack export. Let's say it's called `my-slack-dump`.

Run `filter_pkoch.py` so that I only see my own log lines.

```
(rm -rf target; mkdir -p target; cd target; unzip ../../my-slack-dump); ./filter_pkoch.py target/
```

Run `./count_lines.py target/` to check for the most active channel in each week.

For a pretty chart, run `./highcharts_count_lines.py target/ > www/set-variables.js` and `python -m http.server 8000 -d www`
