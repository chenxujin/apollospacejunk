# Apollo Space Junk

See [the project web page](http://charlesreid1.github.io/apollospacejunk) for more information,
or browse through the code.

This bot uses [rainbow mind machine](http://github.com/charlesreid1/rainbow-mind-machine), a Twitter bot library that I have authored.

```bot/``` contains the code for the Apollo Space Junk Twitter Bot Flock.

```pelican/``` contains the Pelican files used to generate [the project web page](http://charlesreid1.github.io/apollospacejunk).



## What Is It

queneau bot flock tweeting apollo mission dialogue

[@apollo11junk](https://twitter.com/apollo11junk)

[@apollo12junk](https://twitter.com/apollo12junk)

[@apollo13junk](https://twitter.com/apollo13junk)

## Required Software

This bot flock utilizes [rainbow-mind-machine](https://github.com/charlesreid1/rainbow-mind-machine),
the extensible bot flock framework authored by yours truly.

## Required Twitter Setup

You will need to set up some Twitter accounts for your bots, obviously.
Set up a new Gmail account, create a Google Voice number, and use that 
as a phone number if Twitter demands a phone number from you.
(Twilio phone numbers _will not work_ for Twitter registration. Don't blow $1.)

You will also need a bot-master account. This acount will be associated with
your application. You can have one bot-master that runs all of your bot flocks
under the same application, even if they are different flocks running on 
different machines.

You will need to create a Twitter app through the bot-master account.
This will give you a consumer token and a consumer secret token.

**Captain Obvious sez:** you should keep your consumer secret token a secret!

Once you have your consumer token and consumer secret, they go in `bot/apikeys.py`.
This step must be done prior to running the bot.

## Running The Bot Flock

Running the bot flock is a two-step process:

1. (One time) Authorize the program to tweet on behalf of your account 
    (i.e., log in with each user account). This requires `apikeys.py` be present
    next to your bot flock program. This step generates key files (JSON format).

2. Run the bot flock. Tweet! Sleep! Repeat!

## Docker

To run the bot flock using docker, use the Dockerfile
contained in this directory to build the container:

```
docker build -t apollobotflock .
```

This container expects to have a docker data volume 
mounted at `/bot`. Now you can run the container:

```
docker volume create apollo_data
doker run -d --name stormy_apollo -v apollo_data:/bot apollobotflock
```

(hopefully that's right, but in any case, just use docker-compose.)

The container should be run interactively the first time through,
so you can set up the keys. The keys will live next to the bot program
and `apikeys.py file`, in a folder called `keys/` containing one json file
per bot account.

##  Docker Compose

To run this bot in a container using docker-compose,
use the included `docker-compose.yml` file. 

The container should be run interactively the first time through,
so you can set up the keys. The keys will be inside the data volume,
`apollo_data` which will persist even if the container is stopped or destroyed.

Use this as a building block to create a
master docker-compose.yml running all the 
bot flocks.

## Rebuilding the Docker Container (Debugging)

If you end up doing debugging work,
and changes to files don't seem to have 
any effect, you may need to delete 
the data volume:

```
docker ps -qa | xargs -n1 docker rm
docker volume rm bapollo_apollo_data
```


