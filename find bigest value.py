a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = int(input("Enter The Value of C : "))

if a > b and a > c:
    print("Biggest Value is : a = ", a)
elif b > a and b > c:
    print("Biggest Value is : b = ", b)
else:
    print("Biggest Value is : c = ", c)
