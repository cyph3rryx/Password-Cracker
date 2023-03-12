import hashlib

def crack_password(hash_value, dictionary_file):
    with open(dictionary_file, 'r') as f:
        for line in f:
            password = line.strip()
            hash_object = hashlib.sha256(password.encode('utf-8'))
            hashed_password = hash_object.hexdigest()
            if hashed_password == hash_value:
                return password
    return None
