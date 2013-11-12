#!/usr/bin/python
#Dixon's Random square algorithm 
import numpy as np
import fractions
import math	

def verifyBsmooth(num,n):
	B = [-1,2,3,5,7,11,13,17,19,23,29,31] # 12 elementes 
	a =[0]*len(B)
	if (num**2 %n < n/2): num = num**2 %n; 
	else: num = -(n-(num**2 %n)) ; 
	
	if num<0 : 
		a[0]=1
		num = -num
	for i in range(1,11):
		while (num%B[i]==0):		
			a[i]=a[i]+1
			num = num/B[i]
	if (num==1): 
		'''for i in range(len(a)):
			a[i] = a[i]%2'''
		return (True,a)
	else: return (False,a)
	
if __name__=="__main__":
	
	n = 256961
	# set the range of test number
	min = 500 
	max = int(math.sqrt(5*n))
	
	count = 0 # let's say that we need 16 equations (12 + 4)
	A = []  # coefficient list
	Num =[] # chosen x
	
	for i in range(min,max):
		success, a_i = verifyBsmooth(i,n)
		if success and count <16: 
			count = count + 1
			print a_i
			print i
			A.append(a_i)
			Num.append(i)
	
	print A[6]; print A[7]
	print Num[6]; print Num[7]
	# We find A[6], A[7]
	# calculate the two factors
	z = 531*561 % n ; y = (2**4)*(5**3)*19 %n
	k = fractions.gcd(z+y,n); l = fractions.gcd(y-z,n)
	print "z: %d, y: %d" %(z,y)
	print "k: %d, l: %d" %(k,l)
	
