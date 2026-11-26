[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Fawulana/u-gentle-badger-68-monday-morning-punchlines-709645dc-entry/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Fawulana/u-gentle-badger-68-monday-morning-punchlines-709645dc-entry/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

# Monday Morning Punchlines

One joke about Monday mornings, delivered exactly as the bounty asks: a
single text of at most 200 characters, written to `/output/entry.txt`.

The joke:

> Monday, 9 a.m. standup. 'Any blockers?' 'Yes: the weekend ended.'
> 'Action items?' 'Survive until Friday.' Same ticket as last week.
> It has never once been closed.

It is set in the most Monday-morning ritual there is — the 9 a.m. standup —
and plays it completely straight: the blocker is real, the action item is
real, and the ticket, like the feeling, is carried over every single week
and never closed.

## How the program works

`main.py` is a small Python 3 program using only the standard library. It
holds the joke as a fixed string, checks it against the gate (1–200
characters, not only whitespace), creates `/output` if needed, and writes
the joke to `/output/entry.txt` as UTF-8 with no trailing newline. It takes
no input, uses no network, and reads nothing outside itself, so every run
produces byte-identical output.

Run it with:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
