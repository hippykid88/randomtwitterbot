import random
from  twython import Twython

CONSUMER_KEY = 'PLACE KEY HERE'
CONSUMER_SECRET = 'PLACE KEY HERE'
ACCESS_KEY = 'PLACE KEY HERE'
ACCESS_SECRET = 'PLACE KEY HERE'

twitter = Twython( CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET )


def twitter_file():
    random_options = [ 'Burgers:burger.jpg', 'French_Toast:French_Toast.jpeg', 'Prime_Rib:Prime_Rib.jpeg',
                       'Omelettes:Omelettes.jpeg' ]
    random_tweets = random.choice( random_options )
    file, photo = random_tweets.split( ':' )
    print( file )
    print( photo )
    file_open = open( str( file ), 'r' )
    twitter_file = file_open.read()
    photo_open = open( photo, 'rb' )
    response = twitter.upload_media( media=photo_open )
    return twitter_file, response

random_tweet, response = twitter_file()


"""build text part of tweet"""
tweet = "Come on down to Moon Valley Cafe and try out our " + random_tweet + " #food #phoenix #localbuiness #family"

"""tweets status and media"""
twitter.update_status( status=tweet, media_ids=[response['media_id']] )
