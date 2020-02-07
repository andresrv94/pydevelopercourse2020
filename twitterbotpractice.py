import tweepy

file = open("credentialsfortwapi.txt","r")

credentials=[] # 0 and 1 are access token and access token secret, 2 and 3 are consumer key and consumer secret

for i in file:
    x=i.split()
    credentials.append(x[1])

file.close()

auth = tweepy.OAuthHandler(credentials[2], credentials[3])
auth.set_access_token(credentials[0], credentials[1])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
