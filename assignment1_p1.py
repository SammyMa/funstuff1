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
	queue = [(startingPrime, [startingPrime])]
	visited = []
	added = []
	while queue:
		(key,path) = queue.pop(0)
		visited.append(key)
		children = getPossibleActions(key)
		for elem in children:
			if elem == finalPrime:
				return ' '.join(map(str,path + [elem]))
			else:
				if inlist(visited, elem) == False and inlist(added, elem) == False:
					queue.append((elem,path+[elem]))
					added.append(elem)

	return "UNSOLVABLE"

def main():
	primes = str(sys.stdin.readline()).split()
	print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
