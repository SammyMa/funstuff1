__author__ = 'jim027@ucsd.edu, A99075314, siz001@ucsd.edu, A99076798, yuc036@ucsd.edu'

import sys

#function to check if a number is a prime or not
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
	return listOfPrimes

def getPath(startingPrime, finalPrime):
	return path

def main():
	primes = str(sys.stdin.readline()).split()
	print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
	main()
