# Core script

import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import os, csv, requests, json, datetime
import numpy as np
# from config import mapbox_token
from datetime import date
# import re
from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy
# from sklearn.feature_extraction.text import CountVectorizer
# import nltk
# from nltk.corpus import stopwords

# mapbox_token = os.getenv("mapbox_token")

# app = Flask(__name__)

# When database is implemented, will need something like this:
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_CONN")
# db = SQLAlchemy(app)

# PATH = os.path.join("data", "files", "headlines_with_nid.csv")

# px.set_mapbox_access_token(mapbox_token)

# Best to build this here or better to make in a CSV or Excel file first?
# Timeline = Event, Date, Location, Commentary, Latitude, Longitude, Action
# Add changes of command
# Hovering over or clicking on an event highlights the ship's location on the map.
# Show on the map other notable events occurring at the same time as Russell's actions.

# timeline = [
#     (
#         "Keel Date",
#         "12-20-1937",
#         "Newport News, VA",
#         "Newport News Shipbuilding & Drydock Co.",
#         37.0870821,
#         -76.4730122,
#     ),
#     (
#         "Launch Date",
#         "12-8-1938",
#         "Newport News, VA",
#         "NA",
#         37.0870821,
#         -76.4730122,
#     ),
#     (
#         "Commissioned",
#         "11-3-1939",
#         "Newport News, VA",
#         "NA",
#         37.0870821,
#         -76.4730122,
#     ),
#     (
#         "Decommissioned",
#         "11-15-1945",
#         "San Diego, CA",
#         "NA",
#         32.7152778,
#         -117.1563889,
#     ),
#     (
#         "Lend Lease Act Signing",
#         "09-01-1940",
#         "Halifax, Nova Scotia",
#         "Exact date in September unknown. Check historical record on Lend-Lease Act.",
#         44.65,
#         -63.6,
#     ),
#     (
#         "Target Practice",
#         "12-7-1941 12:53",
#         "Cosco Bay, Maine",
#         "NA",
#         43.640800,
#         -70.257440,
#     ),  # 7:53am Honolulu time, first wave of Japanese attack on Pearl Harbor
#     (
#         "Repairs",
#         "12-17-1941",
#         "New York Navy Yard",
#         "Received orders for the Pacific sailing with the carrier Yorktown and four other destroyers.",
#         40.712345,
#         -74.005531,
#     ),
#     (
#         "Set sail with reinforcements",
#         "01-06-1942",
#         "San Diego Naval Base",
#         "Sailed west, screening reinforcements to Samoa.",
#         32.7152778,
#         -117.1563889,
#     ),
#     (
#         "Arrival in Samoa",
#         "01-20-1942",
#         "Pago Pago, Samoa",
#         "Arrived in Samoa with reinforcements.",
#         -14.273280,
#         -170.702970,
#     ),
#     (
#         "Airmen Rescue",
#         "12-23-1941",
#         "Pacific",
#         "Rescued two airmen crashed after takeoff from Yorktown. Location uncertain.",
#         15.305380,
#         -108.701307,
#     ),
#     (
#         "Submarine Encounter",
#         "12-20-1941",
#         "Pacific near Panama Canal",
#         "Attacked probable submarine shortly after entering Pacific Ocean. Location uncertain.",
#         5.840081,
#         -83.121784,
#     ),
# ]

# df = pd.DataFrame(
#     timeline, columns=["event", "date", "location", "comment", "latitude", "longitude"]
# )

# df["date"] = pd.to_datetime(df["date"])

# df.sort_values(by="date", inplace=True)

# Write to CSV file
# df.to_csv("timeline.csv", index=False)

# mapbox_style: str (default `'basic'`, needs Mapbox API token)
#     Identifier of base map style, some of which require a Mapbox API token
#     to be set using `plotly.express.set_mapbox_access_token()`. Allowed
#     values which do not require a Mapbox API token are `'open-street-map'`,
#     `'white-bg'`, `'carto-positron'`, `'carto-darkmatter'`, `'stamen-
#     terrain'`, `'stamen-toner'`, `'stamen-watercolor'`. Allowed values
#     which do require a Mapbox API token are `'basic'`, `'streets'`,
#     `'outdoors'`, `'light'`, `'dark'`, `'satellite'`, `'satellite-
#     streets'`.

# df = pd.read_csv("timeline.csv")

def russ_map():               # Have to use JS format to render on webpage?
    df = pd.read_csv("timeline.csv")
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        #     color="action",
        #     size="event",
        hover_name="event",
        hover_data=["date", "location", "comment"],
        title="Events and Places of the USS Russell DD 414 - WWII",
        mapbox_style="basic",
        width=1250,
        height=900,
        animation_frame="event_date",  # The single line that brings animation to the map based on the parameter indicated
    )
    fig.update_traces(
        marker_size=20,
        marker_color="navy",
        selector=dict(
            type="scattermapbox"
        ),  # Color starts with navy but changes to default after first frame. Recall this from eBird project...
    )
    # plotly.io.write_json(fig, "static/js/location_map.json")
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

#######################################################################################

# russ_map(df)

#######################################################################################

# @app.route("/")
# def home():
#     fig = russ_map()
#     return render_template("russ.html", fig=fig)

# if __name__ == "__main__":
#     app.run(debug=True)