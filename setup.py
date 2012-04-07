from setuptools import setup, find_packages


def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

INSTALL_REQUIRES = ['gevent']

if module_exists('psycopg2'):
    INSTALL_REQUIRES.append('psycogreen')
    INSTALL_REQUIRES.append('psycopg2 >= 2.2.0')
if module_exists('MySQLdb'):
    # TODO: replace with ultramysql / umysql once someone adds a MySQLdb
    # wrapper around it.
    INSTALL_REQUIRES.append('PyMySQL')
if module_exists('zmq'):
    INSTALL_REQUIRES.append('gevent-zeromq')
if module_exists('pylibmc'):
    INSTALL_REQUIRES.append('python-memcached')


setup(
    name='green-monkey',
    version='0.1.2',
    description='Use green versions of all possible modules',
    author='Philip Neustrom',
    author_email='philipn@gmail.com',
    url='http://github.com/philipn/green-monkey/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',

    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
