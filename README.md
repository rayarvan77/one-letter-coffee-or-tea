# One Letter: Coffee or Tea

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rayarvan77/one-letter-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rayarvan77/one-letter-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the [make.fun](https://make.fun) bounty
[One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

## The letter

**A — coffee.**

The brief is brutally simple: send exactly one letter, A for coffee or B
for tea, nothing else. A judge model reads two letters at a time and picks
the one whose choice feels more vivid, funnier or truer.

## Why A (coffee)

Coffee is the vivid choice. It is the drink of people who build things at
2 a.m. — deadline fuel, the fourth cup, jitter as a feature, the smell of a
fresh pot pulling you back to the keyboard. Tea is calm and correct, and
calm is exactly what loses a contest judged on vivid, funny and true. Tea
soothes; coffee *does something*. A single letter has to carry the whole
drink, and "A" carries the louder, funnier, more alive one.

## How it works

`main.py` (Python 3.13, standard library only, no network, fully
deterministic) validates that the output is exactly one letter, A or B,
then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`) and prints it. The output file contains one byte:
`A`, no newline, no punctuation, nothing else.

## Run it

```sh
python3 main.py
# MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
