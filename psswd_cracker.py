import hashlib
import itertools

def crack_password(hash_value):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for length in range(1, 9):
        for combination in itertools.product(characters, repeat=length):
            password = "".join(combination)
            hash_object = hashlib.sha256(password.encode('utf-8'))
            hashed_password = hash_object.hexdigest()
            if hashed_password == hash_value:
                return password
    return None
