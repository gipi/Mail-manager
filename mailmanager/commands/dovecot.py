from .base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args):
        print self.render_template(
            'dovecot-sql.conf',
            self.get_configuration_params())
