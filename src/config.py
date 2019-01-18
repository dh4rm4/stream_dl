import os, string, random

class Config(object):
    SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(42))
