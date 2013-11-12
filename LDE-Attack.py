#!/usr/bin/python

import math
import numpy as np

# Eulidean algorithm 
def gcd(a,b):
	Q=[]
	while b != 0:
		t = b;
		q = a/b
		b = a % b
		a = t;
		Q.append(q)
	return Q  

if __name__=="__main__":
	
	n = 317940011; b = 77537081
	Q = gcd(b,n)
	C=[];D=[]
	C.append(1);C.append(0);
	D.append(0);D.append(1);
	a_max = math.sqrt(math.sqrt(n))/3
	
	for i in range (2,len(Q)+1):
		C.append(C[i-1]*Q[i-1] +C[i-2])
		D.append(D[i-1]*Q[i-1] +D[i-2])
		n_prime = (D[i]*b -1)/C[i]
		print C[i-1]*Q[i-1] +C[i-2] 
		print D[i-1]*Q[i-1] +D[i-2]
		print n_prime
		print n_prime - n
		print "..........."		
	
	P = [1,-(n-317902032+1),n]
	roots = np.roots(P)
	print roots
	print Q
	print a_max
	
