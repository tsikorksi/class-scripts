# Vernam / One-time pad cypher
# for juheb:
# cipher text = pamezqprnnclspvicqsjsqy
# pad = hnbqemcpzbnrzlevkokffou
import random
import string


def encode(input_string):
    """
    i gave up on binary, so here is the vernam cipher with ords and ascii
    https://en.wikipedia.org/wiki/One-time_pad#Example
    Note: copy pasting the returned result is hard, since it is often weird chars from the bottom of the ascii table
    :param input_string: the string to be coded
    :return: the ciphered text, as well as the pad
    """
    # pad_string = generate_pad(len(input_string))
    # this is the secret pad which is shared with the other user
    pad_string = 'hnbqemcpzbnrzlevkokffou'
    # the orded message
    cipher_text = []
    # the orded pad
    cipher_pad = []
    for i in range(0, len(input_string)):
        # add the ascii value to an array
        cipher_text.append(ord(input_string[i]))
        # add the ascii value to the other array
        cipher_pad.append(ord(pad_string[i]))
        # ord them and convert back to chars
        cipher_text[i] = chr((int(cipher_text[i]) ^ int(cipher_pad[i])))
    # make a string of the chars
    print(''.join(cipher_text), pad_string)
    return cipher_text, cipher_pad


def generate_pad(count):
    """
    generates long string of lowercase ascii chars
    :param count: the number of chars
    :return: a string filled with random lowercase ascii chars
    """
    return ''.join(random.choices(string.ascii_lowercase, k=count))


encode("I love Computer Science")
