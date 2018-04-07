FROM python:3.6-stretch

MAINTAINER charles@charlesreid1.com

#RUN apt-get update && apt-get install git

RUN git clone https://github.com/charlesreid1/rainbow-mind-machine.git /rmm
RUN cd /rmm && \
    /usr/bin/env pip install -r requirements.txt && \
    /usr/bin/env python /rmm/setup.py build && \
    /usr/bin/env python /rmm/setup.py install

RUN git clone https://github.com/charlesreid1/apollospacejunk.git /apollo

WORKDIR "/apollo/bot"

CMD ["/usr/bin/env","python","ApolloBotFlock.py"]

