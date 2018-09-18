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
    the math shenanigans is to deal with the fact that it is too easy to overflow ascii, so convert to simple a=0
    then do the mod then add the numbers back, should probably split it up
    :param input_string: the string to be coded
    :return: the ciphered text, as well as the pad
    """
    # input_string = input_string
    # pad_string = generate_pad(len(input_string))
    pad_string = 'hnbqemcpzbnrzlevkokffou'
    # pad_string = 'poop'
    cipher_text = []
    cipher_pad = []
    for i in range(0, len(input_string)):
        cipher_text.append(ord(input_string[i]))
        cipher_pad.append(ord(pad_string[i]))
        cipher_text[i] = chr((int(cipher_text[i]) ^ int(cipher_pad[i])))
    # print(cipher_text)
    print(''.join(cipher_text), pad_string)
    return cipher_text, cipher_pad


# def decode():


def generate_pad(count):
    """
    generates long string of lowercase ascii chars
    :param count: the number of chars
    :return: a string filled with random lowercase ascii chars
    """
    return ''.join(random.choices(string.ascii_lowercase, k=count))


encode("I love Computer Science")
