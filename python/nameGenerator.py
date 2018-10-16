import random as rand
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","z"]
vowels = ["a","e","i","o","u","y"]


def getName():

	return cVccV()
	

	
def cVccV():
	name = ""
	con1 = consonants[rand.randint(0,len(consonants)-1)]
	vow1 = vowels[rand.randint(0,len(vowels)-1)]
	con2 = consonants[rand.randint(0,len(consonants)-1)]
	vow2 = vowels[rand.randint(0,len(vowels)-1)]
	return con1+vow1+con2+con2+vow2