# num = int(input("Enter Your Number: "))
# print(f"Multiplication Table of {num} is: ")

try:
    num = int(input("Enter Your Number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
except ValueError:
    print("Invalid Syntax!")

print("Program End")