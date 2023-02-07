import hashlib
from django.conf import settings


def hash_md5(string):
    return hashlib.md5(string.encode()).hexdigest()