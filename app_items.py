from flask import Flask, jsonify, render_template, request, make_response
import requests
import pandas as pd
import os
from datetime import datetime
import json

from news_app.plots import article_vs_headline_plot, calendar_heatmap, box_plots, lat_lon_heatmap, linechart
from news_app.sentiment import user_analysis, emotion_plotter, find_articles
# from news_app.ngrams import trigram_plot

from nltk import data

NLTK_DATA_LOCATION = os.path.join("news_app", "static", "resources", "nltk_data")
data.path.append(NLTK_DATA_LOCATION)
NLTK_DATA_LOCATION = os.path.join(".", "news_app", "static", "resources", "nltk_data")
data.path.append(NLTK_DATA_LOCATION)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/visualizations")
def visualizations():
    # Read in data
    FILE_PATH = os.path.join("news_app", "static", "data", "headlines_scores_keywords.csv")
    df = pd.read_csv(FILE_PATH)
    # df["datetime"] = df["pub_date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
    
    article_headline_figure = article_vs_headline_plot(df)
    boxplot_data, boxplot_layout = box_plots(df)
    calendar_heatmap_data, calendar_heatmap_layout = calendar_heatmap()
    linechart_figure = linechart()

    with open(os.path.join("news_app", "static", "js", "bigrams.json"), "r") as file:
        bigram_dict = json.load(file)

    bigram_json = json.dumps(bigram_dict)

    with open(os.path.join("news_app", "static", "js", "trigrams.json"), "r") as file:
        trigram_dict = json.load(file)

    trigram_json = json.dumps(trigram_dict)

    return render_template(
        "visualizations.html", 
        article_headline_figure=article_headline_figure,
        boxplot_data=boxplot_data,
        boxplot_layout=boxplot_layout, 
        calendar_heatmap_data=calendar_heatmap_data,
        calendar_heatmap_layout=calendar_heatmap_layout,
        linechart_figure=linechart_figure,
        bigram_json=bigram_json,
        trigram_json=trigram_json,
  )


@app.route("/interactive")
def interactive():
    return render_template("interactive.html")


@app.route("/interactive/user-sentiment", methods=["POST", "GET"])
def user_sentiment():
    print("Running user_sentiment in app.py")
    user_text = request.get_json()
    print(user_text)
    print(type(user_text))

    gauge_data = user_analysis(user_text)
    emotion_plot_data, emotion_plot_layout = emotion_plotter(user_text) 

    response_dict = {
        "gauge_data": gauge_data,
        "emotion_plot_data": emotion_plot_data,
        "emotion_plot_layout": emotion_plot_layout
    }

    response = json.dumps(response_dict)
    return response

@app.route("/interactive/article-search", methods=["POST", "GET"])
def article_search():
    print("Running article_search in app.py")
    search_dict = request.get_json()
    print(search_dict)
    # print(type(search_json))

    find_articles_dict = find_articles(search_dict["keyword"], search_dict["find"])

    response = json.dumps(find_articles_dict)
    return response

@app.route("/maps")
def maps():

    with open(os.path.join("news_app", "static", "js", "fig1_time.json"), "r") as file:
        fig1_time_dict = json.load(file)
    fig1_time_json = json.dumps(fig1_time_dict)

    with open(os.path.join("news_app", "static", "js", "fig2_month.json"), "r") as file:
        fig2_month_dict = json.load(file)
    fig2_month_json = json.dumps(fig2_month_dict)

    with open(os.path.join("news_app", "static", "js", "fig3_weekday.json"), "r") as file:
        fig3_weekday_dict = json.load(file)
    fig3_weekday_json = json.dumps(fig3_weekday_dict)

    with open(os.path.join("news_app", "static", "js", "fig4_time.json"), "r") as file:
        fig4_time_dict = json.load(file)
    fig4_time_json = json.dumps(fig4_time_dict)

    with open(os.path.join("news_app", "static", "js", "fig5_month.json"), "r") as file:
        fig5_month_dict = json.load(file)
    fig5_month_json = json.dumps(fig5_month_dict)
    
    with open(os.path.join("news_app", "static", "js", "fig6_weekday.json"), "r") as file:
        fig6_weekday_dict = json.load(file)
    fig6_weekday_json = json.dumps(fig6_weekday_dict)

    lat_lon_heatmap_dict = lat_lon_heatmap()

    return render_template(
        "maps.html",
        fig1_time_json=fig1_time_json,
        fig2_month_json=fig2_month_json,
        fig3_weekday_json=fig3_weekday_json,
        fig4_time_json=fig4_time_json,
        fig5_month_json=fig5_month_json,
        fig6_weekday_json=fig6_weekday_json,
        lat_lon_heatmap_dict=lat_lon_heatmap_dict
  )