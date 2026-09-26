# England's Euro 2025 Journey ⚽

An interactive dashboard analysing how England won Women's Euro 2025, and what the data suggests about their chances of a third straight title at Euro 2029, using professional match event data from StatsBomb.

**🔗 [Open the live dashboard](https://lionesses-euro2025.streamlit.app/)**

> ✅ **Status: Live.** Explore the [interactive dashboard](https://lionesses-euro2025.streamlit.app/), or follow the full build, session by session, in the [devlog](DEVLOG.md).

![England's Euro 2025 journey: xG and goals match by match](england_journey_xg.png)

---

## About the project

Men's football is one of the most heavily analysed sports in the world, but the women's game receives a fraction of that attention, despite rapidly growing audiences, investment and professionalism. This project uses free, professional-grade event data, where every pass, shot and tackle is recorded with its location on the pitch, to tell the story of England's Euro 2025 win and look ahead to the next tournament.

### Why I built this

I moved into data from a background in media production. This project brings the two together: the analytical side of working with real, messy data, and the storytelling and visual design skills from my creative work. Every chart follows the same visual identity, and the dashboard is structured like a story, from the tournament itself to the players behind it, and then to the future.

### Guiding questions

1. How did England's attacking threat change match by match?
2. Did England deserve their results?
3. Who drove England's attack?
4. How did England defend?
5. Looking ahead: what does the data suggest about England's chances of a third consecutive title at Euro 2029 in Germany?

---

## Key findings

### 1. England grew into the tournament, then survived

England were out-created in their opening 2–1 defeat to France, dominated the Netherlands and Wales, were level on chances with Sweden, and were clearly stronger than Italy. In the final, Spain created more than twice England's xG (2.14 vs 0.88), but England held on and won on penalties.

### 2. Volume vs quality in the final

![Shot map of the Euro 2025 final](shot_map_euro2025_final.png)

Spain took nearly three times as many shots as England in the final (23 vs 8). But shot for shot, England's chances were just as good, with a slightly higher average xG per shot, and both teams took around 75% of their shots from inside the box. Spain's advantage came from volume, not quality.

### 3. Russo was a complete forward, and penalties distorted the raw numbers

![Shooters vs creators: England at Euro 2025](england_shooters_vs_creators.png)

Alessia Russo led England in both shooting threat and assists, with Ella Toone and Lauren Hemp completing an attacking core dangerous in both roles. Removing penalties (non-penalty xG) changed the picture: Chloe Kelly's saved penalty against Italy had made her look wasteful, when her real strength was creating chances. Lauren Hemp created the most xG for teammates but finished with no assists.

### 4. Spain are rising, and England's defence is a concern

![Road to Euro 2029: xG difference per match across four tournaments](road_to_2029_trend.png)

Across the last four major tournaments, Spain have become the most dominant team in the data, while Germany, the Euro 2029 hosts, dropped sharply at Euro 2025. England win tournaments through clinical finishing rather than dominance, and have allowed more chances at every tournament since 2019.

### 5. England's attack is heading towards 30

![England's attack by age at Euro 2029](england_age_2029.png)

9 of England's 17 attacking contributors will be 30 or older by Euro 2029, accounting for 49.8% of their attacking involvement at Euro 2025. A third straight title may depend on younger players like Lauren James, Aggie Beever-Jones and Michelle Agyemang stepping up.

---

## The dashboard

The [live dashboard](https://lionesses-euro2025.streamlit.app/) has four sections:

- **Tournament overview:** England's chances created and goals scored across all six matches.
- **Match explorer:** pick any of England's matches to see its key stats and an interactive shot map.
- **Player view:** who drove England's attack, with a sortable table of every player's stats.
- **Looking ahead to 2029:** how England compare with Spain and Germany over time, and how the squad is ageing.

---

## Data and methods

**Match data:** [StatsBomb Open Data](https://github.com/statsbomb/open-data), covering Women's Euro 2025, Euro 2022 and the 2019 and 2023 Women's World Cups.

**Player birthdates:** the Wikipedia "UEFA Women's Euro 2025 squads" page, which cites the FA's official squad announcement.

**Key measures:**

- **xG (expected goals):** the probability a shot becomes a goal, from 0 to 1, based on thousands of historical shots. It measures the quality of chances, not just the result.
- **npxG (non-penalty xG):** xG with penalties removed, for a fairer comparison of open-play threat.
- **xG assisted:** the total xG of shots a player set up with the pass right before them.
- **xG difference:** xG created minus xG allowed per match, a measure of how dominant a team was.

**Choices and assumptions:**

- Penalty shootouts are excluded from all analysis, as they don't reflect open play.
- Euro 2029 dates aren't confirmed, so player ages use 1 July 2029.
- "30 or older" is a simple threshold for the age analysis, not a scientific cut-off.

### Limitations

This analysis describes what happened; it doesn't predict the future. Four tournaments is a short trend, World Cups and Euros involve different opponents, and some samples are small (Germany played only three matches at the 2023 World Cup). Individual finishing numbers come from few shots and would likely settle over a longer period. The age finding is sensitive to the threshold: Ella Toone will be 29.8, just under the line.

---

## Tools and technologies

| Tool                 | What it's used for                              |
| -------------------- | ----------------------------------------------- |
| **Python**           | The programming language for the whole project  |
| **pandas**           | Loading, cleaning, joining and analysing data   |
| **statsbombpy**      | Downloading StatsBomb data directly into Python |
| **mplsoccer**        | Drawing football pitches for shot maps          |
| **matplotlib**       | Creating charts and visualisations              |
| **Jupyter Notebook** | Exploring the data step by step                 |
| **Streamlit**        | Building and hosting the interactive dashboard  |
| **Git and GitHub**   | Version control and sharing                     |

---

## Project structure

```
womens-football-dashboard/
├── app.py                              # The Streamlit dashboard
├── 01_exploration.ipynb                # Exploring the StatsBomb data
├── 02_shot_map.ipynb                   # Shot map and xG analysis of the final
├── 03_england_journey.ipynb            # England's six matches and player analysis
├── 04_looking_ahead.ipynb              # Trends and squad ages for Euro 2029
├── data/
│   ├── shots_2019_2025.csv             # Shots from four tournaments
│   ├── england_ages.csv                # Player birthdates
│   └── england_players_euro2025.csv    # England player stats
├── shot_map_euro2025_final.png         # Shot map of the final
├── england_journey_xg.png              # Tournament overview chart
├── england_players_npxg.png            # Top 10 by non-penalty xG
├── england_shooters_vs_creators.png    # Shooters vs creators chart
├── road_to_2029_trend.png              # Rivals trend chart
├── england_age_2029.png                # Squad age chart
├── DEVLOG.md                           # Session-by-session development log
├── requirements.txt                    # Python libraries needed
├── .gitignore                          # Files excluded from the repository
└── README.md                           # You are here
```

---

## How to run it yourself

1. Clone the repository:

   ```
   git clone https://github.com/georgiajayy/womens-football-dashboard.git
   cd womens-football-dashboard
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Mac / Linux
   source .venv/bin/activate
   ```

3. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

4. Run the dashboard:

   ```
   streamlit run app.py
   ```

5. To open the notebooks, install Jupyter too:
   ```
   pip install jupyter
   jupyter notebook
   ```

---

## What I learned

This was my first full data project after moving into tech from media production. Along the way I learned to work with messy real-world data, test theories against numbers rather than first impressions, combine data from different sources, and turn analysis into a live product. Some of the most valuable moments came from the data correcting me, like discovering that Spain's dominance in the final came from volume rather than quality. The full story, including everything that confused me and how I solved it, is in the [devlog](DEVLOG.md).

---

## Roadmap

- [x] Set up the project environment and GitHub repository
- [x] Explore a full match and understand the event data
- [x] Choose the project's focus (England's Euro 2025 journey)
- [x] Build the tournament overview, shot map and player analysis
- [x] Build the interactive Streamlit dashboard
- [x] Look ahead to Euro 2029 (trends and squad ages)
- [x] Publish the dashboard online
- [ ] Record a demo video walkthrough
- [ ] Future: use WSL data to find young English players performing well at club level, like a scouting tool
- [ ] Future: build my own expected goals (xG) model

---

## Acknowledgements

- [StatsBomb](https://statsbomb.com/) for making their event data freely available
- [mplsoccer](https://mplsoccer.readthedocs.io/) for the football pitch plotting library

---

**Georgia J Summers** · Junior Data Analyst · [GitHub](https://github.com/georgiajayy) · [LinkedIn](https://www.linkedin.com/in/georgiajayysummers/)
