#!/usr/bin/python

# "^"  = XOR
import itertools
import random
import threading, os, sys

S=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d_I = [8,4,2,1]


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        search_SBOX(self.name)
        print "Exiting " + self.name




def search_SBOX(threadName):	
         
            
	Diff_M = [[0 for i in range(16)] for j in range(16)]
	isfound= False
	count1=0
	count2=0
	
	while (not isfound):		
		PI_S = list(S)
		random.shuffle(PI_S)
		count1+=1
		if(count1%100000==0):print "%s : %d" %(threadName, count1)	
		#first criteria	
		if (PI_S[0]==S[0] or PI_S[1]==S[1] or PI_S[2]==S[2] or PI_S[3]==S[3]): continue
		elif (PI_S[4]==S[4] or PI_S[5]==S[5] or PI_S[6]==S[6] or PI_S[7]==S[7]): continue
		elif (PI_S[8]==S[8] or PI_S[9]==S[9] or PI_S[10]==S[10] or PI_S[11]==S[11]): continue
		elif (PI_S[12]==S[12] or PI_S[13]==S[13] or PI_S[14]==S[14] or PI_S[15]==S[15]): continue 
		
		#second criteria
		Diff_M = [[0 for i in range(16)] for j in range(16)]
		count = 0
		for j in range(len(S)):
			for k in range(len(S)):
				if (k==j): continue
				diff_x = S[j]^S[k]
				diff_y = PI_S[j]^PI_S[k]
				Diff_M[diff_x][diff_y]+=1		
		
		for j in range(len(S)):
			for k in range(len(S)):
				if (Diff_M[j][k]>4):
					count+=1 	
		#print count	
		if (count>0): isfound = False
		else: isfound = True
		
		if(not isfound): continue	
		
		#third criteria
		if (Diff_M[1][1]==0 and Diff_M[1][2]==0 and Diff_M[1][4]==0 and Diff_M[1][8]==0
		and Diff_M[2][1]==0 and Diff_M[2][2]==0 and Diff_M[2][4]==0 and Diff_M[2][8]==0
		and Diff_M[4][1]==0 and Diff_M[4][2]==0 and Diff_M[4][4]==0 and Diff_M[4][8]==0
		and Diff_M[8][1]==0 and Diff_M[8][2]==0 and Diff_M[8][4]==0 and Diff_M[8][8]==0):
			isfound = True
		else: isfound = False
	print PI_S
	os.exit(1)
	
			    
# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"			
																					
#print count1														



