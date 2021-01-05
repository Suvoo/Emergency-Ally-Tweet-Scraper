from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy as tw
import numpy as np
import pandas as pd
import tweepy

class Import_tweet_sentiment:

    consumer_key="Enter Your Consumer Key"
    consumer_secret="Enter Your Consumer Key Secret "
    access_token="Enter Your  Access Token"
    access_token_secret="Enter Your Access Token Secret"

    def tweet_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df

    def get_tweets(self, handle):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        auth_api = API(auth)

        account = handle
        item = auth_api.user_timeline(id=account,count=50)
        df = self.tweet_to_data_frame(item)

        all_tweets = []
        for j in range(50):
            all_tweets.append(df.loc[j]['Tweets'])
        return all_tweets

    def get_hashtag(self, hashtag):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        auth_api = API(auth)
        account = hashtag
        all_tweets = []

        for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en',tweet_mode='extended').items(50):
            
            status=tweet
            if 'extended_tweet' in status._json: 
                
                status_json = status._json['extended_tweet']['full_text'] 
                #status=tweet
                
            elif 'retweeted_status' in status._json and 'extended_tweet' in status._json['retweeted_status']: 
                status_json = status._json['retweeted_status']['extended_tweet']['full_text'] 
            elif 'retweeted_status' in status._json: 
                status_json = status._json['retweeted_status']['full_text'] 
            else: 
                status_json = status._json['full_text'] 
            print(status_json)
            all_tweets.append(status_json)
        return all_tweets