# Vernam / One-time pad cypher
import random
import string


def encode(input_string):
    """
    function to execute OTP cipher encoding, by converting to binary, xoring and then converting back
    the conversions are harder then the actual algorithm tbh
    :param input_string: the string to be encoded
    :return: the cipher and the pad
    """
    input_string = input_string.lower().replace(' ', '')
    binary_string = (' '.join(format(ord(x), 'b') for x in input_string)).replace(' ', '')
    # print(input_string, binary_string)

    pad_string = (generate_pad(len(input_string))).replace(' ', '')
    binary_pad = (' '.join(format(ord(x), 'b') for x in pad_string)).replace(' ', '')
    # print(pad_string, binary_pad)

    cipher_text = ''
    for i in range(0, len(binary_string)):
        if int(binary_string[i]) + int(binary_pad[i]) == 1:
            cipher_text += '1'
        else:
            cipher_text += '0'
    print(cipher_text)

    output_string = ''
    for i in range(0, len(cipher_text), 8):
        # todo: convert cipher text back to string
        output_string += chr(int(cipher_text[i:i+8], base=2))
    print(output_string)
    return cipher_text, pad_string


def generate_pad(count):
    """
    generates a list of ascii letters, lowercase
    :param count: the number of letters
    :return: the l chars as 1 string
    """
    return ''.join(random.choices(string.ascii_lowercase, k=count))


encode("I love Computer Science")
