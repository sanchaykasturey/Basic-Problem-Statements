#PROGRAM FOR TAKING INPUT OF NUMBERS IN A LIST AND THEN IF NOT PRESENT IT WILL APPEND IT AND
#MULTIPLE NUMBERS WILL BE REMOVED AUTOMATICALLY IF PRESENT
def removeMultipleNumbers(list):
    numbersInput = []
    for number in list:
        if number not in numbersInput:
            numbersInput.append(number)
    return numbersInput

numbers =(input("Enter the number: "))
a = ((numbers.split()))
print("Numbers in input: ", (removeMultipleNumbers(a)))
