import os
import string
import base64
from hashlib import sha256

class BaseCommand(object):
    need_database = False

    # lines below from https://bitbucket.org/tarek/bugbro/src/b042d7640067/bugbro/util.py
    _SALT_LEN = 8

    def randchar(self, chars=string.digits + string.letters):
        pos = int(float(ord(os.urandom(1))) * 256. / 255.)
        return chars[pos % len(chars)]

    def _gensalt(self): 
        """Generates a salt"""
        return ''.join([self.randchar() for i in range(self._SALT_LEN)])

    def ssha256(self, password, salt=None):
        """Returns a Salted-SHA256 password"""
        if salt is None:   
            salt = self._gensalt()
        ssha = base64.b64encode(sha256(password + salt).digest()
                                   + salt).strip()
        return "%s" % ssha


    def __call__(self, *args):
        self.handle(*args)
