import sys

from gevent import monkey

from utils import module_exists


def patch_all():
    monkey.patch_all()

    if module_exists('psycogreen'):
        from psycogreen.gevent.psyco_gevent import make_psycopg_green
        make_psycopg_green()

    if module_exists('pymysql'):
        import pymysql
        pymysql.install_as_MySQLdb()

    if module_exists('gevent_zeromq'):
        from gevent_zeromq import zmq
        sys.modules["zmq"] = zmq

    if module_exists('pylibmc'):
        import memcache
        sys.modules["pylibmc"] = memcache
