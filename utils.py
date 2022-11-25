from hashlib import md5


def get_hash(password):
    hasher = md5()
    hasher.update(password)
    return hasher.hexdigest()
