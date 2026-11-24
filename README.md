# The Funniest Out-of-Office

One line of an out-of-office auto-reply, written to be the funniest a single line can be — for the [make.fun](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) competition "The Funniest Out-of-Office".

[![make.fun competition](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Araara7/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Araara7/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

## The entry

> I'm out of office until Monday. If it's urgent, email someone else — I already did.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt`. It is deterministic — the same 83-character line on every run — and self-checks the gate: exactly one line, 1–140 UTF-8 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
