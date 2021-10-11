import base64
from urllib.parse import unquote, quote_plus

def decode_Url(u):
    return unquote(u)



def encode_Url(u):
    return quote_plus(u)


def base64_Encode(u):
    try:
        message_byte = u.encode('ascii')
        base64_byte = base64.b64encode(message_byte)
        base64_message = base64_byte.decode('ascii')
        return base64_message
    except:
        return "Not printable data"


def base64_Decode(u):
    try:
        base64_bytes = u.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        return message
    except:
        return "Not printable data"


def base32_Encode(u):
    try:
        base32_bytes = u.encode('ascii')
        message_bytes = base64.b32encode(base32_bytes)
        message = message_bytes.decode('ascii')
        return message
    except:
        return "Not printable data"


def base32_Decode(u):
    try:
        message_bytes = u.encode('ascii')
        base32_bytes = base64.b32decode(message_bytes)
        message = base32_bytes.decode('ascii')
        return message
    except:
        return "Not Printable data"



def base16_Encode(u):
    try:
        base16_bytes = u.encode('ascii')
        message_bytes = base64.b16encode(base16_bytes)
        message = message_bytes.decode('ascii')
        return message
    except:
        return "Not printable data"

def base16_Decode(u):
    try:
        base16_bytes = u.encode('ascii')
        message_bytes = base64.b16decode(base16_bytes)
        message = message_bytes.decode('ascii')
        return message
    except:
        return "Not Printable data"



