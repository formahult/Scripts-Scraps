#!/bin/python3
# toy implementations of AES decryption functions in both counter
# (ctr) and cipher block chaining modes of operation
# Completed as part of Dan Boneh's online cryptography class

from Crypto.Cipher import AES, XOR

#datadatadatadatadatadatadatadatadatadatadatadatadatadatadatadata
cbcKey1 = bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
cbcMsg1	= bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")

cbcKey2	= bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
cbcMsg2	= bytes.fromhex("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")

ctrKey1	= bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
ctrMsg1	= bytes.fromhex("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")

ctrKey2	= bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
ctrMsg2	= bytes.fromhex("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")

#decrypt function
def cbcDecrypt(msg, key):
	# split into 16 byte blocks
	length, blockSize = len(msg), 16
	blocks 	= [ msg[i:i+16] for i in range(0, length, blockSize)]
	# First block is the IV, pull it out, the chain variable will be reused
	chain 	= blocks.pop(0)
	# Generate our crypto object
	crypto 	= AES.new(key, AES.MODE_ECB)
	plain 	= []
	for block in blocks:
		# Decrypt block, xor it with the previous link, append it to plaintext
		xor = XOR.new(chain)
		plain.append(str(xor.decrypt(crypto.decrypt(block)), encoding='utf-8'))
		chain = block
	plain = ''.join(plain)
	padLength = int.from_bytes(bytes(plain[len(plain)-1], encoding='utf-8'), byteorder='big')
	plain = plain[:len(plain)-padLength]
	return plain

def ctrDecrypt(msg, key):
	# split into 16 byte blocks
	length, blockSize = len(msg), 16
	blocks 	= [ msg[i:i+16] for i in range(0, length, blockSize)]
	# First block is the nonce, pull it out
	nonce 	= blocks.pop(0)
	# generat crypto object
	crypto 	= AES.new(key, AES.MODE_ECB)
	plain 	= []
	for block in blocks:
		# Create a new XOR object, using the encryption of the nonce as the key
		xor = XOR.new(crypto.encrypt(nonce))
		# XOR with the block
		plain.append(str(xor.decrypt(block), encoding='utf-8'))
		# You'd think incrementing some random bytes would be easy
		nonce = (int.from_bytes(nonce, byteorder='big') + 1).to_bytes(16, byteorder='big')
	plain = ''.join(plain)
	padLength = int.from_bytes(bytes(plain[len(plain)-1], encoding='utf-8'), byteorder='big')
	if padLength > blockSize:
		padLength = 0
	plain = plain[:len(plain)-padLength]
	return plain

def cbcEncrypt(msg, key):
	length, blockSize = len(msg), 16
	blocks 	= [ msg[i:i+16] for i in range(0, length, blockSize)]

def ctrEncrypt(msg, key):
	length, blockSize = len(msg), 16
	blocks 	= [ msg[i:i+16] for i in range(0, length, blockSize)]

print(cbcDecrypt(cbcMsg1, cbcKey1))
print(cbcDecrypt(cbcMsg2, cbcKey2))
print(ctrDecrypt(ctrMsg1, ctrKey1))
print(ctrDecrypt(ctrMsg2, ctrKey2))
