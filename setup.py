from setuptools import setup

setup(name='mailmanager',
      version='0.1',
      description='Postfix, Dovecot and Postgres configuration made easy',
      url='http://github.com/gipi/mailmanager',
      author='Gianluca Pacchiella',
      author_email='gp@ktln2.org',
      license='GPLv3',
      packages=['mailmanager'],
      scripts=['bin/mailmanager'],
      install_requires=[
        'docopt',
        'psycopg2',
        'peewee',
        'jinja2',
      ],
      zip_safe=False)
