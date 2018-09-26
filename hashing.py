# Hashing algorithm in MD5

import hashlib


def generate_hash(password, salt):
    """
    takes in a password (string) and hashes it in both md5 and sha256, salting it with generic salt 'salt', but feel
    free to change that
    :param salt: the salt
    :param password: the text to be hashed
    :return: both the hashes
    """
    # encode the password/salt in utf-8
    bytes_string = password.encode(encoding='utf-8')
    salt = salt.encode(encoding='utf-8')

    # creates hash objects
    hash_md5 = hashlib.md5()
    hash_sha256 = hashlib.sha256()

    # hashes salt and password in the 2 formats
    hash_md5.update(salt + bytes_string)
    hash_sha256.update(salt + bytes_string)

    # returns the hex-digest eg the format you most commonly see
    print(hash_md5.hexdigest())
    print(hash_sha256.hexdigest())

    return hash_sha256, hash_md5


def hash_comparing(key):
    """
    takes a key, and hashes it in md5, attempting a encode to utf-8, but if the object is already utf-8, will continue
    :param key: the object to be hashed
    :return: the hash
    """
    # the try except block will not stop the process if the object happens to already be in utf-8
    try:
        key = key.encode(encoding='utf-8')
    except AttributeError:
        pass
    iteration = hashlib.md5()
    iteration.update(key)
    return iteration


def comparison(test_hashes):
    """
    compares list of hashes to first 10000 4 digit password combinations
    :param test_hashes: the password hashes tested against, or the ones being cracked
    :return: all hashes found
    """
    # neat little bit of python which fills an array with the passwords form 0000 to 9999
    hashes = ['{0:04}'.format(num) for num in range(0, 9999)]

    hashed = []

    # convert the above list to the format matching the input
    for i in range(0, len(hashes)):
        hashed.append(str(hash_comparing(hashes[i]).hexdigest().upper()))

    # linear search
    found = []
    for j in range(0, len(hashed)):
        if hashed[j] in test_hashes:
            found.append(hashes[j])

    # neat formatting to get the passwords back
    for i in range(0, len(found)):
        next_print = str(found[i])
        while len(next_print) < 0:
            next_print = '0' + next_print
        print(next_print)

    return found


def file_digest(file):
    """
    generates a digest of a file
    :param file: the filename to be hashed
    :return: the digest of the hash
    """
    # 'rb' file mode reads the file as bytes
    input_file = open(file, 'rb')
    data = input_file.read()
    # getting the digest
    digest = hash_comparing(data).hexdigest()
    input_file.close()
    return digest


passwords = ['B8002139CDDE66B87638F7F91D169D96', '7EA25C95B0792CA4CE01EA18BBDA2D44', 'D39934CE111A864ABF40391F3DA9CDF5',
             '024D2D699E6C1A82C9BA986386F4D824', 'D77C703536718B95308130FF2E5CF9EE', '67606D48E361CE176CA71FD54FCF4286',
             'B29EED44276144E4E8103A661F9A78B7', '109D2DD3608F669CA17920C511C2A41E', '64D52E08CC03E6090BC1EF30B73CCB85',
             'E643B33B3019892367371B27BC0E63C2']

file_digest('testfile.txt')
