MaxVal = 10
#maximum value
def main():
    #print table headers
    print("KPH       MPH")
    print("------------------")

    #prints the values itself
    for kph in range(60,130,10):
        MPH = kph*0.6214
        print(kph,"        ",MPH)
#call the main function
main()