import itertools
import hashlib

def hybrid_attack(password_hash, dictionary_file, min_length, max_length, charset):
    """
    Hybrid attack.
    """
    with open(dictionary_file, 'r') as f:
        # Dictionary attack using common passwords
        for line in f:
            password = line.strip()
            hash_object = hashlib.sha256(password.encode('utf-8'))
            hashed_password = hash_object.hexdigest()
            if hashed_password == password_hash:
                return password

        # Brute-force attack using character set and specified length range
        for length in range(min_length, max_length+1):
            for combination in itertools.product(charset, repeat=length):
                password = ''.join(combination)
                hash_object = hashlib.sha256(password.encode('utf-8'))
                hashed_password = hash_object.hexdigest()
                if hashed_password == password_hash:
                    return password

    return None
