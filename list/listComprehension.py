
# double_list = []
# for single in range(11):
#     double_list.append(single*2)


# print(double_list)

# List comprehension gives us a shorter syntax to generate a list based on existing values of the list

# /Eg. 1
# single_list = range(11)

# double_list = [2 * val for val in single_list]

# print(double_list)


# double_odd_number_list = [2 * val for val in range(100) if (val % 2 != 0)]

# print(double_odd_number_list)

factors = []


def recursiveFunc(val: int):
    num = val // 2
    factors.append(num)

    if (num != 1 and val % 2 == 0):
        return recursiveFunc(num)
    return factors


print(recursiveFunc(100))
