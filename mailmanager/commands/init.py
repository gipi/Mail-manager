import os
from .base import BaseCommand


class Command(BaseCommand):

    def _write_configuration_to_file(self, username, password):
        if os.path.exists(self._get_configuration_file_path()):
           self.error(
            "the configuration file at '%s' already exists" %
                self._get_configuration_file_path()) 
        else:
            with open(self._get_configuration_file_path(), 'wx') as f:
                # we want only to create the file
                pass

        with self._get_configuration_file() as f:
            f.write('''username=%s
password=%s
''' % (username, password))

    #TODO: hash password also in the config file
    def handle(self, *args):
        username = args[0]
        password = args[1]

        self._create_configuration_dir()

        self._write_configuration_to_file(username, password)
