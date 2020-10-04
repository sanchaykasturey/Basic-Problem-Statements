##Consider a currency system in which there are notes of seven denominations, namely, Re. 1,
##Rs. 2, Rs. 5, Rs. 10, Rs. 50, and Rs. 100. If a sum of Rs. N is entered through the keyboard,
##write a program to compute the smallest number of notes that will combine to give Rs. N
print("Money : ") ##taking input as in INR
INR = int(input())
##suitable conditions applied according to the input taken
while INR >= 100:
	b = int(INR / 100)
	INR = INR % 100
	print("\n\n 100 notes are : ", b)
	break
while INR >= 50 :
	c = int(INR / 50)
	INR = INR % 50
	print("\n\n 50 notes are : ", c)
	break
while INR >= 10:
	d = int(INR / 10)
	INR = INR % 10
	print("\n\n 10 notes are : ", d)
	break
while INR >= 5:
	e = int(INR / 5)
	INR = INR % 5
	print("\n\n 5 notes are: ", e)
	break
while INR >= 2:
	f = int(INR / 2)
	INR = INR % 2
	print("\n\n 2 notes are : ", f)
	break
while INR >= 1:
	g = int(INR / 1)
	INR = INR % 1
	print("\n\n 1 notes are : ", g)
	break
