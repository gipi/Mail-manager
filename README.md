THIS IS NOT READY FOR PRODUCTION!!! YOUR SERVER WILL BLOW UP!!!


## INSTALLATION

     $ python setup.py install# soon a deb package
     $ mailmanager init --db-user userdb \
        --db-name maildb --db-passwd dbpasswd

this last command save in the .mailmanager/ directory a
configuration file with the credentials useful to connect
to the mail database.

It'a also possible to generate the configuration files

     # mailmanager conf | tar xf - -C /

## CONFIGURATION

The configuration file is created with the ``init`` command and
should contain the following variables

    username
    password
    dbname
    tablename

that will be passed to the requested template when rendered.

## TEST

 $ vagrant up
 $ vagrant ssh
