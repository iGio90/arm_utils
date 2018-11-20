import ctypes


def ands(a, b):
    return a & b


def add(a, b):
    return a + b


def asrs(a, b):
    return a >> b | 0xf0000000


def bic(a, b):
    r = a & ((-1 - b) << 8)
    r = (a & 0x00000ff) | r
    return r


def eor(a, b):
    return a ^ b


def lsl(a, b):
    a << b


def lsr(a, b):
    a >> b


def orr(a, b):
    return a | b


def ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))


def ror4(a, b):
    return ror(a, b, 32)


def rsb(a, b):
    return 0 - a + b


def smmul(a, b):
    a = ctypes.c_int32(a).value
    b = ctypes.c_int32(b).value
    return (a * b) >> 32


def sub(a, b):
    return a - b