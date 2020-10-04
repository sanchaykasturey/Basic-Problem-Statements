#RESTAURANT MANAGEMENT SYSTEM
#SUM UP THE CONTENTS OF THE MENU (PRICES ALONG WITH THE FOOD ITEMS)
menu={"a":1, "b":2, "c":3, "d":4 } #PREDEFINED DICTIONARY MENU FOR THE RESTAURANT
output= sorted(menu.items(), key= lambda x:x[1])#OUTPUT OF MENU ITEMS IN SORTED MANNER ACCORDING TO KEY
bill={}#ANOTHER DICTIONARY FOR STORING THE BILL
for i in output:#PRINTING THE FOOD ITEMS
    print(i[0],i[1])
def takeOrder(): #FUNCTION FOR TAKING THE ORDERS
    order = input("Please enter your order according to the available menu")
    if order in menu.keys():#CONDITIONALS FOR ORDERS TAKEN
        print ("You have ordered {} for price Rs {} .".format(order, menu[order]))
        bill.update({order:menu[order]})#UPDATING THE ORDER ALONG WITH PRICE IN BILL DICTIONARY
        otherOrder = input("Do you want to order something else?(Y/N?)")
        if otherOrder=="Y":
            for i in output:#IT WILL AGAIN DISPLAY OUTPUT TO CHOOSE FROM THE DICTIONARY OF MENU
                print(i[0],i[1])
            order = input("Please enter your order according to the available menu")
            print ("You have ordered {} for price Rs {} .".format(order, menu[order]))
            bill.update({order:menu[order]})#UPDATING THE ORDER ALONG WITH PRICE IN BILL DICTIONARY

    else:
        print("Your choice is not available, Please order again")
        for i in output:
            print(i[0],i[1])
        order = input("Please enter your order according to the available menu")
        print ('You have ordered {} for price Rs {} .'.format(order, menu[order]))
        bill.update({order:menu[order]})
        otherOrder = input("Do you want to order something else?(Y/N?)")
        if otherOrder=="Y":
            for i in output:
                print(i[0],i[1])
            order = input("Please enter your order according to the available menu")
            print ("You have ordered {} for price Rs {} .".format(order, menu[order]))
            bill.update({order:menu[order]})
def OrderBill(bill):
    sum = 0
    for i in bill.values():
        sum = sum + i
    return sum#SUM OF THE FINAL BILL
takeOrder()
OrderBill(bill)
