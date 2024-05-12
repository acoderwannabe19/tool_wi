import time
from django.shortcuts import render, redirect
from pymongo import MongoClient
import pandas as pd




def view_base(request):
    return render(request, "home.html")


def view_champ(request):
    return render(request, "champ.html")


def view_dashboard(request):
    MONGODB_URL = "mongodb+srv://openweathermap:Ept2023@cluster0.fafwdse.mongodb.net/test?retryWrites=true&w=majority"
    COLLECTION_NAME = "openweathermap"

    # Connect to MongoDB
    client = MongoClient(MONGODB_URL)

    # Select the database
    db = client[COLLECTION_NAME]

    weather_collection = db["weather"]
    predictions_collection = db["predictions"]
    
        # Retrieve data from MongoDB collections
    weather_data = weather_collection.find()
    predictions_data = predictions_collection.find()

    # Convert data to DataFrame
    weather_df = pd.DataFrame(list(weather_data))
    predictions_df = pd.DataFrame(list(predictions_data))
    
    last_forecasts = []
    # for column in predictions_df.columns:
    last_forecast = predictions_df["temperature"]
    humidity_list = weather_df["humidity"]
    temp_list = weather_df["temp"]
    wsp_list = weather_df["wind_speed"]


    last_forecasts.append(last_forecast)

    firstEightForecasts = predictions_df["temperature"][:-8]   
    
    print(weather_df.columns) 
    
    
    temp_list = weather_df["temp"].tolist()
    mean_temp = int(sum(temp_list)/len(temp_list))
    hum_list = weather_df["humidity"].tolist()
    mean_hum = int(sum(hum_list)/len(hum_list))
    wsp_list = weather_df["wind_speed"].tolist()
    mean_wsp = int(sum(wsp_list)/len(wsp_list))
    # prec_list = predictions_df["prec"].tolist()
    # mean_prec = int(sum(prec_list)/len(prec_list))
    
    hourly_temp_list = df_hourly["temp_moy"].tolist()
    hours = df_hourly["hour"].tolist()
    
    daily_temp_list = df_daily["temp_moy"].tolist()
    days = df_daily["date"].tolist()
        
    timestamps = df["timestamp"].tolist()
    
    times = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    
    times3hours = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]




    # Convert MongoDB collection to DataFrame
    # df_forecast = pd.DataFrame(list(collection.find()))
    print(weather_df)
    return render(request, "dashboard.html", {
                        'firstEightForecasts': firstEightForecasts,
                         'temp_list': temp_list[-20:], 
        'mean_temp': mean_temp, 
        'hum_list': hum_list[-20:],
        'wsp_list': wsp_list[-20:],
        # 'prec_list': prec_list[-20:], 
        'mean_wsp': mean_wsp, 
        'mean_hum':mean_hum, 
        # 'mean_prec': mean_prec, 
        'times2Hours': times2Hours,

        'times':times, 

                                        })