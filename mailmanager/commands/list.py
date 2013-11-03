from .base import BaseCommand
from .models import Users

class Command(BaseCommand):
    def handle(self):
        users = Users.select()
        for u in users:
            print "%s@%s\t%s\t%s" % (u.userid, u.domain, u.home, u.password,)
