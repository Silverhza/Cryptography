#!/usr/bin/python

ciphertext = "\
dwxrellvrjeowgznoxlcjnvwkhurtxtpyrhlzcerwhvcbhvfabhgil\
zofgiglcguibjsaqituvpuegywattesqrjmmzhunxpzwpukhwgorjh\
jsvawxiiraxmgwynpexcejekvgqbghfhrahgshvimmqcapibfhurqt\
abbspbyvgpvtozfgsfshhemmqkurvxowgufxabtpvhobqpvhgyrqiv\
dwcfilyovawmzwftphjmsvkaloaqxbesguemyoirhhlvabaaagtvjm\
ucassnfrgvqxvcguxksbfsmqlvrsphmfvfllwhbachmhunrwvsyiil\
lvrcekszyrplaborenlmfovhotrrhlgbguiksfvgmxkcsaemmfrfxk\
mhunrwfcgumgyggnrwkphgjhjvvfwvqhurxhecjnrwqsggsmaarfmg\
zccrqrnsefilzoyywmsbqcvtagvakmzmjbvmzrrftblsuvwvjiryltfr\
"
ll = len(ciphertext)
numberloop = ll/12
Y0 = list(ciphertext)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
y11 = []
y12 = []

for x in range(0, numberloop):
	y1.append(Y0[x*12+0])
	y2.append(Y0[x*12+1])
	y3.append(Y0[x*12+2])
	y4.append(Y0[x*12+3])
	y5.append(Y0[x*12+4])
	y6.append(Y0[x*12+5])
	y7.append(Y0[x*12+6])
	y8.append(Y0[x*12+7])
	y9.append(Y0[x*12+8])
	y10.append(Y0[x*12+9])
	y11.append(Y0[x*12+10])
	y12.append(Y0[x*12+11])
	
P = []
def	setProb (sublist):
	P.append(sublist.count('a')/40.0)
	P.append(sublist.count('b')/40.0)
	P.append(sublist.count('c')/40.0)
	P.append(sublist.count('d')/40.0)
	P.append(sublist.count('e')/40.0)
	P.append(sublist.count('f')/40.0)
	P.append(sublist.count('g')/40.0)
	P.append(sublist.count('h')/40.0)
	P.append(sublist.count('i')/40.0)
	P.append(sublist.count('j')/40.0)
	P.append(sublist.count('k')/40.0)
	P.append(sublist.count('l')/40.0)
	P.append(sublist.count('m')/40.0)
	P.append(sublist.count('n')/40.0)
	P.append(sublist.count('o')/40.0)
	P.append(sublist.count('p')/40.0)
	P.append(sublist.count('q')/40.0)
	P.append(sublist.count('r')/40.0)
	P.append(sublist.count('s')/40.0)
	P.append(sublist.count('t')/40.0)
	P.append(sublist.count('u')/40.0)
	P.append(sublist.count('v')/40.0)
	P.append(sublist.count('w')/40.0)
	P.append(sublist.count('x')/40.0)
	P.append(sublist.count('y')/40.0)
	P.append(sublist.count('z')/40.0)
	
	
setProb(y1)		


print P  
		
