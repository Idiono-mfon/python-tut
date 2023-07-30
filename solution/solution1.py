""" ( Solution 2 )

testString = "google.com"

result = {}


for i in testString:
    count = testString.count(i)
    result[i] = count


print(result)

"""


"""
(solution 3)

def echoSubstr(my_string):
    if len(my_string) < 2:

        return ""

    new_string = f'{my_string[0]}{my_string[1]}{my_string[-2]}{my_string[-1]}'

    if len(new_string) < 2:

        return ""
    return new_string



"""

"""

(Solution 4)

def updateChar(target_str: str):
    myString = ""

    search_string = target_str[0]

    context_string = target_str[1:]

    return search_string + context_string.replace(search_string, "$")

"""


"""

(solution 5)

def printMultipleStr(str1: str, str2: str):

    if (len(str1) < 3 and len(str2) < 3):
        return ""

    swap_str1 = str2[0] + str2[1] + str1[2:]

    swap_str2 = str1[0] + str1[1] + str2[2:]

    return "{} {}".format(swap_str1, swap_str2)


"""


"""

(Solution 6)

def addIngToStr(target_str: str):
    if (len(target_str) < 3):
        return target_str

    if (target_str.endswith('ing')):
        return target_str + "ly"

    return target_str + "ing"


print(addIngToStr('string'))


"""
