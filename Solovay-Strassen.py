#!/usr/bin/python
# Solovay-Strassen primality test

import random
import fractions
import sys


#-------------------------------------------------------------------------------
def gcd(a,b):
	while b != 0:
		t = b;
		b = a % b; 
		a = t;
	return a

#-------------------------------------------------------------------------------
def isPrime(n,k):

	if n % 2 == 0: return False;
 	pow = (n-1)/2;

	for i in range(k):
	
		a = random.randint(1,n-1); # a is equal or greater than 1

	 	# modded by n to take care of the -1 case
	 	print "%d, %d, %d" %(i,n,a)
		x = jacobi(a,n) % n;
		if x==0: return False;

		y = (a**pow) % n;
		if y % n != x : return False;

	return True;

#-------------------------------------------------------------------------------
def calc2(num):

	# property 2: return 1 or -1
	if num % 8 == 3 or num % 8 == 5: return -1;
	else: return 1;

#-------------------------------------------------------------------------------
def jacobi(m,n):
	print "jacobi test"
	if gcd(m,n) != 1: return 0;
	negative = 1;

	while m > 1:
		
		# property 1 needs factoring
		# property 4: flip & mod 
		if n % 2 == 1 and m % 2 == 1:

			t = n; n = m; m = t;

			# test if negative
			m1 = n % 4;
			m2 = m % 4;

			if m1 == 3 and m2 == 3:
				negative *= -1;
			m = m % n;

		# property 3: see if we can extract a 2 
		elif m % 2 == 0:
			m = m/2;
			negative *= calc2(n);		

		else: 
			print "ERROR! degenerate case!";
		#print m
	print "test finished!"
	return negative;


#-------------------------------------------------------------------------------
def main():

	if(len(sys.argv) != 2):
		print "Usage: ss_prime <integer>"
	else:
		val = int(sys.argv[1])
		print isPrime(val,5)

#-------------------------------------------------------------------------------
# main function
if __name__ == "__main__":
    main()
    
