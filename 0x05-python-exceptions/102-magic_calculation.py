#!/usr/bin/python3

class TooFarException(Exception):
    pass


def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise TooFarException("Too far")
            else:
                result += (a ** b) / i
        except TooFarException:
            result = b + a
            break
    return result


# import dis
# dis.dis(magic_calculation)
