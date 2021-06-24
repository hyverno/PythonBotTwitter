
# Here we import all the libraries we need as well as the file where our tokens are saved

from typing import Text
from config import getApi
import sys
import twitter
api = twitter.Api()

from RandomWordGenerator import RandomWord

# rw = random word -> we need different comments to post a tweet, that's why I generate a 5 letters word, to bypass the anti-spam system of twitter.

rw = RandomWord(max_word_size=5)
print(rw.generate())

api = getApi()

# place here your twitte that you want to publish.

TwitteThat = "https://store.steampowered.com/app/1575870/UpGun/ "

# The twitte is executed with the variable filled in previously and the word aleatoir.

status = api.PostUpdate(TwitteThat + rw.generate())
print(status.text)
