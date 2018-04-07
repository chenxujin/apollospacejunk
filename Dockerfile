FROM python:3.6-stretch

MAINTAINER charles@charlesreid1.com

VOLUME ["/bot"]

RUN apt-get update && apt-get install git
RUN git clone https://github.com/charlesreid1/rainbow-mind-machine.git /rmm
RUN git clone https://github.com/charlesreid1/apollospacejunk.git /apollo

COPY ./bot/apikeys.py /apollo/bot/apikeys.py
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

CMD ["/usr/bin/env","python","ApolloBotFlock.py"]

# command above will be passed as argument to entrypoint
ENTRYPOINT ["/entrypoint.sh"]

