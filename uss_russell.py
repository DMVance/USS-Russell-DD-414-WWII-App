# This is a webpage devoted to honoring those who served on the USS Russell during WWII.
# Also the Princeton and Columbus
# Machine learning to identify ships and people that were together in various battles or at different times during the war
# First iteration: create a map with the routes traveled over the course of the war. Animated map by month - try plotly with mapbox.

import json
from flask import Flask, jsonify, render_template
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import os

app = Flask(__name__)

mapbox_token = "your key here"
api_key = "97b0a5778687b29af9fa0cf9fadbf1f3"

def home():
    return 

def map():
    return

def bios():
    return

def places():
    return

def resources():
    return



# Home page with brief intro and history
# Interactive Map page with animation of routes traveled during the war, statistics and plots
# Page with bios of the crew (definitely Grandpa and Grandma)
# history and present-day info about the locations visited by the ship
# Resources page with links to media
# Challenge: ML to network ships and crewmembers who crossed paths during the war

@app.route("/")
def home():
    tri_data, tri_layout = trigram_plot()
    return render_template("index.html", data=tri_data, layout=tri_layout)

@app.route("/map")
def map():
    bi_data, bi_layout = bigram_plot()
    return render_template("bigram.html", data=bi_data, layout=bi_layout)

@app.route("/bios")
def bios():
    bi_data, bi_layout = bigram_plot()
    return render_template("bigram.html", data=bi_data, layout=bi_layout)

@app.route("/places")
def places():
    bi_data, bi_layout = bigram_plot()
    return render_template("bigram.html", data=bi_data, layout=bi_layout)

@app.route("/resources")
def resources():
    bi_data, bi_layout = bigram_plot()
    return render_template("bigram.html", data=bi_data, layout=bi_layout)

@app.route("/MLnetwork")
def MLnetwork():
    bi_data, bi_layout = bigram_plot()
    return render_template("bigram.html", data=bi_data, layout=bi_layout)

if __name__ == "__main__":
    app.run(debug=True)