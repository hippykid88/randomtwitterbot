#!/usr/local/bin/python3.6
import random, config
from  twython import Twython


twitter = Twython( config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_KEY, config.ACCESS_SECRET )


def twitter_file():
    random_tweet = random.choice(config.OPTION)
    photo_open = open( random_tweet["media"], 'rb' )
    response = twitter.upload_media( media=photo_open )
    return random_tweet["tweet_text"], response

tweet_text, response = twitter_file()


"""build text part of tweet"""
tweet = "Come on down to Moon Valley Cafe and try out our " + tweet_text + " #food #phoenix #localbuiness #family"

"""tweets status and media"""
twitter.update_status( status=tweet, media_ids=[response['media_id']] )
