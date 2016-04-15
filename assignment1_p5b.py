__author__ = 'jim027@ucsd.edu, A99075314, siz001@ucsd.edu, A99076798, yuc036@ucsd.edu, A91112915'

import sys
import time
try:
	import Queue as Q
except ImportError:
	import queue as Q

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

def distance(heu, startingPrime, finalPrime):
	distance = len(str(startingPrime))
	if heu >= 0:
		distance = heu - 1
		return distance
	for index in range(0, len(str(startingPrime))):
		if str(startingPrime)[index] == str(finalPrime)[index]:
			distance = distance - 1

	return distance

def getPath(startingPrime, finalPrime):
	startingPrime = int(startingPrime)
	finalPrime = int(finalPrime)

	if len(str(startingPrime)) != len(str(finalPrime)):
		return "UNSOLVABLE"

    	if isprime(startingPrime) == False or isprime(finalPrime) == False:
        	return "UNSOLVABLE"
    	if startingPrime == finalPrime:
        	return startingPrime

	queue = Q.PriorityQueue()
    	queue.put(((distance(0,startingPrime,finalPrime)),distance(0,startingPrime,finalPrime),0,startingPrime,[startingPrime]))
	
	visited = set()
	added = {startingPrime}

	while queue:
		(distf,disth,distg,key,path) = queue.get()
		visited.add(key)
		children = getPossibleActions(key)
		for elem in children:
			if elem == finalPrime:
				return ' '.join(map(str,path + [elem]))
			else:
				if elem not in visited and elem not in added:
					queue.put((distg+1+distance(disth,elem,finalPrime),distance(disth,elem,finalPrime),distg+1,elem,path+[elem]))
					added.add(elem)
	return "UNSOLVABLE"

def main():
	for line in sys.stdin:
		primes = str(line).split()
		print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
