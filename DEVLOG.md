# Devlog – Women's Football Dashboard

## Session 1

**Goal:** Set up my workspace and load real football data into Python for the first time.

**What I did:** Created a project folder, set up a virtual environment,
installed the libraries I need, opened a Jupyter notebook, and loaded
StatsBomb's list of competitions, then filtered it to women's competitions only.

**What I learned:**

- Virtual environment: Where project tools are stored and accessed
- DataFrame: A snapshot table of data with rows and columns that can be worked with using code (i.e. code can be used to filter the data)

**What confused me:**
**How did statsbomb manage to pull such data?**
Mostly by people, trained analysts who log the data by hand.

**Why is jupyter notebook a seperate webpage and what it the purpose of this?**
It's a local file that can be accessed as a viewing screen on the browser; it's purpose is so you can run code in small pieces and see the result immediately with notes to help explore and experiment so once you know what you want, you can write the final piece as a normal Python code in a terminal like VS

**Next time:** Put the project on GitHub and load my first full match.

## Session 2

**Goal:** Load a full match from Euro 2025 and explore its event data.

**What I did:** Loaded all 31 matches from Women's Euro 2025, filtered them
to England's six games, loaded every event from the final against Spain
(4,830 events), explored the event types, and tested a theory about the goals.

**What I learned:**

- Why I chose Euro 2025: It's the most recent women's data StatsBomb has
  released for free. The WSL 2023/24 season has more matches per team,
  but Euro 2025 is newer and includes high-profile games like England's
  win in the final.
- value_counts(): It counts how many times each value appears in a column
  and sorts them from most to least common. It's a quick way to get a feel
  for a new dataset, like seeing which event types happen most in a match.
- & and |: When filtering, & means "and" (both conditions must be true)
  and | means "or" (either condition can be true). Each condition needs
  its own brackets.
- xG: Expected goals is an estimate of how likely a shot is to become a goal,
  from 0 to 1, based on things like where it was taken from. A penalty is
  around 0.78, while a long-range shot might be 0.02.
- Testing a theory: I thought the only real match goals were Caldentey's and
  Russo's, and the other goals in the data were shootout penalties. I checked
  by filtering shots to period 5 (the shootout), which showed England winning
  3–1, then filtering goals from before the shootout, which showed exactly
  two: Caldentey and Russo.

**What confused me:**

- Understanding xG.
  Resolved: xG is roughly how many times out of 100 a shot like that would
  go in. It measures the quality of chances, not just the result.
- The difference between & and | when filtering.
  Partly resolved: & narrows results (every condition must be true),
  | widens them (only one needs to be true). A quick way to remember it: & is picky, | is generous. Still getting comfortable with this, so I'll keep practising.

**Things I noticed in the data:**

- The score columns don't include penalty shootouts, so the final shows 1–1.
- Team names are inconsistent ("England Women's" vs "Wales W").
- StatsBomb minutes are elapsed time, so the 25th-minute goal shows as 24.

**Next time:** Plot every shot from the final on a football pitch using mplsoccer.

## Session 3

**Goal:** Create my first visualisation: a shot map of the Euro 2025 final.

**What I did:** Started a new notebook, filtered the final's shots (excluding
the penalty shootout), split each shot's location into x and y coordinates,
flipped Spain's shots to the opposite end, and built a styled shot map sized
by xG with goals shown as stars. Then compared both teams' xG with groupby
and tested who shot from inside the box.

**What I learned:**

- Coordinates: StatsBomb's pitch is 120 x 80, and every team attacks left
  to right. To show both teams, I flipped one by subtracting from 120 and 80,
  like rotating the pitch 180 degrees.
- mplsoccer: Pitch() draws the pitch, and pitch.scatter() places dots on it.
  fig is the whole canvas, ax is the area the pitch is drawn on.
- Styling: hex codes set colours, alpha makes dots see-through, zorder controls
  layering (like track order in an edit), and comments starting with #
  label sections of code.
- groupby: splits data into groups and calculates something for each one,
  like a pivot table in Excel.

**What confused me:**

- A NameError when drawing the chart.
  Resolved: the cells creating england_shots hadn't been run. NameError means
  something hasn't been created yet. Run All Cells runs everything in order.
- Why every shot appeared at the same goal on my first attempt.
  Resolved: StatsBomb records both teams attacking the same direction, so one
  team needs flipping.

**Things I noticed in the data:**

- Spain dominated volume: 23 shots and 2.14 xG, against England's 8 shots
  and 0.88 xG.
- But shot quality was similar: England's average xG per shot was slightly
  higher (0.11 vs 0.09), and both teams took about 75% of shots inside the box.
- So Spain's advantage came from volume, not better positions. My first
  impression from the chart was only half right, which shows why visuals
  should be checked against numbers.
- England matched their xG; Spain scored once from over two goals' worth
  of chances.
- Caveat: this is one match, so it's a small sample.

**Next time:** Add the shot map to my README, then decide the dashboard's
wider focus.
