# This is a webpage devoted to honoring those who served on the USS Russell during WWII.
# Also the Gwin, Princeton and Columbus
# Machine learning to identify ships and people that were together in various battles or at different times during the war
# First iteration: create a map with the routes traveled over the course of the war. Animated map by month - try plotly with mapbox.
# Follow structure of news-app for initial construction.

import json
import requests
from flask import Flask, jsonify, render_template, request, make_response
from uss_russell import russ_map
# from config import api_key, mapbox_token

app = Flask(__name__)

@app.route("/")
def index():
    fig = russ_map()
    return render_template("index.html", fig=fig)

# @app.route("/maps")
# def map():

#     return render_template(
    # "visualizations.html", 
    # article_headline_figure=article_headline_figure,
    # boxplot_data=boxplot_data,
    # boxplot_layout=boxplot_layout, 
    # calendar_heatmap_data=calendar_heatmap_data,
    # calendar_heatmap_layout=calendar_heatmap_layout,
    # linechart_figure=linechart_figure,
    # bigram_json=bigram_json,
    # trigram_json=trigram_json,
#   )

# @app.route("/people")
# def bios():
#     return

@app.route("/places")
def places():
    print("The Places page is up and running!")
    return render_template("places.html")

# @app.route("/things")
# def resources():
#     return



# Home page with brief intro and history
# Interactive Map page with animation of routes traveled during the war, statistics and plots
# Page with bios of the crew (definitely Grandpa and Grandma)
# history and present-day info about the locations visited by the ship
# Resources page with links to media
# Challenge: ML to network ships and crewmembers who crossed paths during the war

# @app.route("/")
# def index():
#     tri_data, tri_layout = trigram_plot()
#     return render_template("index.html", data=tri_data, layout=tri_layout)

# @app.route("/map")
# def map():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/bios")
# def bios():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/places")
# def places():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/resources")
# def resources():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/MLnetwork")
# def MLnetwork():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

if __name__ == "__main__":
    app.run(debug=True)