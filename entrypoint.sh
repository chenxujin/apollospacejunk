#!/bin/sh

cd /rmm
/usr/bin/env pip install -r requirements.txt
/usr/bin/env python setup.py build
/usr/bin/env python setup.py install

cd /apollo/bot
exec "$@"
