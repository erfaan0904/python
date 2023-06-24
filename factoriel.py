print("---------------------------------------")
num = int(input("Please enter a number : "))
fac, i = 1, 1
while(i <= num) :
    fac = fac * i
    i   = i + 1
print("Factorial of the entered number :", fac)
print("---------------------------------------")