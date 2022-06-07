import re

def decode_protocol(message):
    return [message[0:5], message[5:6], message[6:10], message[10:]]

def is_valid_protocol(message):
    return bool(re.match(regex_protocol(), message))

def regex_protocol():
    return '^\d{5}(.)\d{4}(.){1,30}'
    