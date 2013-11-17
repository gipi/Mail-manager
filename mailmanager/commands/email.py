from .base import BaseCommand
from .models import Users, init_db


class Command(BaseCommand):
    """
    Manages the emails. The available commands are
    
        list
        add    user@domain password
    """
    def handle(self, *args, **kwargs):
        params = self.get_configuration_params()

        init_db(
            params['username'],
            params['password'],
            params['dbname'],
        )

        if kwargs.has_key('list') and kwargs['list']:
            self.list()
        elif kwargs.has_key('add') and kwargs['add']:
            if len(kwargs['OPTIONS']) < 2:
                self.error(self.__doc__)
            self.add(kwargs['OPTIONS'][0], kwargs['OPTIONS'][1])

    def list(self):
        print 'email\thome'
        for user in Users.select():
            print '%s@%s\t%s'  % (
                user.userid,
                user.domain,
                user.home,
            )

    def add(self, email, password):
        username, domain = email.split('@')
        Users.create(
            domain=domain,
            userid=username,
            home='%s/%s' % (domain, username),# make 'home' configurable
            password=self.ssha256(password),
        )

        print 'created mail \'%s\'' % email
