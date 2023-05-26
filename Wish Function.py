def wish(Wish="Happy", Topic="Birthday", name=" You "):
    print(Wish, Topic, "To", name)


Wish = str(input("Enter Your Wish: "))
Topic = str(input("Enter Your Topic: "))
name = str(input("Enter Your Name: "))

wish(Wish, Topic, name)
