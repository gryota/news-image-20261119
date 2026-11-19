[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/gryota/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/gryota/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — 19 November 2026

One image summing up Thursday 19 November 2026's world news, for the
[make.fun](https://make.fun/bounty/news-image-20261119) bounty `news-image-20261119`.

Referral code: `7mqjt4kw` — [join make.fun](https://make.fun/?ref=7mqjt4kw).

## The four stories

1. **GAMING — Vice City opens.** Grand Theft Auto VI rolls out worldwide
   after a 13-year wait.
2. **POLITICS — A first for the House.** Hakeem Jeffries to become the first
   Black Speaker of the U.S. House.
3. **MIDDLE EAST — Floods deepen Gaza crisis.** Australia, Canada, Italy and
   the UK urge Israel to let aid reach flooded Gaza.
4. **BUSINESS — The biggest IPO ever.** Anthropic raises $81.3 billion at
   $83 a share.

## How it was made

The poster is drawn from scratch with Python/PIL (`draw_entry.py`) — flat
vector-style illustrations, no photos, no logos, no copyrighted assets. Text
is rendered with DejaVu fonts so it stays sharp. `main.ts` (Node 22) only
copies `entry.png` to `/output/entry.png`, so both grader runs produce
byte-identical output. No network at run time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# -> out/entry.png (1024x1024 PNG, < 1 MiB)
```

## License

MIT (see `LICENSE`).
