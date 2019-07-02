# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pickle
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def TVShows_list():
    getPage = requests.get('https://www.imdb.com/chart/toptv/')
    getPage.raise_for_status()
    Page = BeautifulSoup(getPage.text, 'html.parser')
    TV_details = {
        "data": []
    }
    TVList = Page.find_all('tr')
    #print(TVList)
    count= 0
    for data in TVList[1:251]: 
        count = count + 1
        print(count)
        #print(data)
        name = data.find('td',class_="titleColumn").text 
        print(name)
        print("     ")
        rating = data.find('td',class_="imdbRating").text
        print("Rating")
        print(rating)
        print("     ")
        
        details = {
                    "Name" : name,
                    "Rating" : rating,
                }
        TV_details['data'].append(details)
        print("        ")
    #print(TV_details)
    with open('TV_details_pickle.pkl', 'wb') as f:
        pickle.dump(TV_details,f,protocol=pickle.HIGHEST_PROTOCOL) 
        


def results():
    ratings = []
    years = []
    counterRatingsKeys = []
    counterRatingsValues = []
    counterYearsKeys = []
    counterYearsValues = []
    with open('TV_details_pickle.pkl', 'rb') as f:   
        data = pickle.load(f)
        for l in data['data']:
            r = l['Rating'].strip()
            ratings.append(r)
            y =l['Name'].lstrip().splitlines( )[2][1:5]
            years.append(y)
    counterRating =collections.Counter(ratings)
    #print(counterRating)
    for key in counterRating.keys():
        counterRatingsKeys.append(key)
    for values in counterRating.values():
        counterRatingsValues.append(values)
    counterYears =collections.Counter(years)
    for key in counterYears.keys():
        counterYearsKeys.append(key)
    for values in counterYears.values():
        counterYearsValues.append(values)
    frequencies = counterYearsValues
    freq_series = pd.Series(frequencies)
    y_labels = counterYearsKeys
    plt.figure(figsize=(44, 44))
    ax = freq_series.plot(kind='barh')
    ax.set_title('Examine on popular TV shows in IMDB using web scraping')
    ax.set_xlabel('Number of series')
    ax.set_ylabel('Year')
    ax.set_yticklabels(y_labels)
    ax.set_xlim(0, 16) # expand xlim to make labels easier to read
    rects = ax.patches
    

    for rect in rects:
        # Get X and Y placement of label from rect.
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        ha = 'left'

        # If value of bar is negative: Place label left of bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label at right
            ha = 'right'

        # Use X value as label and format number with one decimal place
        label = "{:.1f}".format(x_value)

        # Create annotation
        plt.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha)                      # Horizontally align label differently for
    plt.savefig("image.png")
    
    
    frequencies = counterRatingsValues
    freq_series = pd.Series(frequencies)
    y_labels = counterRatingsKeys
    plt.figure(figsize=(44, 44))
    ax = freq_series.plot(kind='barh')
    ax.set_title('Examine on popular TV shows in IMDB using web scraping')
    ax.set_xlabel('Number of series')
    ax.set_ylabel('Year')
    ax.set_yticklabels(y_labels)
    ax.set_xlim(0, 84) # expand xlim to make labels easier to read
    rects = ax.patches
    

    for rect in rects:
        # Get X and Y placement of label from rect.
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        ha = 'left'

        # If value of bar is negative: Place label left of bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label at right
            ha = 'right'

        # Use X value as label and format number with one decimal place
        label = "{:.1f}".format(x_value)

        # Create annotation
        plt.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha)                      # Horizontally align label differently for
    plt.savefig("image2.png")
   
    
    
results()

    