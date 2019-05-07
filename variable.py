a = 10
b = 20
c = 30

print (10+20+30)
print ("Summe = ", a+b+c)
print ("multiplikation = ", a*b)
print ("Division = ",a/b)
print ("Division = ",int(c/a))
print ("Potenz = ",a**b)

text = "Halo Welt";

print(text)
print(text * 99)

name = input("Wer bist du eig?!")
print("Du bist also ", name * 99,)

for i in ("Franz", "Karl", "Klausz"):
	print(i)
	
for i in (-4, 12, 19, 7, 0, -281, 192):
	print(i, end=" ")
	
for i in range (1, 100):
	print (i, end = ".")
	
while(True):
	i /= 1000
	print(i, end = " ")