from hashlib import sha256
from string import ascii_letters
from random import choices


def hash_password(password: str, salt=None) -> tuple:
    if salt is None:
        salt = "".join(choices(ascii_letters, k=16))
    cipher = password + salt
    for _ in range(10):
        cipher = sha256(cipher.encode('utf-8')).hexdigest()
    return cipher, salt
