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

	
def getPossibleActions(currentPrime):
	listOfPrimes = set()
	temp = currentPrime

	numOfDigit = len(str(currentPrime))	
	temp = currentPrime
	
	for index in range(0, numOfDigit):
		if index == numOfDigit - 1: 
			temp = temp % (10 ** index)
			for loop in range (1,10):
				temp = temp + (10 ** index)
                		if isprime(temp) and temp not in listOfPrimes:
                    			listOfPrimes.add(temp)
		else: 
			tempindex = index + 1
			temp = (temp / (10 ** tempindex)) * (10 ** tempindex) + (temp % (10 ** index))
			origin = temp
			for loop in range(0, 10):
				temp = origin + loop * (10 ** index)
				if isprime(temp) and temp not in listOfPrimes:
					listOfPrimes.add(temp)
		temp = currentPrime

	return listOfPrimes

def getPath(startingPrime, finalPrime):
	startingPrime = int(startingPrime)
	finalPrime = int(finalPrime)
    	if isprime(startingPrime) == False or isprime(finalPrime) == False:
        	return "UNSOLVABLE"
    	if startingPrime == finalPrime:
        	return startingPrime
    	queue = {startingPrime: [startingPrime]}
	visited = set()
	added = set()
	while queue:
		(key,path) = queue.pop(0)
		visited.add(key)
		children = getPossibleActions(key)
		for elem in children:
			if elem == finalPrime:
				return ' '.join(map(str,path + [elem]))
			else:
                		if elem not in visited and elem not in added:
					queue.append((elem,path+[elem]))
					added.add(elem)

	return "UNSOLVABLE"

def main():
	primes = str(sys.stdin.readline()).split()
	print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
