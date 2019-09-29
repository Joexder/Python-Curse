myStr = "Hrello World"

# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())

myStr = myStr.replace("Hrello", "Hello")
print (myStr)
print(myStr.count(' '))
print(myStr.startswith('Hello'))
print(myStr.endswith('l'))

print(myStr.split('l'))
print(myStr.find('d'))
print(len(myStr))
print(myStr.index("l"))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[6])

print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))