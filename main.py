name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter you age: "))

# String Formating
# print("Hello " + name)
# print("Hello {a} {b}".format(a=name, b=surname))
# print("Hello %s %d" % (name, 5))
print(f"Hello {name} {surname}")

if age >= 18:
    print("You are an adult")
elif age >= 12:
    print("You are a teenager")
else:
    print("You are a baby")
