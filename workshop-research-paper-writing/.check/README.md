# Layout verification tools

`overflow.js` — reports any slide whose content exceeds the 1280×720 frame.
`apply_class.py` — applies a Marp local class directive (e.g. `dense`, `xdense`) to specific slide numbers.

```bash
export CHROME_PATH=/usr/bin/google-chrome    # or /usr/bin/chromium
export CHROME_NO_SANDBOX=1                   # only when running as root / in a container

marp --no-stdin slides/day1.md -o .check/bare1.html --theme slides/theme.css --html --template bare
marp --no-stdin slides/day2.md -o .check/bare2.html --theme slides/theme.css --html --template bare
node .check/overflow.js .check/bare1.html .check/bare2.html

# fix any overflowing slide by increasing its density:
python3 .check/apply_class.py slides/day2.md dense 13 21 29
python3 .check/apply_class.py slides/day2.md xdense 12
```

Both decks currently report **no overflow**.
