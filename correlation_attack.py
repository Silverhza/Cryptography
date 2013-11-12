#!/usr/bin/python

def generate_X(init_x,N):
   # 3 registers for x
   X = init_x
   x_0 = X[0]
   x_1 = X[1]
   i = 0
   while(len(X)<N):
	   x_3 = (x_0 + x_1)%2
	   X = X +[x_3]
	   i+=1
	   x_0 = X[i]
	   x_1 = X[i+1] 
	   
   return X

def generate_Y(init_y,N):
   # 4 registers for y
   Y = init_y
   y_0 = Y[0]
   y_3 = Y[3]
   i = 0
   while(len(Y)<N):
	   y_4 = (y_0 + y_3)%2
	   Y = Y +[y_4]
	   i+=1
	   y_0 = Y[i]
	   y_3 = Y[i+3] 
	   
   return Y
   
def generate_Z(init_z,N):
   # 5 registers for z
   Z = init_z
   z_0 = Z[0]
   z_2 = Z[2]
   i = 0
   while(len(Z)<N):
	   z_5 = (z_0 + z_2)%2
	   Z = Z +[z_5]
	   i+=1
	   z_0 = Z[i]
	   z_2 = Z[i+2] 
	   
   return Z

def generate_K1(X,Y,Z):
	K1 = []
	for i in range(len(X)):
		k_temp = (X[i]*Y[i]+Y[i]*Z[i]+Z[i])%2
		K1.append(k_temp)
	return K1

P_X = 0.75
P_Y=0.5
P_Z=0.75
K=[0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0]
Length_K = len(K)


init_x = [0,1,0]     # 010
init_y = [1,0,1,0]   # 1010 (when z =11001, no y matches with k)
init_z = [1,0,1,0,1] # 10101/11001

X = generate_X(init_x, Length_K)
Y = generate_Y(init_y, Length_K)
Z = generate_Z(init_z, Length_K)
K1 = generate_K1(X, Y, Z) # look for the correct initial value for y
print Z
print K1

count_x = 0 ; count_z = 0 ; count_k1 = 0
for i in range(Length_K):
	if(X[i] == K[i]):
		count_x+=1
	if(Z[i] == K[i]):
		count_z+=1	
	if (K1[i] == K[i]):
		count_k1+=1	
print "correlation attack : #of x ->%d, #of z ->%d"%(count_x,count_z)
print "# of matches between K1 and K is %d"%count_k1
	

