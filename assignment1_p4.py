__author__ = 'jim027@ucsd.edu, A99075314, siz001@ucsd.edu, A99076798, yuc036@ucsd.edu, A91112915'

import sys

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

def inlist(toBeCheck, position):
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
				if inlist(listOfPrimes, temp) == False and isprime(temp):
					listOfPrimes.append(temp)    
		else: 
			tempindex = index + 1
			temp = (temp / (10 ** tempindex)) * (10 ** tempindex) + (temp % (10 ** index))
			print ("HERE IS: %d" %temp)
			origin = temp
			for loop in range(0, 10):
				print(loop)
				temp = origin + loop * (10 ** index)
				print("here is: %d" %temp)
				if inlist(listOfPrimes, temp) == False and isprime(temp):
					listOfPrimes.append(temp)
		temp = currentPrime
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
	while queue1 and queue2:
		keyS = queue1.keys().pop(0)
		pathS = queue1[keyS]
		visitedS.add(keyS)
		childrenS = getPossibleActions(keyS)
		del queue1[keyS]
		if keyS in queue2:
			str2 = ' '.join(map(str,[finalPrime] + pathS[::-1]))
			str1 = ' '.join(map(str,[startingPrime] + pathS))
			return str1 + '\n' + str2
		for elemS in childrenS:
			if elemS not in visitedS and elemS not in addedS:
				queue1[elemS] = pathS+[elemS]
				addedS.add(elemS)
		keyF = queue2.keys().pop(0)
		pathF = queue2[keyF]
		visitedF.add(keyF)
		childrenF = getPossibleActions(keyF)
		del queue2[keyF]
		if keyF in queue1:
			str2 = ' '.join(map(str,[finalPrime] + pathF))
			str1 = ' '.join(map(str,[startingPrime] + pathF[::-1]))
			return str1 + '\n' + str2
		for elemF in childrenF:
			if elemF not in visitedF and elemF not in addedF:
				queue2[elemF] = pathF+[elemF]
				addedF.add(elemF)
	return "UNSOLVABLE"

def main():
	primes = str(sys.stdin.readline()).split()
	print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
