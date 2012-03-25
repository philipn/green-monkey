import sys

from utils import module_exists

from gevent import monkey


def make_django_green():
    monkey.patch_all()

    if module_exists('psycogreen'):
        from psycogreen.gevent.psyco_gevent import make_psycopg_green
        make_psycopg_green()

    if module_exists('pymysql'):
        import pymysql
        pymysql.install_as_MySQLdb()

    if module_exists('zmq'):
        from gevent_zeromq import zmq
        sys.modules["zmq"] = zmq
