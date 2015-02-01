Title: "Scraping the Apollo 12 Flight Journal: Python, BeautifulSoup, and Mechanize" 
Date: 2015-01-29 18:15
Category: 

## Scraping the Apollo Flight Journals

I wanted to iterate through each day of the [transcripts of the Apollo 12 flight logs](http://www.hq.nasa.gov/office/pao/History/ap12fj/)
(i.e., the radio dialogue from the Apollo 12 mission), and extracting the text using a Python web scraper.

That text is then parsed to break dialogue up into sentences,
and match dialogue with speakers, all of which is then exported
as a JSON file for olipy, a random text generation library for Python.

This would all be used to create bots that would generate new, fake, 
but plausible random Apollo radio chatter, by chopping up the dialogue
and serving up a remix.

This is the purpose of olipy, which requires a JSON file that looks like this: [apollo 11.txt](https://raw.githubusercontent.com/leonardr/olipy/master/data/apollo_11.txt) 

A series of lines of the form:

```
 {
  "tokens": [
   "Where are we going?"
  ],
  "speaker": "Conrad",
  "time": "000:24:00"
 },
 {
  "tokens": [
   "AC Bus 1 light, all the fuel cells ... "
  ],
  "speaker": "Conrad",
  "time": "000:25:00"
 },
 {
  "tokens": [
   "Altitude a mile and a half now.",
   "Velocity 1,592 feet per second."
  ],
  "speaker": "Public Affairs Office",
  "time": "000:26:00"
 }
```

All of this will allow us to make the [Apollo 12 Space Junk twitterbot](http://twitter.com/apollo12) (now created),
a sister of the [Apollo 11 Space Junk twitterbot](http://twitter.com/apollo11junk).

## TL;DR

Here's the links to the finished products, if you want to follow along, or skip everything:

* [apollo 12.txt](https://raw.githubusercontent.com/charlesreid1/wordswordswords/master/apollo12/data/apollo_12.txt) - finished product, parsed JSON text of the Apollo 12 flight journals

* [apollo 12 scrapeit.py](https://github.com/charlesreid1/wordswordswords/tree/master/apollo12) - the Python script utilizing BeautifulSoup and Mechanize that I am walking you through on this post.

## Scraping with Python

I decided to use [Mechanize](http://wwwsearch.sourceforge.net/mechanize/),
just cuz I wanted to learn how.

I used [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) 
cuz it's a breeze.

I was interested in extracting the text from each of the 10 days listed on the 
Apollo 12 Flight Journal page. So I fired up mechanize and BeautifulSoup:

### Getting Each Log Day Page 

The first bit of the script obtains the HTML 
of the main page. This is where the links to each 
day are, and we can iterate through links to find
links whose text contains "Day ".

```python
import mechanize 
from bs4 import BeautifulSoup

base_link = 'http://www.hq.nasa.gov/office/pao/History/ap12fj/'

base_page = 'index.htm'

browser = mechanize.Browser()
headers=[('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')]
browser.addheaders = headers
resp = browser.open(base_link+base_page)

html_doc = resp.read()
```

Next is iterating through all the links with the soup object:

```python
soup = BeautifulSoup(html_doc)
a_s = soup.find_all('a')

log_links = []
for a_ in a_s:
    link_text = a_.get_text()
    if 'Day ' in link_text:
        page_name = a_.attrs['href']
        link_name = base_link+page_name
        log_links.append(link_name)

# follow those links!!!
```

## A Whole Bunch of Crummy Low-Level Text Wrangling

I had to do a bunch of nonsense to get the text
properly encoded and decoded, namely, find and replace
ascii characters like 1/2, single and double quotes,
emdashes and endashes, etc.

## Sentence Tokenization with NLTK

Now we can start using the [Natural Language Toolkit (nltk)](http://www.nltk.org/)
to parse the text:

```python
    import nltk

    # tokenize by sentence:
    tokens = nltk.tokenize.sent_tokenize(booty)
```

I then did some cleaning up of the tokens, to split at colons and hyphens
(delineating speakers from dialogue).

### Speakers and Dialogue

Now I get to the hard part: parsing who says what.

I started by defining all the speakers:

```python
    speakers = [
        'Public Affairs Office',
        'SC',
        'MS',
        'Carr',
        'Conrad',
        'Gordon',
        'Gibson',
        'Bean',
        'ARIA',
        'MS',
        'SC',
        'Weitz',
        'Lind'
        ]
```

Next, some regular expression magic to get rid of timestamps 
appearing next to speakers' names:

```python
    # replace timestamps 000:00:00
    # look for "last updated" location
    #
    last_updated_index = 0
    for jj,tok in enumerate(tokens):

        if any([speaker in tok for speaker in speakers]):

            stripped_tok = re.sub('[0-9]{3}:[0-9]{2}:[0-9]{2} ','',tok)
            stripped_tok2 = re.sub('at [0-9]{3}:[0-9]{2}:[0-9x]{2}','',stripped_tok)
            stripped_tok3 = re.sub(' \(onboard\)','',stripped_tok2)
            tokens[jj] = stripped_tok3
        
        if 'last updated' in tok.lower():
            last_updated_index = jj
    
    if last_updated_index <> 0:
        tokens[0:last_updated_index+1] = []
```

The last step is to put all this information into a 
Python dictionary, with keys "speaker", "tokens",
and "time". I'm generating a fake timestamp, 
incremented by one minute with each line of 
dialogue, since timestamps aren't used consistently
through the flight journal, and so long as order is 
preserved, aren't as important to the text generation process.

```python
    ii = 0
    while ii < len(tokens):
        if tokens[ii] in speakers:
            d = {}
            d['speaker'] = tokens[ii]
            ii += 1
            z = []
            while (ii<len(tokens)) and (comm_break not in tokens[ii].lower()) and (tokens[ii] not in speakers):
                z.append(tokens[ii])
                ii += 1
            d['tokens'] = z

            cc = len(all_the_dialogue)
            if ((mm+1)%60)==0:
                mm=0
            if ((cc+1)%60)==0:
                hh += 1

            d['time'] = '%03d:%02d:00'%(hh,mm)
            all_the_dialogue.append(d)
            mm += 1

        ii += 1

```

You can see that I am compiling a Python list containing 
each of those dictionaries. Once I'm done, I can dump
that whole list into a file with the JSON dumps function,
which dumps the list to a string:

```python
import json

with open('data/apollo_12.txt','w') as f:
    for d in all_the_dialogue:
        f.write(json.dumps(d))
        f.write("\n")
```

which results in this output:

```
{"tokens": ["Two minutes, 20 seconds and counting at this time.", "Two minutes, 10 seconds at this time.", "We see that the stages are now beginning to pressurize as our countdown proceeds.", "Coming up on the 2 minute mark in the count.", "T minus 2 minutes and counting, T minus 2.", "Spacecraft commander now has placed the environmental control system of the spacecraft on internal.", "Up to this time we have been providing external sources for the environmental control system.", "We're checking the hydraulics of the first stage of the launch vehicle now.", "We are still Go.", "One minute, 40 seconds and counting at this time.", "T minus 90 seconds and counting, T minus 90, still Go.", "Our status board here in firing room 2 indicates all is still well with the countdown.", "Third stage tanks now pressurized as the automatic sequence continues."], "speaker": "Public Affairs Office", "time": "000:08:00"}
{"tokens": ["Lift-off.", "The clock's running."], "speaker": "Conrad", "time": "000:09:00"}
{"tokens": ["Six seconds."], "speaker": "Bean", "time": "000:10:00"}
{"tokens": ["Clear the tower."], "speaker": "Gordon", "time": "000:11:00"}
{"tokens": ["Pete Conrad reports the yaw program is in.", "Tower clear."], "speaker": "Public Affairs Office", "time": "000:12:00"}
{"tokens": ["Roger, Pete."], "speaker": "Carr", "time": "000:13:00"}
{"tokens": ["It's a lovely lift-off.", "It's not bad at all.", "[Pause.]"], "speaker": "Conrad", "time": "000:14:00"}
{"tokens": ["Everything's looking great.", "Sky's getting lighter."], "speaker": "Gordon", "time": "000:15:00"}
{"tokens": ["Thirty seconds."], "speaker": "Bean", "time": "000:16:00"}
{"tokens": ["Roll's complete."], "speaker": "Conrad", "time": "000:17:00"}
{"tokens": ["Roger, Pete.", "[Pause.]"], "speaker": "Carr", "time": "000:18:00"}
```

I can even print it out all nice and pretty like:

```python
with open('data/apollo_12_pretty.txt','w') as f:
    json.dump(all_the_dialogue,f,indent=1)
```
which results in this:

```
 {
  "tokens": [
   "Two minutes, 20 seconds and counting at this time.", 
   "Two minutes, 10 seconds at this time.", 
   "We see that the stages are now beginning to pressurize as our countdown proceeds.", 
   "Coming up on the 2 minute mark in the count.", 
   "T minus 2 minutes and counting, T minus 2.", 
   "Spacecraft commander now has placed the environmental control system of the spacecraft on internal.", 
   "Up to this time we have been providing external sources for the environmental control system.", 
   "We're checking the hydraulics of the first stage of the launch vehicle now.", 
   "We are still Go.", 
   "One minute, 40 seconds and counting at this time.", 
   "T minus 90 seconds and counting, T minus 90, still Go.", 
   "Our status board here in firing room 2 indicates all is still well with the countdown.", 
   "Third stage tanks now pressurized as the automatic sequence continues."
  ], 
  "speaker": "Public Affairs Office", 
  "time": "000:08:00"
 }, 
 {
  "tokens": [
   "Lift-off.", 
   "The clock's running."
  ], 
  "speaker": "Conrad", 
  "time": "000:09:00"
 }, 
 {
  "tokens": [
   "Six seconds."
  ], 
  "speaker": "Bean", 
  "time": "000:10:00"
 }, 
 {
  "tokens": [
   "Clear the tower."
  ], 
  "speaker": "Gordon", 
  "time": "000:11:00"
 }, 
 {
  "tokens": [
   "Pete Conrad reports the yaw program is in.", 
   "Tower clear."
  ], 
  "speaker": "Public Affairs Office", 
  "time": "000:12:00"
 }, 
 {
  "tokens": [
   "Roger, Pete."
  ], 
  "speaker": "Carr", 
  "time": "000:13:00"
 }, 
 {
  "tokens": [
   "It's a lovely lift-off.", 
   "It's not bad at all.", 
   "[Pause.]"
  ], 
  "speaker": "Conrad", 
  "time": "000:14:00"
 }, 
 {
  "tokens": [
   "Everything's looking great.", 
   "Sky's getting lighter."
  ], 
  "speaker": "Gordon", 
  "time": "000:15:00"
 }, 
 {
  "tokens": [
   "Thirty seconds."
  ], 
  "speaker": "Bean", 
  "time": "000:16:00"
 }, 
 {
  "tokens": [
   "Roll's complete."
  ], 
  "speaker": "Conrad", 
  "time": "000:17:00"
 }, 
 {
  "tokens": [
   "Roger, Pete.", 
   "[Pause.]"
  ], 
  "speaker": "Carr", 
  "time": "000:18:00"
 }, 
```

In any case, the end result is a brand-new file, apollo_12.txt, 
which is in just the right format to feed to olipy!

Here's the link to the final product, apollo_12.txt: [https://raw.githubusercontent.com/charlesreid1/wordswordswords/master/apollo12/data/apollo_12.txt](https://raw.githubusercontent.com/charlesreid1/wordswordswords/master/apollo12/data/apollo_12.txt)

In a future post I'll cover my script for feeding this JSON file to olipy
to make an Apollo 12 Space Junk bot. That script is available on Github 
at [apollo12_olipy.py](https://github.com/charlesreid1/wordswordswords/tree/master/apollo12).

