#!/usr/bin/env python

from struct import Struct

# short int short short int (native, unsigned)
s = Struct('=ccIHHI')  # <1>

with open('../DATA/chimp.bmp', 'rb') as chimp_in:
    chimp_bmp = chimp_in.read(s.size)  # <2>

(sig1, sig2, size, reserved1, reserved2, offset) = s.unpack(chimp_bmp)  # <3>

print("signature:", (sig1 + sig2).decode())  # <4>
print('size:', size)
print('reserved1:', reserved1)
print('reserved2:', reserved2)
print('offset:', offset)
