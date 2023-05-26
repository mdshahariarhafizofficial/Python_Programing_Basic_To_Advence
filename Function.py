def largestValue(a, b, c):
    if a > b and a > c:
        print("Largest Value IS\" a \"")
    elif b > a and b > c:
        print("Largest Value Is \" b\"")
    else:
        print("Largest Value Is \" c\"")


a = int(input("Enter The Value Of a: "))
b = int(input("Enter The Value Of b: "))
c = int(input("Enter The Value Of c: "))

largestValue(a, b, c)
largestValue(58, 89, 40)