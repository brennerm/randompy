import random
import string
import datetime


class PyRandom:
    @staticmethod
    def string(length, chars='', uppercase=True, lowercase=True, digits=True):

        if chars == '':
            chars += string.ascii_uppercase if uppercase else ''
            chars += string.ascii_lowercase if lowercase else ''
            chars += string.digits if digits else ''

        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def integer(minimum, maximum, even=False, odd=False):
        if minimum > maximum:
            print('minimum can\'t be greater than maximum')
            return

        if even is True and odd is True:
            print('setting even and odd flag to True is not allowed')
            return

        def check_value(value):
            if even:
                if (value % 2) != 0:
                    return False

            if odd:
                if not (value & 0x1):
                    return False
            return True

        while True:
            value = random.randint(minimum, maximum + 1)
            if check_value(value):
                return value

    @staticmethod
    def array(source, selection_size=1, duplicates=True):
        if not duplicates and len(source) < selection_size:
            print('unable to select ' + str(selection_size) + ' elements from a list of size ' + str(len(source)))
            return

        selected_elements = []
        for i in range(selection_size):
            selected_element = random.choice(source)
            selected_elements.append(selected_element)
            if not duplicates:
                source.remove(selected_element)

        return selected_elements

    @staticmethod
    def datetime(start=datetime.datetime(year=1970, month=1, day=1), end=datetime.datetime(year=2050, month=1, day=1)):
        delta = end - start
        delta_microseconds = (delta.days * 86400000000) + (delta.seconds * 1000000) + delta.microseconds

        microseconds = PyRandom.integer(0, delta_microseconds)
        return start + datetime.timedelta(microseconds=microseconds)

    @staticmethod
    def mail(length_local=7, length_domain=5, domain_ending='com'):
        if length_local > 64:
            print('local part can\'t be longer than 64 characters')
            return
        if (length_local + length_domain + len(domain_ending)) > 254:
            print('mail address can\'t be longer than 2544 characters')

        return PyRandom.string(length_local) + '@' + PyRandom.string(length_domain) + '.' + domain_ending

    @staticmethod
    def ipv4address():
        return '.'.join([str(PyRandom.integer(0, 255)) for _ in range(4)])

    @staticmethod
    def ipv6address():
        return ':'.join('{:x}'.format(PyRandom.integer(0, 65535)) for _ in range(8))