import gmpy2
import threading
#	Performs a meet in the middle attack on weak discrete log parameters
# i.e this finds x such that h=g^x in Zp (Zp is the cyclic group)
# Completed as part of Dan Boneh's online cryptography class
# data
p	=	13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g	=	11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h	=	3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
B 	=	2 ** 20 # the middle of 2^40 possible combinations

class TableThread(threading.Thread):
	def __init__(self, low, high):
		super(TableThread, self).__init__()
		self.low = low
		self.high = high
		self.table = []

	def run(self):
		base = gmpy2.invert(g,p)
		for x in range(self.low, self.high):
			self.table.append(gmpy2.f_mod(h*gmpy2.powmod(base,x,p),p))

class SearchThread(threading.Thread):
	def __init__(self, low, high):
		super(SearchThread, self).__init__()
		self.low = low
		self.high = high
		self.X0 = 0
		self.X1 = 0

	def run(self):
		for x0 in range(self.low, self.high):
			check = gmpy2.powmod(g,B*x0,p)
			if check in table:
				self.X1 = table.index(check)
				self.X0 = x0



# build the left hand side table of values
thread1 = TableThread(0,131072)
thread2 = TableThread(131072,262144)
thread3 = TableThread(262144,393216)
thread4 = TableThread(393216,524288)
thread5 = TableThread(524288,655360)
thread6 = TableThread(655360,786432)
thread7 = TableThread(786432,917504)
thread8 = TableThread(917504,1048576)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

table = thread1.table + thread2.table + thread3.table + thread4.table + thread5.table + thread6.table + thread7.table + thread8.table

print "table done"
print len(table)

threadA = SearchThread(0,131072)
threadB = SearchThread(131072,262144)
threadC = SearchThread(262144,393216)
threadD = SearchThread(393216,524288)
threadE = SearchThread(524288,655360)
threadF = SearchThread(655360,786432)
threadG = SearchThread(786432,917504)
threadH = SearchThread(917504,1048576)

threadA.start()
threadB.start()
threadC.start()
threadD.start()
threadE.start()
threadF.start()
threadG.start()
threadH.start()

threadA.join()
threadB.join()
threadC.join()
threadD.join()
threadE.join()
threadF.join()
threadG.join()
threadH.join()

print "X0: " + threadA.X0
print "X1: " + threadA.X1
print "X0: " + threadB.X0
print "X1: " + threadB.X1
print "X0: " + threadC.X0
print "X1: " + threadC.X1
print "X0: " + threadD.X0
print "X1: " + threadD.X1
print "X0: " + threadE.X0
print "X1: " + threadE.X1
print "X0: " + threadF.X0
print "X1: " + threadF.X1
print "X0: " + threadG.X0
print "X1: " + threadG.X1
print "X0: " + threadH.X0
print "X1: " + threadH.X1
