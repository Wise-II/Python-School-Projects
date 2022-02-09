import sys
import os
def main():
    retail()
    repeat()
def retail():
#asks the end-user for a wholesale price
 wholesale =(float(input("Enter wholesale price ")))

#calculates said price to a retail MSRP
 retailMSRP = wholesale * 2.50

#gives out a price in said currency (such as $)
 print("retail price is ",retailMSRP," $")
 repeat()
def repeat():
    keepgoing =(input("do you wish to keep going Y/N "))

    if keepgoing == "y":
        retail()
    else:
     print("Goodbye...")
     sys.exit()
main()
  

