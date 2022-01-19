#Varibles, one is used to determine if the calculation shuld go on or not
keepgoing = "y"
COMM_RATE = 0.10

while keepgoing == "y":
    SALES = float(input("enter the amount of sales "))
    COMM = COMM_RATE * SALES
    print("the commissions are,", COMM)
    keepgoing = input("do you want to calculate anoter commission? ")
