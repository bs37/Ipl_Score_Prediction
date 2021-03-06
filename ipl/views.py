from django.shortcuts import HttpResponse, render
import pandas as pd
import pickle

def home(request):
    return render(request, "templates/home.html")


def add(request):
    a = int(request.GET['val1'])
    b = int(request.GET['val2'])
    c = a + b
    return render(request, "templates/result.html", {"addition" : c})

def predict(request):
    bat_team = request.GET['bat_team']
    bowl_team = request.GET['bowl_team']
    runs = request.GET['runs']
    wickets = request.GET['wickets']
    overs = request.GET['overs']
    runs_last_5 = request.GET['runs_last_5']
    wickets_last_5 = request.GET['wickets_last_5']

    df = []

    if bat_team == "bat_team_Chennai Super Kings":
        df = df + [1, 0, 0, 0, 0, 0, 0, 0]
        st = "CSK"
    elif bat_team == "bat_team_Delhi Daredevils":
        df = df + [0, 1, 0, 0, 0, 0, 0, 0]
        st = "DC"
    elif bat_team == "bat_team_Kings XI Punjab":
        df = df + [0, 0, 1, 0, 0, 0, 0, 0]
        st = "PK"
    elif bat_team == "bat_team_Kolkata Knight Riders":
        df = df + [0, 0, 0, 1, 0, 0, 0, 0]
        st = "KKR"
    elif bat_team == "bat_team_Mumbai Indians":
        df = df + [0, 0, 0, 0, 1, 0, 0, 0]
        st = "MI"
    elif bat_team == "bat_team_Rajasthan Royals":
        df = df + [0, 0, 0, 0, 0, 1, 0, 0]
        st = "RR"
    elif bat_team == "bat_team_Royal Challengers Bangalore":
        df = df + [0, 0, 0, 0, 0, 0, 1, 0]
        st = "RCB"
    elif bat_team == "bat_team_Sunrisers Hyderabad":
        df = df + [0, 0, 0, 0, 0, 0, 0, 1]
        st = "SRH"

    if bowl_team == "bowl_team_Chennai Super Kings":
        df = df + [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == "bowl_team_Delhi Daredevils":
        df = df + [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == "bowl_team_Kings XI Punjab":
        df = df + [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == "bowl_team_Kolkata Knight Riders":
        df = df + [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == "bowl_team_Mumbai Indians":
        df = df + [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == "bowl_team_Rajasthan Royals":
        df = df + [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == "bowl_team_Royal Challengers Bangalore":
        df = df + [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == "bowl_team_Sunrisers Hyderabad":
        df = df + [0, 0, 0, 0, 0, 0, 0, 1]
        
    df = df + [int(runs)]
    df = df + [int(wickets)]
    df = df + [float(overs)]
    df = df + [int(runs_last_5)]
    df = df + [int(wickets_last_5)]
    df = [df]

    # fileName = "first_inning_score_prediction.pkl"

    with open('static/first_inning_score_prediction.pkl', 'rb') as f:
        model = pickle.load(f)

    df = int(model.predict(df))
    df2 = df + 20

    return render(request, "templates/predict.html", {"score1": df, "score2": df2, "team": st})

