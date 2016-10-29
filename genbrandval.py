import csv
import tweepy
from textblob import TextBlob

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = ''
consumer_secret = ''

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open('names.txt', 'r')
headerList = ['Time']

# Get the sentiment analysis for each of the tweets in the for loop.
# Generate the brand score based on the subjectivity and polarity of each tweet
for line in f:
        print(line)
        headerList = headerList + [line]
        public_tweets = api.search(q=line, show_user=True)
        sum = 0.00

        for tweet in public_tweets:
           #print(tweet.text)
           print(tweet.user.name + ":::" + tweet.text)
           analysis = TextBlob(tweet.text)
           print("Subjectivity: " + str(analysis.sentiment.subjectivity)  + "Polarity: " + str(analysis.sentiment.polarity))
           sum = sum + (analysis.sentiment.subjectivity * analysis.sentiment.polarity)

	# Display the brand value
        print("Brand Score = " + str(sum * 100))
        #print(sum * 100)

# Display the trends based on location. The below data is additional data which may or may not be used based on changes in the algorithm
trends1 = api.trends_place(2295420) # from the end of your code
# trends1 is a list with only one element in it, which is a
# dict which we'll put in data.
data = trends1[0]
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)
