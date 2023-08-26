import tweepy
import pandas as pd

consumer_key = "JXRN8j3ZB22PiNKXBOcw2fPxU"  # Your API/Consumer key
consumer_secret = "RYHxUa1Mu4fUA8b7xttWHhDcmxfXdjDKdZOIMDc0SrC5cm9N1l"  # Your API/Consumer Secret Key
access_token = "981585424056569856-5vNYHLfGVLoKIBVEEMk8a8c4BWeSmzK"    # Your Access token key
access_token_secret = "KKvnSm9GwpoDTg8LVy71PeNlRROtrK2uUoDA8rcXlrsuy"  # Your Access token Secret key

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "#asuu_strike -filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 500

try:
    # The number of tweets we want to retrieve from the search
    tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en", tweet_mode='extended').items(no_of_tweets)

    # Pulling some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    # Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of DataFrame
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except tweepy.TweepError as e:
    print('Error:', str(e))
except Exception as e:
    print('Status Failed On,', str(e))



##SECOND CODE BASE
import tweepy
import pandas as pd

consumer_key = "JXRN8j3ZB22PiNKXBOcw2fPxU"  # Your API/Consumer key
consumer_secret = "RYHxUa1Mu4fUA8b7xttWHhDcmxfXdjDKdZOIMDc0SrC5cm9N1l"  # Your API/Consumer Secret Key
access_token = "981585424056569856-5vNYHLfGVLoKIBVEEMk8a8c4BWeSmzK"    # Your Access token key
access_token_secret = "KKvnSm9GwpoDTg8LVy71PeNlRROtrK2uUoDA8rcXlrsuy"  # Your Access token Secret key

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "#asuu_strike -filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 20

try:
    # The number of tweets we want to retrieve from the search
    tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en", tweet_mode='extended').items(no_of_tweets)

    # Pulling some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    # Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of DataFrame
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except tweepy.TweepError as e:
    print('Error:', str(e))
except Exception as e:
    print('Status Failed On,', str(e))


##THIRD CODE
import tweepy
import pandas as pd

consumer_key = "JXRN8j3ZB22PiNKXBOcw2fPxU"
consumer_secret = "RYHxUa1Mu4fUA8b7xttWHhDcmxfXdjDKdZOIMDc0SrC5cm9N1l"
access_token = "981585424056569856-5vNYHLfGVLoKIBVEEMk8a8c4BWeSmzK"
access_token_secret = "KKvnSm9GwpoDTg8LVy71PeNlRROtrK2uUoDA8rcXlrsuy"

auth = tweepy.OAuth1Session(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "#asuu_strike -filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 20

try:
    tweets = tweepy.Cursor(api.search, q=search_query, lang="en", tweet_mode='extended').items(no_of_tweets)

    attributes_container = [
        [tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text]
        for tweet in tweets
    ]

    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except tweepy.TweepError as e:
    print('Error:', str(e))
except Exception as e:
    print('Status Failed On,', str(e))


##FOUTRH CODE
import tweepy
import pandas as pd

consumer_key = "JXRN8j3ZB22PiNKXBOcw2fPxU"
consumer_secret = "RYHxUa1Mu4fUA8b7xttWHhDcmxfXdjDKdZOIMDc0SrC5cm9N1l"
access_token = "981585424056569856-5vNYHLfGVLoKIBVEEMk8a8c4BWeSmzK"
access_token_secret = "KKvnSm9GwpoDTg8LVy71PeNlRROtrK2uUoDA8rcXlrsuy"

auth = tweepy.OAuth1(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "#asuu_strike -filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 20

try:
    tweets = tweepy.Cursor(api.search, q=search_query, lang="en", tweet_mode='extended').items(no_of_tweets)

    attributes_container = [
        [tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text]
        for tweet in tweets
    ]

    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except tweepy.TweepError as e:
    print('Error:', str(e))
except Exception as e:
    print('Status Failed On,', str(e))
