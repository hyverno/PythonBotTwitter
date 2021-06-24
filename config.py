import twitter

# yourKey = token -> https://developer.twitter.com/en/docs/twitter-api

def getApi():
    return twitter.Api(consumer_key='yourKey',
                    consumer_secret='yourKey',
                    access_token_key='yourKey',
                    access_token_secret='yourKey')
