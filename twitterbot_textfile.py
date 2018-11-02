from credentials import *
import tweepy
from time import sleep
import string

# Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

most_used_by_trump = {"American": "USAian", "American": "USAians", "people": "flesh and blood",
                        "tonight": "when sun go bye", "new": "pristine",
                        "America": "Land of the Free", "great": "considerable",
                        "year": "a period of 365 days starting from any date", "congress": "CONgress",
                        "ISIS": "ad-dawla al-ʾislāmiyya fī l-ʿirāq waš-šām", "Democrats": "libtards"}
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def get_tweets(username):
    # Get tweets from a user.
    num_tweets = 100
    tweets = api.user_timeline(screen_name = username, count = num_tweets)
    tmp = []
    tweets_csv = [tweet.text for tweet in tweets]
    for j in tweets_csv:
        t = replace_all(j, most_used_by_trump)
        api.update_status(t)

def print_text(txt):
    # Open text file verne.txt (or your chosen file) for reading
    my_file = open(txt, 'r')

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

get_tweets("HillaryClinton")
