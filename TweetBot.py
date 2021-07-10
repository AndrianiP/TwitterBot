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
ceo = screen_name = usernameThree

latestTweetID = since_id = latestTweet
#latestTweetIDZay = since_id = latestTweetZay

latestTweetIDCeo = since_id = latestTweetCeo


filepath = os.getcwd()
def MakeFile(file_name, newID):
    temp_path = filepath + file_name
    with open(file_name, 'w') as f:
        f.write(
            newID
        )

def likeComment():
    tweet.favorite()
    api.update_status(status='If you get this that means the bot i created is working... How long did it take? It doesnt matter, I wont miss a post!',
                      in_reply_to_status_id=latestTweetID, auto_populate_reply_metadata=True)
    MakeFile('LatestTweetID.py', 'latestTweet = '+tweet.id_str+'\nlatestTweetCeo = '+str(latestTweetIDCeo))

while(True):
    print("Checking Chloe's Tweets")
    #Checks for the 15 most recent timelines to speed up checking
    for tweet in tweepy.Cursor(api.user_timeline, chloe, since=latestTweetID).items(15):
        tempID = tweet.id
        try:
            if(tempID > latestTweetID):
                latestTweetID = tempID
                print("\nChloe Tweeted: "+tweet.text)
                print(tweet.created_at)
                likeComment()
        except Exception as e:
            print(e)

    print("Checking Ceo's Tweets")
    #Checks for the 15 most recent timelines to speed up checking
    for tweet in tweepy.Cursor(api.user_timeline, ceo, since=latestTweetIDCeo).items(15):
        tempIDCeo = tweet.id
        try:
            if(tempIDCeo > latestTweetIDCeo):
                latestTweetIDCeo = tempIDCeo
                print("\nCeo Tweeted: "+tweet.text)
                print(tweet.created_at)
                MakeFile('LatestTweetID.py', 'latestTweet = '+str(latestTweetID)+'\nlatestTweetCeo = '+tweet.id_str)
                tweet.favorite()
        except Exception as e:
            print(e)

    print("NO TWEETS WE ARE SLEEPING")
    time.sleep(120)

