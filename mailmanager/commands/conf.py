from .base import BaseCommand
import sys
import tarfile
import StringIO


class Command(BaseCommand):
    """
    Print out a tar archive containing all the configuration file
    needed for your system.

    If the command find that the stdout is a tty, then alerts the user; the
    intended usage is to pipe with the tar command like

      $ mailmanager conf | tar xf - -C /"""
    def build_tarinfo(self, filepath, content):
        info = tarfile.TarInfo(filepath)
        fobject = StringIO.StringIO(content)
        info.size = len(fobject.buf)

        return {'tarinfo': info, 'fileobj': fobject}

    def handle(self, *args):
        if sys.stdout.isatty():
            self.error('a tty has been detected, probably you want to pipe this to \'tar xf - -C /your/path/\'')

        params = self.get_configuration_params()

        output = StringIO.StringIO()
        with tarfile.open(mode='w:', fileobj=output) as tar:
            tar.addfile(**self.build_tarinfo(
                '/etc/dovecot/dovecot.conf',
                self.render_template('dovecot.conf', params)))
            tar.addfile(**self.build_tarinfo(
                '/etc/dovecot/dovecot-sql.conf',
                self.render_template('dovecot-sql.conf', params)))
            tar.addfile(**self.build_tarinfo(
                '/etc/postfix/main.cf',
                self.render_template('main.cf', params)))
            tar.addfile(**self.build_tarinfo(
                '/etc/postfix/mailbox_domains.cf',
                self.render_template('mailbox_domains.cf', params)))
            tar.addfile(**self.build_tarinfo(
                '/etc/postfix/mailbox_maps.cf',
                self.render_template('mailbox_maps.cf', params)))

        print output.getvalue()
