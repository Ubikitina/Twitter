# Library imports
import tweepy
import random
import schedule
import time

# Enter here the codes provided by Twitter
consumer_key = '1234' # API Key
consumer_secret = '1234' # API Key Secret

key = '1234' # Access Token
secret = '1234' # Access Token Secret

bearer_token = '1234'

# Create the client
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret, 
                       access_token=key, 
                       access_token_secret=secret)


# Array definition
list_tweets = ['Emojis can be used 🍕', 'Tweet 1 text', 'Tweet 2 text', 'Tweet 3 text', 'Tweet 4 text', 'Tweet 5 text', 'Tweet 6 text', 'Tweet 7 text', 'Tweet 8 text', 'Tweet 9 text']

# Method that posts a random tweet of the above array
def tweet_something():
	client.create_tweet(text=random.choice(list_tweets))

# Method that search a text and likes the last 10 tweets with that text
def likeTweets():
	text = "#DataScience"
	tweetsRaw = client.search_recent_tweets(text)
	tweets = tweetsRaw.data

	for tweet in tweets:
		print(tweet.id)
		client.like(tweet.id, user_auth=True)

# Main function
def main():

	client.create_tweet(text="Hello") # Post a tweet that says "Hello"
	tweet_something() # Post a tweet with a random text from the list above
	

	# Schedules an action for every day at the specified time. In this case, the scheduled action likes 10 tweets that include "#DataScience" text 
	schedule.every().day.at('21:03').do(likeTweets)

	while True: # Infinite loop
		try:
			schedule.run_pending() # Checks if there is an action scheduled and runs it
			time.sleep(2) # Waits 2 seconds before restarting the loop
		except tweepy.TweepError as e:
			raise e
	
	

if __name__ == "__main__":
	main()
