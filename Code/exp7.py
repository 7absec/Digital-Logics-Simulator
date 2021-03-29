#Booths algorithm:
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()


def continue_():
    ans=input("\nDo you want to continue(y/n)? : ").capitalize()
    if ans=='Y':
        selector7()
    elif ans=="N":
        exit()
    else:
        print("Please enter a valid option")
        continue_()

# Takes an integer and returns it's binary equivalent as string type:
def binary(no):
	bi=[]
	binary='0'
	while no!=0:
		remainder = no%2
		no = no//2
		bi.append(remainder)
	for _ in range(len(bi)-1,-1,-1):
		binary = binary+str(bi[_])
	return binary	

# Takes binary number as a string and returns it's two's compliment as string type:
def twosComp(no):
	swap=0
	ans=''
	for _ in range(len(no)-1,-1,-1):
		if swap==1:
			if no[_]=='0':
				ans = ans + '1'
			else:
				ans = ans + '0'	
		else:
			ans = ans + no[_]
			if no[_]=='1':
				swap=1
	return ans[::-1]

# Takes two binary numbers as strings and returns their binary sum as string type:
def add(x,y):
	maxlen = max(len(x),len(y))
	x = x.zfill(maxlen)
	y = y.zfill(maxlen)
	result=''
	carry=0

	for i in range(maxlen-1,-1,-1):
		sum = int(x[i])+int(y[i])
		if sum == 2:
			if carry == 1:
				result+='1'
				carry=1
			else:
				result+='0'
				carry=1
		elif sum == 1:
			if carry == 1:
				result+='0'
				carry=1
			else:
				result+='1'
		elif sum == 0:
			if carry ==1:
				result+='1'
				carry=0
			else:
				result+='0'
	if carry==1:
		# result+='1'	#Carry is discarded
		pass 		
	return result[::-1]

#A function to rightshift:
def rightShift(no):
	ans=''
	for i in range(0,len(no)-1):
		ans = ans+no[i]
	return ans

#Taking inpus from user:
def selector7():
	print("\t\t\t\t/------------------------------\ ")
	print("\t\t\t\t      EXPERIMENT NUMBER: 7  ")
	print("\t\t\t\t\------------------------------/")
	print("\n\t\t\tTo impliment BOOTH'S ALGORITHM")
	print("\t\t\__________________________________________________________/")
	print("\n\t/------------------------\ ")
	print("\t BOOTH'S ALGORITHM")
	print("\t\------------------------/ ")
	print("Please enter the Multiplicant and Multiplier::")
	M = int(input("\tEnter the multiplicant(M):"))
	Q = int(input("\tEnter the multiplier(Q):"))
	if M < 0:  # in case of negative M:
		binary_m = twosComp(binary(abs(M)))
		neg_m = binary(abs(M))
	else:
		binary_m = binary(M)
	# neg_m = twosComp(binary_m)
	if Q < 0:
		binary_q = twosComp(binary(abs(Q)))
	else:
		binary_q = binary(Q)
	maxlen = max(len(binary_m), len(binary_q))
	binary_m = binary_m.zfill(maxlen)
	binary_q = binary_q.zfill(maxlen)
	neg_m = twosComp(binary_m)
	AC = '0'
	AC = AC.zfill(maxlen)
	Q_1 = '0'
	steps = maxlen
	print('\n\tStep=0' + '\tAC=' + AC + '\tQ=' + binary_q + '\tI=' + Q_1 + '\tM=' + binary_m)
	for _ in range(0, steps):
		if binary_q[-1] + Q_1[-1] == '01':
			AC = add(AC, binary_m)
			Q_1 = binary_q[-1]
			binary_q = AC[-1] + rightShift(binary_q)
			AC = AC[0] + rightShift(AC)

		elif binary_q[-1] + Q_1[-1] == '10':
			AC = add(AC, neg_m)
			Q_1 = binary_q[-1]
			binary_q = AC[-1] + rightShift(binary_q)
			AC = AC[0] + rightShift(AC)

		elif binary_q[-1] + Q_1[-1] in ('00', '11'):
			Q_1 = binary_q[-1]
			binary_q = AC[-1] + rightShift(binary_q)
			AC = AC[0] + rightShift(AC)

		print('\tStep=' + str(_ + 1) + '\tAC=' + AC + '\tQ=' + binary_q + '\tI=' + Q_1 + '\tM=' + binary_m)

	print('\n\tBinary Answer = (' + AC + binary_q + ')2\n\tDecimal Answer =', int(M * Q))
	continue_()