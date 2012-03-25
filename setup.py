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


setup(
    name='green-django',
    version='0.1',
    description='Utility function to green Django for gevent usage.',
    author='Philip Neustrom',
    author_email='philipn@gmail.com',
    url='http://github.com/philipn/green-django/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
