# Women's Football Dashboard ⚽

An interactive dashboard exploring women's football using professional match event data from StatsBomb.

> 🚧 **Status: In progress.** This project is being built step by step, and documented as I go. Follow along in the [devlog](DEVLOG.md).

---

## About the project

Men's football is one of the most heavily analysed sports in the world, but the women's game receives a fraction of that attention, despite rapidly growing audiences, investment and professionalism. This project aims to help close that gap by turning detailed match data into clear, interactive visuals that anyone can explore.

The dashboard will cover competitions including the FA Women's Super League, the UEFA Women's Euros and the FIFA Women's World Cup, using event data where every pass, shot, tackle and carry is recorded with its location on the pitch.

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

| Tool | What it's used for |
|---|---|
| **Python** | The programming language for the whole project |
| **pandas** | Loading, cleaning and analysing tables of data |
| **statsbombpy** | Downloading StatsBomb data directly into Python |
| **mplsoccer** | Drawing football pitches for shot maps, pass maps and heatmaps |
| **matplotlib** | Creating charts and visualisations |
| **Jupyter Notebook** | Exploring the data step by step |
| **Streamlit** | Building the interactive web dashboard |

---

## Project roadmap

- [x] Set up the project environment and GitHub repository
- [x] Load StatsBomb data and filter to women's competitions
- [ ] Explore a full match and understand the event data
- [ ] Choose the project's focus and key questions
- [ ] Build visualisations (shot maps, passing networks, player comparisons)
- [ ] Assemble the interactive Streamlit dashboard
- [ ] Publish the dashboard online
- [ ] Stretch goal: build a simple expected goals (xG) model
- [ ] Record a short demo video walkthrough

---

## Project structure

```
womens-football-dashboard/
├── 01_exploration.ipynb    # Exploring the StatsBomb data
├── DEVLOG.md               # Session-by-session development log
├── requirements.txt        # Python libraries needed to run the project
├── .gitignore              # Files excluded from the repository
└── README.md               # You are here
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
