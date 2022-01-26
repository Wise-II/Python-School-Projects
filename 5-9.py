MaxVal = 10
#maximum value
def main():
    #print table headers
    print("Number       sqaure")
    print("------------------")


    #print numbers 1 to 10 and their squares
    for number in range(1, 11):
        square = number*2
        print(number,"          ",square)
#call the main function
main()