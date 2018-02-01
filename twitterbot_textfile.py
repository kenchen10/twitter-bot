from credentials import *
import tweepy
from time import sleep

# Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('verne.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
    # Catch and output errors
    try:
        print(line)
        # Ensure that blank lines are skipped
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    # Tweet every 15 minutes
    sleep(900)
