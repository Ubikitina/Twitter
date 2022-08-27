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


# Main function
def main():

	user_id = 727209273248325632 # The user ID can be found in the HTML code of a Tweet that belongs to that user

	# Method for getting the users that is following the above user_id. Also some user fields can be retrieved
	response = client.get_users_following(
		user_id, user_fields=["username","created_at","public_metrics","description"], max_results=1000 # The maximun result number is 1000
	)

	# Loop for printing part of the information stored in the "response" array
	for user in response.data:
		print(user.username, "#", user.created_at, "#", user.public_metrics)

	

if __name__ == "__main__":
	main()
