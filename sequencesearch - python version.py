a = [[0] * 4 for _ in range(3)]
print("---------------------------------------------")
print("Enter your array:")
for i in range(3):
    for j in range(4):
        print("a[{}][{}]: ".format(i+1, j+1), end="")
        a[i][j] = int(input())

print("---------------------------------------------")
print("Entered array:")
for i in range(3):
    for j in range(4):
        print(a[i][j], end=" ")
    print()

print("---------------------------------------------")
print("What number do you want to search: ", end="")
n = int(input())
print("---------------------------------------------")

for i in range(3):
    for j in range(4):
        if a[i][j] == n:
            print("Your number is found")
            print("Position:")
            print("i =", i+1)
            print("j =", j+1)

print("---------------------------------------------")