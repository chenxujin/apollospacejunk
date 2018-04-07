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
$ docker build -t apollobotflock .
```

This container expects to have a docker data volume 
mounted at `/bot`. Now you can run the container:

```
$ docker volume create apollo_data
$ doker run -d --name stormy_apollo -v apollo_data:/bot apollobotflock
```

(hopefully that's right, but in any case, just use docker-compose.)

The container should be run interactively the first time through
(add the `-it` flag to docker to make it interactive and give you tty),
so you can set up the keys. The keys will live next to the bot program
and `apikeys.py file`, in a folder called `keys/` containing one json file
per bot account.

On first run, the bot container will detect that there are no keys and 
run the interactive part of the script (Keymaker).

After the keys are set up, the bot container will detect that keys are present
and can run in detached mode.

##  Docker Compose

Running the bot with docker-compose is a three-step process.

The first step is to build the pod (one container).

```
$ docker-compose build
```

If you've made some changes to files copied into the 
container, specify the `--no-cache` flag or it will
continue to use the crusty version:

```
$ docker-compose --no-cache
```

First, to run the container interactively,
modify the docker-compose service `apollo_botflock`
to include `stdin_open: true` and `tty: true`:

```
  apollo_botflock:
    build: . 
    # ---------------
    # Only include these two lines 
    # when setting up API keys. 
    stdin_open: true
    tty: true
    # ---------------
```

Once those two lines are added, run the container
interactively using `docker-compose run` 
(do not use `up`!):

```
$ docker-compose run stormy_apollo
```

This will run the entrypoint script, install 
rainbow mind machine, and run the interactive 
script.

Once the keys are present, you can run the 
bot using `docker-compose up`, and `-d` to detach:

```
$ docker-compose up -d
```

Use this as a building block to create a
master `docker-compose.yml` running all the 
bot flocks.

## Rebuilding the Docker Container (Debugging)

If you end up doing debugging work,
and changes to files don't seem to have 
any effect, you may need to delete 
the data volume.

(Be advised, this will delete your API keys too!!)

```
$ docker ps -qa | xargs -n1 docker rm
$ docker volume rm bapollo_apollo_data  # DANGER!!!
```

