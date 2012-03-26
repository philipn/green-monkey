green-monkey
============

Use green versions of all possible modules.  For use with gevent.

.. image:: http://mathburritos.org/misc/greenmonkey.png

Install & Usage
---------------

``pip install green-monkey`` or, from source, ``python setup.py
install``

In addition to installing ``green_monkey``, this will install green versions
of all possible modules.

Then place the following::

    import green_monkey
    green_monkey.patch_all()

somewhere *before* any of your normal imports or code.

You'll now be using green versions of all modules and the standard
library will be patched. You can think of this as an extension of
``monkey.patch_all()`` beyond the standard library.


Example: greening Django project
--------------------------------

For instance, in a standard WSGI handler for Apache you might do something
like this::

    import os, sys
    sys.path.append('/usr/local/django')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    import green_monkey
    green_monkey.patch_all()
    
    import django.core.handlers.wsgi
    
    application = django.core.handlers.wsgi.WSGIHandler()

Or in a Gunicorn config, you might do something like this::

    bind = "127.0.0.1:"
    workers = 3
    worker_class = "gevent"
    
    def def_post_fork(server, worker):
        import green_monkey
        green_monkey.patch_all()
    
    post_fork = def_post_fork

and now your Django project is *probably* green!

In general, it's not possible to automatically green an arbitrary 
codebase, as it may do something like call an external C library which
blocks.  But for many projects this will work well -- *especially* for largely
self-contained bits of code, e.g. event handlers in ``django-socketio``.
