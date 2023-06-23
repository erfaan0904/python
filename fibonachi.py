a, b, j, c = 1, 1, 2, 0
n = int(input("please enter a number : "))
print("1 . 1")
print("2 . 1")
for i in range (1, n) :
    j = j + 1
    c = a + b
    if(j == (n+1)) :
        break
    else :
        print(j, ".", c)
        a = b
        b = c
