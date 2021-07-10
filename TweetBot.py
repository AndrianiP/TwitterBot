import tweepy
import time
import os
from usernames import *
from LatestTweetID import *
from keys import *

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(token, tokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


chloe = screen_name = usernameOne
zay = screen_name = usernameTwo

latestTweetID = since_id = latestTweet
#latestTweetIDZay = since_id = latestTweetZay

filepath = os.getcwd()

def MakeFile(file_name, newID):
    temp_path = filepath +file_name
    with open(file_name, 'w') as f:
        f.write(
            newID
        )

for tweet in tweepy.Cursor(api.user_timeline, chloe, since=latestTweetID).items():
    tempID = tweet.id
    try:      
        if(tempID > latestTweetID):
            latestTweetID = tempID
            print("\n\n")
            print(tweet.text)
            print(tweet.id)
            tweet.favorite()
            api.update_status(status = 'Have you seen the killer bean movie?', in_reply_to_status_id = latestTweetID , auto_populate_reply_metadata=True)
            MakeFile('LatestTweetID.py','latestTweetChloe = '+tweet.id_str)
            print("Current ID is larger: " +tweet.id_str)
            print("\nOld tweet (in file): "+str(latestTweetID))
    except Exception as e:
        print(e)
    print("NO TWEETS WE ARE SLEEPING")
    time.sleep(120)
    