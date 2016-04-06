import time

#How long will it take?

# fibonacci 1

def fib1(p):
	if p <= 1:
		return 1

	else: 
		return fib1(p-1)+fib1(p-2)

#fibonacci 2

def fib2(p):
	a = 1
	b = 1

	for x in range(1, p):
		a = a+b
		b = a-b

	return a


#Laufzeitmessung

print('I want to know the fibonacci sequenz of:')
a = int(input())

t1fb1 = time.clock()
rfb1 = fib1(a)
t2fb1 = time.clock()

t1fb2 = time.clock()
rfb2 = fib2(a)
t2fb2 = time.clock()

tfb1 = t2fb1 - t1fb1
tfb2 = t2fb2 - t1fb2

print('The fibonacci sequenz of ' + str(a) + ' is ' + str(rfb1) )
print('It takes ' + str(tfb1) + ' seconds to calculate the fibonacci sequenz of ' + str(a) + ' with the first code')
print('It takes ' + str(tfb2) + ' seconds to calculate the fibonacci sequenz of ' + str(a) + ' with the second code')

