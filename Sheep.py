import twitter
import time
import simplejson as json
from numpy.random import rand

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

"""
Uses bear's python-twitter library from Github
(official version of what was the Google Code python-twitter):
https://github.com/bear/python-twitter
"""

class SpecialException(Exception):
    pass

class Sheep(object):
    """
    Sheep does three things:
    - communicates with twitter api
    - tweets
    - keeps track of age/# cycles
    """
    def __init__(self,json_file,line_interval,total_interval):

        self.line_interval = line_interval
        self.total_interval = total_interval

        # sheep require a JSON with keys
        with open(json_file, "r") as f:
            self.params = json.load(f)

        # self.params keys:
        # - oauth_token_secret
        # - oauth_token
        # - user_id
        # - screen_name
        # - consumer_token_secret
        # - consumer_token
        # - myfile

        # sheep interface with twitter
        self.setup_api()

        # sheep has memory, which is a list of tokens
        # (lines, or sentences, however we tokenize the file.)
        self.memory = []
        self.memorize()

        # sheep can sleep
        self.sleeping = False

        # tot tweet tracker for total lifetime
        # mod tweet tracker for mod N (N = number of lines, which changes with time)
        self.tot_tweet_tracker = 0
        self.mod_tweet_tracker = 0


    def setup_api(self):
        """
        Create Twitter API instance from our input params
        """
        print "Setting up API for bot "+self.params['screen_name']
        self.api = twitter.Api( consumer_key        = self.params['consumer_token'],
                                consumer_secret     = self.params['consumer_token_secret'],
                                access_token_key    = self.params['oauth_token'],
                                access_token_secret = self.params['oauth_token_secret'])



    def memorize(self):
        """
        Memorize a file
        (i.e. read it into list called memory)
        """
        ## Keep it simple for now.
        ## One-liner straight-shot list comprehension.
        #self.memory = [line.strip() for line in open(self.params['file'])]
        #
        ## Prune empty lines
        #self.memory = [mem for mem in self.memory if mem <> ""]
        self.memory = [""]



    def loop(self):
        """
        Do this forever
        """
        while True:
            try: 
                self.tweet_something()
                self.sleep()
            except:
                print "Uh oh! Sheep "+self.params['screen_name']+" ran into a problem."
                time.sleep(1000)



    def sleep(self):
        """
        Take a nap
        """
        self.sleeping = True

        # If we've finished the file, longer wait.
        # If we're just between lines, shorter wait.

        if (self.mod_tweet_tracker == 0 and self.tot_tweet_tracker > 0):
            time.sleep(self.total_interval)

        else:
            time.sleep(self.line_interval)

        self.sleeping = False



    def tweet_something(self):
        """
        Come up with something clever to say,
        and then tweet it!

        This is what the Shepherd calls.
        """
        self.tweet( self.memory[self.mod_tweet_tracker] )



    def test_tweet(self):
        """
        Tweet hello world + a random favorite number
        """
        txt = "Hello world! My favorite number is %d"%( round(1000*rand()) )
        self.tweet(txt)



    def tweet(self,txt):
        """
        Really tweet!
        """
        #if self.params['screen_name']=='gbf_supermarket':
        #    print self.params['screen_name']
        #    print txt
        #    print
        try:
            # tweet:
            stats = self.api.PostUpdates(txt)

            # everything else:
            for stat in stats:
                print "[Bot "+self.params['screen_name']+"]: "+stat.text

        except twitter.TwitterError as e:
            if e.message[0]['code'] == 185:
                print "[Bot "+self.params['screen_name']+"] Twitter error: Daily message limit reached"
            elif e.message[0]['code'] == 187:
                print "[Bot "+self.params['screen_name']+"] Twitter error: Duplicate error"
            else:
                print "[Bot "+self.params['screen_name']+"] Twitter error"
                print e.message

        self.increment_tweet_counters()
        self.check_age()



    def increment_tweet_counters(self):
        """
        Increment tweet counters by 1
        """
        self.mod_tweet_tracker += 1
        self.tot_tweet_tracker += 1



    def check_age(self):
        """
        Figure out if we've finished tweeting our file
        """
        if (self.mod_tweet_tracker) % len(self.memory) == 0 \
        and self.tot_tweet_tracker > 0:

            # we've finished tweeting our file

            # reset mod tweet tracker 
            self.mod_tweet_tracker = 0

            # happy birthday
            print "~*"*6 + " Happy birthday "+self.params['screen_name'] + " " + "~*"*6




    def lobotomy(self):
        """
        Sheep can delete their whole history and pretend like
        none of this ever happened. 

        Deletes every tweet.
        """
        for j in self.api.GetUserTimeline(self.params['screen_name'],count=100):
            print "Destroying status:"
            print j.text
            self.api.DestroyStatus( j.id )
        self.mod_tweet_tracker = 0
        self.tot_tweet_tracker = 0

