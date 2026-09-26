import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsbombpy import sb
from mplsoccer import Pitch

st.set_page_config(page_title="England's Euro 2025 Journey",
                   page_icon="⚽", layout="wide")

PINK = "#FF5C9D"
DARK = "#121212"
GREY = "#555555"


# ---------- DATA ----------

@st.cache_data
def load_data():
    matches = sb.matches(competition_id=53, season_id=315)
    england = matches[
        matches["home_team"].str.contains("England") |
        matches["away_team"].str.contains("England")
    ].sort_values("match_date")

    all_events = []
    for match_id in england["match_id"]:
        all_events.append(sb.events(match_id=match_id))
    events = pd.concat(all_events)

    shots = events[(events["type"] == "Shot") & (events["period"] < 5)].copy()
    shots["is_goal"] = shots["shot_outcome"] == "Goal"
    shots[["x", "y"]] = pd.DataFrame(
        shots["location"].tolist(), index=shots.index)

    return england, events, shots


def build_journey(shots, england):
    summary = shots.groupby(["match_id", "team"]).agg(
        shots=("shot_statsbomb_xg", "count"),
        xg=("shot_statsbomb_xg", "sum"),
        goals=("is_goal", "sum")
    ).round(2).reset_index()

    eng = summary[summary["team"].str.contains("England")]
    opp = summary[~summary["team"].str.contains("England")]

    journey = eng.merge(opp, on="match_id", suffixes=("_eng", "_opp"))
    journey = journey.merge(england[["match_id", "match_date"]], on="match_id")
    journey = journey.sort_values("match_date").reset_index(drop=True)

    journey["opponent"] = journey["team_opp"].str.replace(
        r" (Women's|W)$", "", regex=True)
    journey["stage"] = ["Group", "Group", "Group",
                        "Quarter-final", "Semi-final", "Final"]
    journey["pens"] = ["", "", "", " (won on pens)", "", " (won on pens)"]
    journey["score"] = (journey["goals_eng"].astype(int).astype(str) + "–"
                        + journey["goals_opp"].astype(int).astype(str) + journey["pens"])
    journey["label"] = journey["stage"] + "\n" + \
        journey["opponent"] + "\n" + journey["score"]
    return journey


def build_players(shots, events):
    eng_np = shots[shots["team"].str.contains(
        "England") & (shots["shot_type"] != "Penalty")]

    shooting = eng_np.groupby("player").agg(
        shots=("shot_statsbomb_xg", "count"),
        npxg=("shot_statsbomb_xg", "sum"),
        goals=("is_goal", "sum")
    )

    assisted = eng_np[["shot_key_pass_id", "shot_statsbomb_xg", "is_goal"]].dropna(
        subset=["shot_key_pass_id"]
    )
    key_passes = events[["id", "player"]].merge(
        assisted, left_on="id", right_on="shot_key_pass_id"
    )
    creating = key_passes.groupby("player").agg(
        chances_created=("id", "count"),
        xg_assisted=("shot_statsbomb_xg", "sum"),
        assists=("is_goal", "sum")
    )

    players = shooting.join(creating, how="outer").fillna(0).round(2)
    return players.sort_values("npxg", ascending=False)


# ---------- CHARTS ----------

def style_axes(ax):
    ax.tick_params(colors="white")
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    for side in ["left", "bottom"]:
        ax.spines[side].set_color(GREY)


def journey_chart(journey):
    x = np.arange(len(journey))
    width = 0.38

    fig, ax = plt.subplots(figsize=(12, 6.5))
    fig.set_facecolor(DARK)
    ax.set_facecolor(DARK)

    bars_eng = ax.bar(
        x - width/2, journey["xg_eng"], width, color=PINK, label="England")
    bars_opp = ax.bar(
        x + width/2, journey["xg_opp"], width, color=GREY, label="Opponent")

    eng_labels = [f"{xg:.2f} ({int(g)})" for xg, g in zip(
        journey["xg_eng"], journey["goals_eng"])]
    opp_labels = [f"{xg:.2f} ({int(g)})" for xg, g in zip(
        journey["xg_opp"], journey["goals_opp"])]
    ax.bar_label(bars_eng, labels=eng_labels,
                 color=PINK, fontsize=9, padding=3)
    ax.bar_label(bars_opp, labels=opp_labels,
                 color="#BBBBBB", fontsize=9, padding=3)

    ax.set_xticks(x)
    ax.set_xticklabels(journey["label"], color="white", fontsize=9)
    ax.set_ylabel("Expected goals (xG)", color="white")
    style_axes(ax)

    ax.set_title("Bar labels show xG (actual goals in brackets)",
                 color="#BBBBBB", fontsize=11)
    ax.legend(facecolor=DARK, edgecolor=GREY, labelcolor="white")
    return fig


def shot_map(match_shots, opponent):
    eng = match_shots[match_shots["team"].str.contains("England")]
    opp = match_shots[~match_shots["team"].str.contains("England")].copy()
    opp["x"] = 120 - opp["x"]
    opp["y"] = 80 - opp["y"]

    pitch = Pitch(pitch_type="statsbomb", pitch_color=DARK, line_color=GREY)
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor(DARK)

    pitch.scatter(eng["x"], eng["y"], ax=ax, s=eng["shot_statsbomb_xg"] * 800,
                  color=PINK, edgecolors=DARK, alpha=0.8, label="England", zorder=2)
    pitch.scatter(opp["x"], opp["y"], ax=ax, s=opp["shot_statsbomb_xg"] * 800,
                  color="white", edgecolors=DARK, alpha=0.8, label=opponent, zorder=2)

    eng_goals = eng[eng["is_goal"]]
    opp_goals = opp[opp["is_goal"]]
    pitch.scatter(eng_goals["x"], eng_goals["y"], ax=ax, s=700, marker="*",
                  color=PINK, edgecolors="white", linewidths=1.5,
                  label="England goal", zorder=3)
    pitch.scatter(opp_goals["x"], opp_goals["y"], ax=ax, s=700, marker="*",
                  color="white", edgecolors=PINK, linewidths=1.5,
                  label=f"{opponent} goal", zorder=3)

    ax.legend(facecolor=DARK, edgecolor=GREY, labelcolor="white",
              loc="lower center", ncol=4)
    return fig


def top10_chart(players):
    top = players.head(10).sort_values("npxg")

    fig, ax = plt.subplots(figsize=(8, 6.5))
    fig.set_facecolor(DARK)
    ax.set_facecolor(DARK)

    bars = ax.barh(top.index, top["npxg"], color=PINK)
    labels = [f"{xg:.2f} ({int(g)})" for xg,
              g in zip(top["npxg"], top["goals"])]
    ax.bar_label(bars, labels=labels, color="white", fontsize=9, padding=4)

    ax.set_xlabel("Non-penalty xG (goals in brackets)", color="white")
    style_axes(ax)
    return fig


def creators_chart(players):
    data = players[(players["npxg"] + players["xg_assisted"]) >= 0.5]

    fig, ax = plt.subplots(figsize=(8, 6.5))
    fig.set_facecolor(DARK)
    ax.set_facecolor(DARK)

    ax.scatter(data["npxg"], data["xg_assisted"], s=120,
               color=PINK, edgecolors="white", zorder=3)
    for name, row in data.iterrows():
        ax.annotate(name.split()[-1], (row["npxg"], row["xg_assisted"]),
                    xytext=(7, 5), textcoords="offset points", color="white", fontsize=9)

    ax.axvline(data["npxg"].mean(), color=GREY, linestyle="--", linewidth=1)
    ax.axhline(data["xg_assisted"].mean(), color=GREY,
               linestyle="--", linewidth=1)

    ax.set_xlabel("Shooting threat: non-penalty xG", color="white")
    ax.set_ylabel("Creating threat: xG assisted", color="white")
    style_axes(ax)
    return fig


# ---------- PAGE ----------

st.title("England's Euro 2025 journey")
st.write(
    "An interactive look at how England won Euro 2025, using professional "
    "match event data. Explore the tournament match by match, dive into any "
    "game's shots, and see which players drove England's attack."
)
st.caption("Data: StatsBomb Open Data  ·  Excludes penalty shootouts")

with st.spinner("Loading match data..."):
    england, events, shots = load_data()

journey = build_journey(shots, england)

tab_overview, tab_match, tab_players = st.tabs(
    ["Tournament overview", "Match explorer", "Player view"]
)

with tab_overview:
    st.subheader("Chances created vs goals scored, match by match")
    st.pyplot(journey_chart(journey))
    st.write(
        "England were out-created in their opening defeat to France, dominated "
        "the Netherlands and Wales, were level on chances with Sweden, and were "
        "clearly stronger than Italy. In the final, Spain created more than twice "
        "England's xG, but England held on and won on penalties."
    )

with tab_match:
    st.subheader("Explore any match")

    journey["menu"] = (journey["stage"] + ": England vs " + journey["opponent"]
                       + " (" + journey["score"] + ")")
    choice = st.selectbox("Choose a match", journey["menu"])

    row = journey[journey["menu"] == choice].iloc[0]
    match_shots = shots[shots["match_id"] == row["match_id"]]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("England xG", f"{row['xg_eng']:.2f}")
    col2.metric(f"{row['opponent']} xG", f"{row['xg_opp']:.2f}")
    col3.metric("England shots", int(row["shots_eng"]))
    col4.metric(f"{row['opponent']} shots", int(row["shots_opp"]))

    st.pyplot(shot_map(match_shots, row["opponent"]))
    st.caption(
        "England attack right, opponents attack left. Dot size = xG. Stars = goals.")

with tab_players:
    st.subheader("Who drove England's attack?")
    players = build_players(shots, events)

    left, right = st.columns(2)
    with left:
        st.markdown("**Top 10 by non-penalty xG**")
        st.pyplot(top10_chart(players))
    with right:
        st.markdown("**Shooters vs creators**")
        st.pyplot(creators_chart(players))
        st.caption("Further right = more shooting threat. Higher up = more chances "
                   "created. Dashed lines = squad average.")

    st.write(
        "Alessia Russo led England in both shooting threat and assists, with "
        "Ella Toone and Lauren Hemp completing an attacking core dangerous in "
        "both roles. Chloe Kelly's real strength was creating chances, and "
        "Lauren Hemp created the most xG for others but finished with no assists."
    )

    st.markdown("**Full squad stats** (click a column header to sort)")
    st.dataframe(
        players.rename(columns={
            "shots": "Shots", "npxg": "npxG", "goals": "Goals",
            "chances_created": "Chances created",
            "xg_assisted": "xG assisted", "assists": "Assists"
        }),
        use_container_width=True
    )
