import random
import string as st
import datetime as dt


def string(length, chars='', uppercase=True, lowercase=True, digits=True):
    if chars == '':
        chars += st.ascii_uppercase if uppercase else ''
        chars += st.ascii_lowercase if lowercase else ''
        chars += st.digits if digits else ''

    return ''.join(random.choice(chars) for _ in range(length))


def integer(minimum, maximum, even=None):
    if minimum > maximum:
        raise ValueError('Minimum must not be bigger than maximum')

    def check_value(val):
        if even is True:
            if (val % 2) != 0:
                return False

        if even is False:
            if not (val & 0x1):
                return False
        return True

    while True:
        value = random.randint(minimum, maximum)
        if check_value(value):
            return value


def array(source, selection_size=1, duplicates=True):
    if not duplicates and len(source) < selection_size:
        raise ValueError('unable to select ' + str(selection_size) + ' elements from a list of size ' + str(len(source)))

    selected_elements = []
    for i in range(selection_size):
        selected_element = random.choice(source)
        selected_elements.append(selected_element)
        if not duplicates:
            source.remove(selected_element)

    return selected_elements


def datetime(start=dt.datetime(year=1970, month=1, day=1), end=dt.datetime(year=2050, month=1, day=1)):
    delta = end - start
    delta_microseconds = (delta.days * 86400000000) + (delta.seconds * 1000000) + delta.microseconds

    microseconds = integer(0, delta_microseconds)
    return start + dt.timedelta(microseconds=microseconds)


def mail(length_local=7, length_domain=5, domain_ending='com'):
    if length_local > 64:
        raise ValueError('local part must not be longer than 64 characters')

    if (length_local + length_domain + len(domain_ending)) > 254:
        raise ValueError('mail address must not be longer than 254 characters')

    return string(length_local) + '@' + string(length_domain) + '.' + domain_ending


def mac_address():
    return ':'.join('{:02x}'.format(integer(0, 255)) for _ in range(6))


def ipv4address():
    return '.'.join([str(integer(0, 255)) for _ in range(4)])


def ipv6address():
    return ':'.join('{:04x}'.format(integer(0, 65535)) for _ in range(8))
