#primes.py
#erzeugen der Primzahlen von 1 bis 1000

primeList = []


for j in range (1, 1001):
	for i in range (1, 1001):
		if(i % j == 0):
			if(i == j or i == 1):
				for x in range(1, 1001):
					primeList[x+1] = j
					
print(primeList)