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
   	
	for num in range(1,9):
        	stack = [(startingPrime,[startingPrime])]
       	 	visited = set()
        	while stack:
			(key,path) = stack.pop()
            		visited.add(key)
            		if key == finalPrime and len(path) <= num :
                		return ' '.join(map(str,path))
            		elif len(path) >= num:
                		for node in path:
                    			if node in visited:
                        			visited.remove(node)
                		continue
            		children = getPossibleActions(key)
            		for elem in children:
                		if elem not in visited:
					stack.append((elem, path + [elem]))
	return "UNSOLVABLE"

def main():
	for line in sys.stdin:
		primes = str(line).split()
		print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
