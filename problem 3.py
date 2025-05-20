a = int(input("Enter a number: "))
for i in range(1, 2 * a):
    if i % 2 == 1:
        print(i, end=", ")
