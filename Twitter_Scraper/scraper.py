#This file scrapes what is trending from twitter, records the top
#50 trending subjects, and their associated information
#First part of code heavily utilized code from this video:
#https://www.youtube.com/watch?v=Lu1nskBkPJU&t=696s
from sqlite3 import Cursor
import tweepy
import configparser
import os
import pandas
import tweet_analyzer
from datetime import date, datetime
import snscrape.modules.twitter as twt


#gets authentication information for Twitter from config.ini file
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication

authentication = tweepy.OAuthHandler(api_key, api_key_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication)

#get all the available locations for getting trends
available_loc = api.available_trends()

#To change location to a different, enter corresponding woeid
#Use this website to find woeid for your specific location:
#https://www.woeids.com/   
usa_woeid = 23424977

#gets trends
trends = api.get_place_trends(usa_woeid)




#gets current date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#formating for csv file
columns = ['Trend', 'URL','Is Promoted Content','Tweet Volume', 'Query', 'Time_US_Central']

#contains data that will be added to csv file
data = []

today = date.today()
print (today)
year = today.year
month = today.month
day = today.day


#appends data to data array
for trend in trends[0]['trends']:
    isTrend = False
    if trend['promoted_content'] != None:
        isTrend = True
    data.append([trend['name'], trend['url'], isTrend, trend['tweet_volume'], trend['query'], str(today) + current_time])
    

df = pandas.DataFrame(data, columns = columns)

#print(df)

#changes working directory to data file containg information pertaining to trending
os.chdir(os.curdir + '/Trending_Data')

#save data aquired from twitter
#The file name is formated with trending[year][month][day][hour][minute][second].csv
df.to_csv('trending' +  "__" + str(today) + "__" +current_time[0:2] + "-" + current_time[3:5] + "-" + current_time[6:8] + '.csv')


#creating directories to store tweet data for various trends
os.chdir('../')
os.chdir(os.curdir + '/Tweet_Data')

titleFolder = os.curdir + '/Trending_Tweets_Data__'  + str(today) + "__" +current_time[0:2] + "-" + current_time[3:5] + "-" + current_time[6:8]
os.mkdir(titleFolder)
os.chdir(titleFolder)


'''
This piece of code loops through a list of current trends, then
queries Twitter for tweets related to said trend. The collected 
tweets are then saved to a .csv file associated with the trend.
The limit variable(marked below) is how many tweets per trend will
be scraped and saved into the .csv file. The greater the limit 
number, the longer the program runtime will be. 
'''
for query_trend in df['Trend']:

    #limit variable
    limit = 1000
    
    length = 0
    results = []
    for tweet in twt.TwitterSearchScraper(query_trend).get_items():

        if length >= limit:
            break
        length += 1
        results.append([tweet.content, tweet.user.username, tweet.date])
    
    df = pandas.DataFrame(results, columns = ['Tweet_Contents','Username', 'Date_Posted'])
    
    df.to_csv(query_trend + '.csv')
