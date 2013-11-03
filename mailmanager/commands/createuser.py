from .base import BaseCommand

class Command(BaseCommand):
    need_database = True

    def handle(*args):
        userid, domain = args[0].split("@")
        user = Users.create(
            userid=userid,
            domain=domain,
            home="%s/%s/" % (userid, domain,),
            password=ssha256(args[1]),
            uid=8,
            gid=8
        )
        user.save()
