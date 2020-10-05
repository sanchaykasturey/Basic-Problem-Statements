#FEEL FREE TO PING ME AT
#https://www.linkedin.com/in/sanchay-kasturey-a97879175/
#THIS PROGRAM IS FOR CALCULATING THE BILL OF ICE CREAMS IF THE PRICE OF
#EACH ICE CREAM IS DIFFERENT IN 5 DAYS, BILL WILL BE OF SEVERAL WEEKS
#LAST BILLING AMOUNT SHOULD BE ONLY PRINTED AT END
#ice-cream a,b,c,d,e

#FUNCTION FOR TAKING INPUT OF PRICES OF DIFFERENT ICECREAMS
def priceOfIceCreamPerDay():
    print("Enter the price of 5 ice-creams")
    a=int(input("for first ice cream"))
    b=int(input("for second ice cream"))
    c=int(input("for third ice cream"))
    d=int(input("for fourth ice cream"))
    e=int(input("for fivth ice cream"))
    bill = a+b+c+d+e
    return bill
#FUNCTION FOR CALCULATING BILL PER WEEK AND APPEND THAT AMOUNT
def billPerWeek():
    bill = priceOfIceCreamPerDay()
    week=[]
    n=0
    while n<7:
        priceOfIceCreamPerDay()
        week.append(bill)
        n=n+1

    print("Bill of the week for mother to pay", sum(week))
if __name__ == '__main__':
    print("The first input is a trial the second input will be counted for the first day of the week")
    billPerWeek()
#FEEL FREE TO PING ME AT
#https://www.linkedin.com/in/sanchay-kasturey-a97879175/
