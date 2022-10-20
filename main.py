import names

def acquaintance():
	input("What is your name? ")
	print("Good! I am ", names.get_full_name())
	pass

def dogName():
	input("What is name your dog? ")
	print("Good! My dog name is ", names.get_first_name())
	pass

acquaintance()
dogName()
