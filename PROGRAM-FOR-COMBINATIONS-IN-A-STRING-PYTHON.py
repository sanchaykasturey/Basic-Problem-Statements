#THE PROGRAM FOR GIVING ALL THE POSSIBLE PERMUTATIONS IN A STRING
def toChange(list):
	return ''.join(list)
def permutaions(a, q, r):
	if q == r:
		print(toChange(a))
	else:
		for i in range(q, r + 1):
			a[q], a[i] = a[i], a[q]
			permutaions(a, q + 1, r)
			a[q], a[i] = a[i], a[q]
forCombinations = input("Enter the string input to get all combinations of that string")
n = len(forCombinations)
print("The no of character present are:")
print(n)
a = list(forCombinations)
print("Number of Combinations are:")
permutaions(a, 0, n-1)
