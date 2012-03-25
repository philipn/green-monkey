A utility function to green Django for gevent usage.

.. image:: http://mathburritos.org/misc/greendjango.png

``pip install green-django`` or, from source, ``python setup.py
install``

Then place the following::

    from green_django import make_django_green
    make_django_green()

somewhere *before* any of your Django imports or code.  For instance, in a
standard WSGI handler for Apache you might do something like this::

    import os, sys
    sys.path.append('/usr/local/django')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    from green_django import make_django_green
    make_django_green()
    
    import django.core.handlers.wsgi
    
    application = django.core.handlers.wsgi.WSGIHandler()

Or in a Gunicorn config, you might do something like this::

    bind = "127.0.0.1:"
    workers = 3
    worker_class = "gevent"
    
    def def_post_fork(server, worker):
        from green_django import make_django_green
        make_django_green()
    
    post_fork = def_post_fork

The aim of this project is to allow greening of *most* Django codebases.
We green all commonly used database adapters and third-party libraries.

In general, it's not possible to automatically green an arbitrary Django
codebase, as it may do something like call an external C library which
blocks.  But for many projects this will work -- *especially* for largely
self-contained bits of code, e.g. event handlers in ``django-socketio``.
