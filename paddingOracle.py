#!/bin/python3
# Implements a padding oracle attack against a TOY remote encryption server in order to recover a key.
# Completed as part of Dan Boneh's online cryptography class
from binascii import unhexlify, hexlify
import urllib.request as Url
import sys

TARGET     = 'http://crypto-class.appspot.com/po?er='
CIPHERTEXT = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
BLOCKSIZE  = 32 # 32 chars for a 16 byteblock
LENGTH     = 128
PAD        = ['01', '0202', '030303', '04040404', '0505050505', '060606060606', '07070707070707', '0808080808080808', '090909090909090909', '0a0a0a0a0a0a0a0a0a0a', '0b0b0b0b0b0b0b0b0b0b0b', '0c0c0c0c0c0c0c0c0c0c0c0c', '0d0d0d0d0d0d0d0d0d0d0d0d0d', '0e0e0e0e0e0e0e0e0e0e0e0e0e0e', '0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f', '10101010101010101010101010101010' ]

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + Url.quote(q)      # Create query URL
        req = Url.Request(target)           # Send HTTP request to server
        try:
            f = Url.urlopen(req)            # Wait for response
        except Url.HTTPError as e:
            #print ("We got: %d" % (e.code)) # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    #my usual block splitting method
    blocks  = [ CIPHERTEXT[i:i+BLOCKSIZE] for i in range(0, LENGTH, BLOCKSIZE)]
    po = PaddingOracle()
    plain = ''
    for block in reversed(blocks[:1]):
        for pad in PAD:
            g = '00'
            while not po.query(CIPHERTEXT[:64].replace(block, hex(int(block, 16)^int(g+plain, 16)^int(pad, 16))[2:])):
                print('guessing: %s pad: %s' % (g+plain, pad), end='\n')
                g = hex(int(g, 16)+1)[2:]
            plain = g + plain
            print('\n' + plain)
    print(''.join(plain))
