FROM charlesreid1/rainbowmindmachine
MAINTAINER charles@charlesreid1.com

RUN git clone https://github.com/charlesreid1/apollospacejunk.git /apollo

WORKDIR "/apollo/bot"

CMD ["/usr/bin/env","python","ApolloBotFlock.py"]

