__author__ = 'jim027@ucsd.edu, A99075314, siz001@ucsd.edu, A99076798, yuc036@ucsd.edu, A91112915'

import sys
import time

""" function to check if a number is a prime or not """
def isprime(n):
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True

def inlist(toBeCheck,position):
	try:
		result = toBeCheck.index(position)         
	except ValueError:
		return False
	else:
	 	return True
	
def getPossibleActions(currentPrime):
	listOfPrimes = []
	temp = currentPrime

	numOfDigit = len(str(currentPrime))	
	temp = currentPrime
	
	for index in range(0, numOfDigit):
		if index == numOfDigit - 1: 
			temp = temp % (10 ** index)
			for loop in range (1,10):
				temp = temp + (10 ** index)
				if isprime(temp) and inlist(listOfPrimes, temp) == False:
					listOfPrimes.append(temp)    
		else: 
			tempindex = index + 1
			temp = (temp / (10 ** tempindex)) * (10 ** tempindex) + (temp % (10 ** index))
			origin = temp
			for loop in range(0, 10):
				temp = origin + loop * (10 ** index)
				if isprime(temp) and inlist(listOfPrimes, temp) == False:
					listOfPrimes.append(temp)
		temp = currentPrime
	#listOfPrimes.reverse()
	return listOfPrimes

def getPath(startingPrime, finalPrime):
	startingPrime = int(startingPrime)
	finalPrime = int(finalPrime)
	queue1 = {startingPrime: []}
	queue2 = {finalPrime: []}
	visitedS = set()
	visitedF = set()
	addedS = set([startingPrime])
	addedF = set([finalPrime])
	if isprime(startingPrime) == False or isprime(finalPrime) == False:
		return "UNSOLVABLE"
	while queue1 and queue2:
		ilist = list(set(queue1.keys()) & set(queue2.keys()))
		if ilist:
			keyS = ilist.pop(0)
			str2 = ' '.join(map(str,[finalPrime] + queue2[keyS]))
			str1 = ' '.join(map(str,[startingPrime] + queue1[keyS]))
			return str1 + '\n' + str2
		else:
			for keyS in queue1.keys():
				visitedS.add(keyS)
				childrenS = getPossibleActions(keyS)
				for elemS in childrenS:
					if elemS not in visitedS and elemS not in addedS:
						queue1[elemS] = queue1[keyS] + [elemS]
						addedS.add(elemS)
				del queue1[keyS]
			slist = list(set(queue1.keys()) & set(queue2.keys()))
			if slist:
				keyS = slist.pop(0)
				str2 = ' '.join(map(str,[finalPrime] + queue2[keyS]))
				str1 = ' '.join(map(str,[startingPrime] + queue1[keyS]))
				return str1 + '\n' + str2
			else: 
				for keyF in queue2.keys():
					visitedF.add(keyF)
					childrenF = getPossibleActions(keyF)
					for elemF in childrenF:
						if elemF not in visitedF and elemF not in addedF:
							queue2[elemF] = queue2[keyF] + [elemF]
							addedF.add(elemF)
					del queue2[keyF]		
	return "UNSOLVABLE"

def main():
	primes = str(sys.stdin.readline()).split()
	start = time.time()
	print(getPath(primes[0],primes[1]))
	end = time.time()
	timer = end - start
	print("time elapsed is %d" % timer)

if __name__ == '__main__':
	main()
