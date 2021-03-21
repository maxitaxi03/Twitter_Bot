import tweepy

auth = tweepy.OAuthHandler("BX0vau2Hd7erHwRMnrVhjfRuw", "NbJotNquvWuWNYQQ32CtAq9ULpvnOfij5pVnxY7VsSzB7McPBp")
auth.set_access_token("1318704537994207237-HyjfCiMjQ0J0LhZBX8KraiJq5K0LTZ", "6pOL1EGNYWiJo0ZQ6IQGfVOzjml8N47xK507kx2eOaMcr")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


x = api.update_status(input("Please input your tweet now: "))

#user = api.get_user('twitter')
#print(user.screen_name)
#print(user.followers_count)

