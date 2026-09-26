# Women's Football Dashboard ⚽

An interactive dashboard exploring women's football using professional match event data from StatsBomb.

> 🚧 **Status: In progress.** This project is being built step by step, and documented as I go. Follow along in the [devlog](DEVLOG.md).

![Shot map of the Euro 2025 final between England and Spain](shot_map_euro2025_final.png)

**Latest finding:** In the Euro 2025 final, Spain took nearly three times
as many shots as England (23 vs 8) and generated 2.14 xG to England's 0.88.
But shot for shot, England's chances were just as good, with a slightly
higher average xG per shot. Spain's advantage came from volume, not quality.

![England's Euro 2025 journey: xG and goals match by match](england_journey_xg.png)

**England's journey:** England were out-created in their opening defeat
to France, dominated the Netherlands and Wales, were level on chances
with Sweden, and were clearly stronger than Italy. In the final, Spain
created more than twice England's xG, but England held on and won on penalties.

---

## About the project

Men's football is one of the most heavily analysed sports in the world, but the women's game receives a fraction of that attention, despite rapidly growing audiences, investment and professionalism. This project aims to help close that gap by turning detailed match data into clear, interactive visuals that anyone can explore.

The dashboard will cover competitions including the FA Women's Super League, the UEFA Women's Euros and the FIFA Women's World Cup, using event data where every pass, shot, tackle and carry is recorded with its location on the pitch.

### Guiding questions

1. How did England's attacking threat change match by match?
2. Did England deserve their results?
3. Who drove England's attack?
4. How did England defend?
5. Looking ahead: what does the data suggest about England's chances
   of a third consecutive title at Euro 2029 in Germany?

### Why I'm building this

I moved into data from a background in media production. This project brings together the two: the analytical side of working with real, messy data, and the storytelling and visual design skills from my creative work. The goal is a dashboard that isn't just accurate, but genuinely engaging to use.

---

## Data

This project uses **StatsBomb Open Data**, a free collection of professional football event data. Each match contains roughly 3,000 to 4,000 individual events, tagged by analysts watching match footage.

Women's competitions available include:

- FA Women's Super League (2018/19 to 2023/24)
- UEFA Women's Euro (2022, 2025)
- FIFA Women's World Cup (2019, 2023)
- Frauen Bundesliga, Liga F, Serie A Women and the NWSL

Data provided by [StatsBomb](https://github.com/statsbomb/open-data).

---

## Tools and technologies

| Tool                 | What it's used for                                             |
| -------------------- | -------------------------------------------------------------- |
| **Python**           | The programming language for the whole project                 |
| **pandas**           | Loading, cleaning and analysing tables of data                 |
| **statsbombpy**      | Downloading StatsBomb data directly into Python                |
| **mplsoccer**        | Drawing football pitches for shot maps, pass maps and heatmaps |
| **matplotlib**       | Creating charts and visualisations                             |
| **Jupyter Notebook** | Exploring the data step by step                                |
| **Streamlit**        | Building the interactive web dashboard                         |

---

## Project roadmap

- [x] Set up the project environment and GitHub repository
- [x] Load StatsBomb data and filter to women's competitions
- [x] Explore a full match and understand the event data
- [x] Choose the project's focus (England's Euro 2025 journey)
- [x] Build tournament overview chart (xG and goals, match by match)
- [x] Build first visualisation (shot map of the Euro 2025 final)
- [ ] Build further visualisations (passing networks, player comparisons)
- [ ] Assemble the interactive Streamlit dashboard
- [ ] Publish the dashboard online
- [ ] Stretch goal: build a simple expected goals (xG) model
- [ ] Record a short demo video walkthrough

---

## Project structure

```
womens-football-dashboard/
├── 01_exploration.ipynb           # Exploring the StatsBomb data
├── 02_shot_map.ipynb              # Shot map and xG analysis of the final
├── 03_england_journey.ipynb       # England's six matches: xG and goals
├── england_journey_xg.png         # Tournament overview chart
├── shot_map_euro2025_final.png    # Saved shot map image
├── DEVLOG.md                      # Session-by-session development log
├── requirements.txt               # Python libraries needed to run the project
├── .gitignore                     # Files excluded from the repository
└── README.md                      # You are here

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

4. Open the notebook:
   ```
   jupyter notebook
   ```

---

## Devlog

I'm documenting each session of this project, including what I built, what I learned and what confused me along the way. Read it in [DEVLOG.md](DEVLOG.md).

---

## Acknowledgements

- [StatsBomb](https://statsbomb.com/) for making their event data freely available
- [mplsoccer](https://mplsoccer.readthedocs.io/) for the football pitch plotting library

---

**Georgia** · [GitHub](https://github.com/georgiajayy)
