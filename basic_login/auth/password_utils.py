import hashlib
import secrets
import string
def verify_hash_and_salt(user, password, parsed_json):
    hashed=parsed_json.get(user)
    hash, salt = hashed.split(':')
    userhashed=hashlib.sha256(f'{salt}{password}'.encode()).hexdigest()
    return userhashed == hash
def hash_and_salt(password):
    salt=secrets.token_hex(16)
    hashed=hashlib.sha256(f'{salt}{password}'.encode())
    return f"{hashed.hexdigest()}:{salt}"
def is_strong_password(password):
    if len(password)<8:
        return False
    elif not any(char in string.punctuation for char in password):
        return False
    elif not any(c.isdigit() for c in password):
        return False
    elif not any(c.isupper() for c in password):
        return False
    return True

