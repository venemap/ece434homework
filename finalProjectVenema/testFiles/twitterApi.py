#!/usr/bin/env python3
import os
import tweepy as tw

consumer_key = 'jHAWioEk8vdYB2gzgUKtc9sVG'
consumer_secret = 'dEObnn9pxY6nlv598C3NtfnQQwkwESGhAHjzHCrqFMDi7Dg7xd'
access_token = '1322980232333320207-C8srXdQnyheWrGmu006QpIdzBSYrOX'
access_token_secret =  'jPFUITzmajeURIBvwvqlZx0jctkJnMWVM4WgwiGKtdZPM'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)


public_tweets = api.home_timeline()

#api.update_status("Hello tweepy")


user = api.get_user('ece343final')
print(user.screen_name)
print(user.followers_count)
for tweet in public_tweets:
    print(tweet.text)