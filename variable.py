var = 1

y = 23.0


y = "sally"

# print(y)
# type is function to check the datatype of a varable
# print(type(y))


# Variable in programming: Variable are placeholder for storing data in a computer program


# Casting

num = 2
# str() here converts integer to a string

num = str(num)


# print(type(num))


# Convert a string value (object) to an integer

x = "1"

x1 = int(x)

# print(type(x1))

# Explain this code

x3 = "12340"

x4 = int(x3)

print(x4)

# print(num)


# Convert number to float (decimals in math)

f = "2995959959595955999"

f1 = float(f)

print(f1)


"""

1. How do we cast an integer to a string
2. How do we cast a string to an integer
3. How do we find the tyoe if variable
4. What is a variable
5. List the various data tyoes of variables in python
6. How many cases do we have i generally  
7. Explain snake, camel, pascal'
8. Concatenation
9. How do we output variables
10. What is a global variable
    
"""
# type. = "John"


first_name = "JOhn"

# MyNaameJohn


# Assigning multiple values to a variable


first_name, last_name = "John", "Doe"


print(first_name)


name2 = name3 = name4 = "Divine123456"

print(name3 + " " + first_name)

list = ["Divine", 12, "Flourish", True, False]


item, _, _, _, _ = list

print(_)

companyName = "Skybeam"

print(companyName)


def printDivine():

    global companyName

    companyName = "DivineTech"


print(companyName)


printDivine()


print(companyName)
