#!/usr/bin/env python

from struct import Struct

name = "Guido"

values = 7, 6, 42.3, b'Guido' # <1>

demo = Struct('iif10s')  # <2>

print("Size of data: {} bytes".format(demo.size)) # <3>

binary_stream = demo.pack(7, 6, 42.3, name.encode()) # <4>

print(f"binary_stream: {binary_stream}")

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # <5>
str1 = raw_bytes.decode().rstrip('\x00')  # <6>

print(raw_bytes)
print(int1, int2, float1, str1)

print(f"bin(int1): {bin(int1)}")  #  hex()  oct() bin()

