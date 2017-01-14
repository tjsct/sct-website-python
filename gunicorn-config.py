import os

bind = ['127.0.0.1:%s' % os.environ['PORT']]
workers = 2
worker_class = 'gevent'
proc_name = 'sct website'

