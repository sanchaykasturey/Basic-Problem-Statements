#FEEL FREE TO PING ME AT
#https://www.linkedin.com/in/sanchay-kasturey-a97879175/
#BASIC LIBRARY MANAGEMENT SYSTEM PROBLEM
#BOOKS WILL BE DISPLAYED IN SORTED AS PER THEIR PRICE
#IF BOOK IS NOT PRESENT THEN, PROGRAM WILL ASK FOR THE PRICE
#AND IT WILL ADD THAT BOOK IN DICTIONARY booksInLibrary
print("Welcome to Book management system")
#UNSORTED DICTIONARY WHICH CONTAINS NAMES AND PRICES OF BOOKS
booksInLibrary = { "ABC": 1, "DEF":2, "GHI": 4, "XYZ": 3 }
#TO SORT THE BOOKS ON THE BASIS OF KEY
b= sorted(booksInLibrary.items(), key= lambda x:x[1])
#FOR DISPLAYING BOOKS ALONG WITH PRICE WHICH ARE IN booksInLibrary
for i in b:
    print(i[0],i[1])

def search():
    #ASKING USER INPUT THAT WHAT BOOK USER WANT TO SEARCH
    name = input("Enter the book name you want to search")
    #CONDITIONALS IF IT IS PRESENT THEN WILL SHOW THE OUTPUT
    if name in booksInLibrary.keys():
        print ('{} has price {} .'.format(name, booksInLibrary[name]))
    #IF IT IS NOT PRESENT PROGRAM WILL ASK FOR PRICE AND THEN UPDATE THE DICTIONARY
    else:
        a=int(input("Enter the price of the book please"))
        booksInLibrary.update({name:a})
        c= sorted(booksInLibrary.items(), key= lambda x:x[1])
        for i in c:
            print(i[0],i[1])
if __name__ == '__main__':
    search()
#FEEL FREE TO PING ME AT
#https://www.linkedin.com/in/sanchay-kasturey-a97879175/
