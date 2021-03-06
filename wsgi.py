#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app

"""
建立一个软连接
ln -s /var/www/bootstrap/bootstrap.conf /etc/supervisor/conf.d/bootstrap.conf

ln -s /var/www/bootstrap/bootstrap.nginx /etc/nginx/sites-enabled/bootstrap.nginx



➜  ~ cat /etc/supervisor/conf.d/bbs.conf

[program:]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2001
--pid /tmp/blog.pid
"""