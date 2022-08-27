# Library imports
import tweepy
import random
import schedule
import time

# Enter here the codes provided by Twitter
consumer_key = 'KKp9sHobkulmF77StcTxbubiU' # API Key
consumer_secret = 'VfPAq81p0GVNDQOwDjkT0x2aabIOQV9mj8aUy2oHPY8mfSOFYS' # API Key Secret

key = '727209273248325632-cchKLvgz05a39RhGMRWOsSDwt3CmrxM' # Access Token
secret = 'EY1wWsqcljFYYxrkvVIwodfbBNyrsPs3GDVjjdvMFUbj4' # Access Token Secret

bearer_token = 'AAAAAAAAAAAAAAAAAAAAACbPZQEAAAAA1AapCMH05sgdZWBDYc4aceyD3ZE%3DLg0hOXGZZbh4sJzTt8gudHfh3e3TUbxF7aLS8DES3NxHZdZxMF'

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
