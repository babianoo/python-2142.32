import hashlib

def hash_passwrd(pw):
    """
    Returns the SHA-256 hex digest of the 'passwd'
    """
    data = pw.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

print(hash_passwrd("saba"))