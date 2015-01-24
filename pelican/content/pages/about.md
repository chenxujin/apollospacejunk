Title: About 
PageStyle: well
save_as: about.html

## What is a Twitter Bot?

A Twitter bot is a computer program that automatically generates
tweets, and interfaces with Twitter to send out those tweets.

<br />

## What is a Bot Flock?

A Bot Flock is a set of Twitter bots who tweet together.
All bots in the bot flock are tweeting similar things or
are interacting with one another.

<br />

<a href="https://twitter.com/charlesreid1/lists/space-junk-botflock" class="btn btn-primary btn-large">Visit the Apollo Space Junk Bot Flock on Twitter</a>

<br />


## What is special about the Apollo Space Junk bot flock?

The Apollo Space Junk bots are robots that create a nd publish tweets.
But the tweets they create
are randomly generated. These bots learn how to speak by being given
a large corpus of dialogue,
and constructs new dialogue by repeating and re-using 
language at the phrase level,
instead of the letter- or word-level that is used in a lot of
random text generation algorithms (e.g., the [Markov model of language](http://www.cs.princeton.edu/courses/archive/spr05/cos126/assignments/markov.html)).
What this allows you to do is generate phony random text 
with the same "look-and-feel" as the original.

<blockquote class="twitter-tweet" lang="en"><p>McCandless: Go ahead, 11. And I&#39;d like to pass up your Delta azimuth correction at this time if you&#39;re ready to copy.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/551686395681452032">January 4, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Evans: Apollo 11, Houston. Just about, though. We got about 2 minutes to LOS here, Mike. Over.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/551443999626915841">January 3, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[leonardr on github](http://github.com/leonardr/olipy) has done all the hard work
of writing the algorithm to train and generate language on the phrase level, 
called Queneau assembly, in a Python library
calleld [olipy](http://github.com/leonardr/olipy).
He also came up with an ingenious application -
he put all of the dialogue of the Apollo 11
flight and ground radio transmissions into
JSON format, easily parsed by olipy, and packaged
it all up as an elegant 10-line script, 
[example.apollo.py](https://github.com/leonardr/olipy/blob/master/example.apollo.py).

I've taken his lead and done the same to the Apollo 12 flight logs, as described in this blog post:

* [Scraping the Apollo 12 Flight Journal: Python, BeautifulSoup, and Mechanize](http://charlesreid1.github.io/blog/2015/01/05/python-scraping-the-apollo-12-flight-journal/)

Because the space junk buts take unaltered sentences straight from the original dialogue,
creating anew by mashing them together in new combinations, 
it presents a very interesting way to experience the history in those logs 
and peek into them in random and often fascinating flashes that 
might otherwise not see the light of day. 

<blockquote class="twitter-tweet" lang="en"><p>Boston out hit Baltimore to score 6 runs to the Orioles&#39; 2; and Chicago beat Kansas City 6 to 1. Loud and clear. It looks okay to us.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/550302963311181825">December 31, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The language the space junk bots use is the language of the astronauts and Mission Control.

<blockquote class="twitter-tweet" lang="en"><p>Collins: I said the Czar is brushing his teeth, so I&#39;m filling in for him. Good.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305959511789569">January 6, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Collins: Let me know when it&#39;s lunch time, will you?</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/550850060582281217">January 2, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

What I love best about it is how densely, thickly technical
the transcrips are, dipping into them at any point,
and yet in so many places the humanity of the astronauts
comes through. The space junk bots take on a personality 
all their own.

<blockquote class="twitter-tweet" lang="en"><p>Over.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548438294191554560">December 26, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Armstrong: (Joking) You can&#39;t get away with anything anymore, can you? Yes, it&#39;s about a second off.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548438652507152384">December 26, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

They weave together barely coherent, yet just-plausible-enough, dialogue,
like an astronaut's waking dream. Entire miniature 
dramas play out over long radio transmissions. 

<blockquote class="twitter-tweet" lang="en"><p>McCandless: There we go, the salmon salad, very good. Reading you loud and clear. One thing that we did miss in the drop-out in the noise</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305204193161216">January 6, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>on panel 251 also. Roll for Sep 357, 107, 041; 301, 287, 319. [No answer.] The feature that I was describing to you - the small bright</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305205946368001">January 6, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

So much of what happens on board the spacecraft consists of routine checks, 
communication tests, diagnosing problems, reading off instruments, changing settings -
the dull routine tasks of the most exciting job in the universe.

The dialogue recycles, so if you keep watching long enough, you'll see the same problems crop up again forever. 

Then again, when you spend ten days in space, lots of problems crop up. So you might be watching a while.

<blockquote class="twitter-tweet" lang="en"><p>Duke: Houston. About 50 percent of the time, we&#39;re getting high bit rate off the omnis when you&#39;re in PTC. Copy, 11. [Long pause.] Copy.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548621624699011073">December 26, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Collins: That&#39;s affirmative.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548621859910975488">December 26, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

On an imaginary circumlunar trajectory, forever.

<blockquote class="twitter-tweet" lang="en"><p>Aldrin: Hey, Charlie, I can see the snow on the - on the mountains out in California, and it looks like LA doesn&#39;t have much of a smog</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163502605864960">January 5, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>problem today. Minus 50 and 270.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163503029501953">January 5, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Collins: See that, Buzz?</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163884207861761">January 5, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Aldrin: Roger.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163999903514626">January 5, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p>Armstrong: Yes.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552164326107148288">January 5, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


