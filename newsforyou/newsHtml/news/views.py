from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import requests
import json
import time
import datetime


def index(request):
    newsApi = requests.get(
        url='https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=606014a906f14ea59a48b33381c5f972')
    #https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=606014a906f14ea59a48b33381c5f972
    #indian https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=606014a906f14ea59a48b33381c5f972
    dump = newsApi.json()
    # dumps the json object into an element
    json_str = json.dumps(dump)
    # load the json to a string
    # var resp has all the values from json
    resp = json.loads(json_str)
    date = datetime.date.today()
    context = {"title0": resp["articles"][0]["title"],
               "urlToImage0": resp["articles"][0]["urlToImage"],
               "url0": resp["articles"][0]["url"],
               "desp0":resp["articles"][0]["description"],
               "title1": resp["articles"][1]["title"],
               "urlToImage1": resp["articles"][1]["urlToImage"],
               "url1": resp["articles"][1]["url"],
               "desp1": resp["articles"][1]["description"],
               "title2": resp["articles"][2]["title"],
               "urlToImage2": resp["articles"][2]["urlToImage"],
               "url2": resp["articles"][2]["url"],
               "desp2": resp["articles"][2]["description"],
               "title3": resp["articles"][3]["title"],
               "urlToImage3": resp["articles"][3]["urlToImage"],
               "url3": resp["articles"][3]["url"],
               "desp03": resp["articles"][3]["description"],
               "title4": resp["articles"][4]["title"],
               "urlToImage4": resp["articles"][4]["urlToImage"],
               "url4": resp["articles"][4]["url"],
               "desp4": resp["articles"][4]["description"],
               "title5": resp["articles"][5]["title"],
               "urlToImage5": resp["articles"][5]["urlToImage"],
               "url5": resp["articles"][5]["url"],
               "desp5": resp["articles"][5]["description"],
               "title6": resp["articles"][6]["title"],
               "urlToImage6": resp["articles"][6]["urlToImage"],
               "url6": resp["articles"][6]["url"],
               "desp6": resp["articles"][6]["description"],
               "title7": resp["articles"][7]["title"],
               "urlToImage7": resp["articles"][7]["urlToImage"],
               "url7": resp["articles"][7]["url"],
               "desp7": resp["articles"][7]["description"],
               "date":date,
               }

    # return render(request,"home/index1.html",{'h': urlToArticle,'re': desc, 're1': urlToImage,'ti': title})
    return render(request, "home/index.html", context)