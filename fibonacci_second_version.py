def rec_fib(n):     #recursive function
    if (n == 0 or n == 1):
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)
print(rec_fib(8))
def fib(n):
    while(True):
        print(" ")
        print("------------------------------")
        print("your entered number : ", n)
        print("------------------------------")
        a    = 1
        b    = 1
        temp = 0
        for i in range(2,n):
            temp = b
            b    = a + b
            a    = temp
        print("the", i, "th member of fibunacci is : ",b)
        break
while (True):
    n = input("Please enter a number : ")
    try:
        n = int(n)
    except:
        if(n == 'A' or n == 'a'):
            print("try again")
        elif(n == 'B' or n == 'b'):
            print("try again")
        elif (n == 'C' or n == 'c'):
            print("try again")
        elif (n == 'D' or n == 'd'):
            print("try again")
        elif (n == 'E' or n == 'e'):
            print("try again")
        elif (n == 'F' or n == 'g'):
            print("try again")
        elif (n == 'H' or n == 'h'):
            print("try again")
        elif (n == 'I' or n == 'i'):
            print("try again")
        elif (n == 'J' or n == 'j'):
            print("try again")
        elif (n == 'K' or n == 'k'):
            print("try again")
        elif (n == 'L' or n == 'l'):
            print("try again")
        elif (n == 'M' or n == 'm'):
            print("try again")
        elif (n == 'N' or n == 'n'):
            print("try again")
        elif (n == 'O' or n == 'o'):
            print("try again")
        elif (n == 'P' or n == 'p'):
           print("try again")
        elif (n == 'Q' or n == 'q'):
            print("try again")
        elif (n == 'R' or n == 'r'):
            print("try again")
        elif (n == 'S' or n == 's'):
            print("try again")
        elif (n == 'T' or n == 't'):
            print("try again")
        elif (n == 'U' or n == 'u'):
            print("try again")
        elif (n == 'V' or n == 'v'):
            print("try again")
        elif (n == 'W' or n == 'w'):
            print("try again")
        elif (n == 'X' or n == 'x'):
            print("try again")
        elif (n == 'Y' or n == 'y'):
            print("try again")
        elif (n == 'Z' or n == 'z'):
            print("try again")
        else:
            print("try again")
    else:
        if(n == 0):
            print("------------------------------")
            print("zero is not accepted")
            print("run again this cod")
            print("------------------------------")
            break
        else:
            fib(n)
            break