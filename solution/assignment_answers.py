company = "skybeam limited"
print(len(company))

#2

samplestring = "google.com"
all_freq = {}

for i in samplestring:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("the amount of letters in google.com is" + str(all_freq))

#3
b = "w3resource"
print(b[:2] + b[-2:])
c = 'w3'
print(c[0:] + c[0:])
d = "w"
print(d[:0])

#4

power = "restart"
print(power.replace("s", "$"))

#5

'''j = "abc"
q = "xyz"
e = print(j[:2] + q[-1:])
h = print( q[:2]+ j[2:])
print(e + h)'''

#6

ghd = "abc{}"
bat = "ing"
print(ghd.format(bat))
jjj = "string{}"
mmm = "ly"
print(jjj.format(mmm))

#7

work = "the lyrics is not that poor"
mod = "the lyrics is poor"
midlle = work.replace("not that poor", "good")
print(midlle)
print(mod)

#8

new = "Exercises"
print("length of longest word:" + str(len(new)))

#9

compan = "skybeam limited"
comp = compan.replace( "limited","limitsexchanged")
come = comp.replace("s", "d")
print(come)

#10

def remove_odd_characters(string):
    new_string = ""
    for index, char in enumerate(string):
        if index % 2 == 0:
            new_string += char
    return new_string
 # Example usage
input_string = "Hello, World!"
newbie = remove_odd_characters(input_string)
print(newbie)

#11

def logical_and(a, b):
    return a and b
result = logical_and(True, False)
print(result)

#12

def exclusive_or(x, y):
    return (x or y) and not (x and y)
popped = exclusive_or(True, False)
print(popped)

#13

def all_true(lst):
    for element in lst:
        if not element:
            return False
    return True
my_list = [True, True, True]
print(all_true(my_list))
my_list = [True, False, True]
print(all_true(my_list))

#14

def at_least_two_true(p, q, r):
    true_count = 0
    if p:
        true_count += 1
    if q:
        true_count += 1
    if r:
        true_count += 1
    return true_count >= 2
print(at_least_two_true(True, True, True))
print(at_least_two_true(True, False, True))
print(at_least_two_true(False, False, False))

#15

def check_condition(a, b):
    if a or not b:
        return True
    else:
        return False
    print(check_condition(True, False))
    print(check_condition(False, True))
    print(check_condition(True, True))
    print(check_condition(False, False))


#16

def check_boolean(x, y):
    if not x or not y:
        return True
    else:
        return False
    result = check_boolean(True, False)
    print(result)
    result = check_boolean(True, True)


print(result)

#17

def check_exactly_one_true(p, q, r):
    if (p and not q and not r) or (not p and q and not r) or (not p and not q and r):
        return True
    else:
        return False
    test = check_exactly_one_true(True, False, False)
    print(test)
    test = check_exactly_one_true(True, True, False)
    print(test)

#18

def check_bool(a, b):
    return a == b

#19
def check_situation (x, y):
    if x is True and y is False:
        return True
    else:
        return False

#20

def check_answer (p, q, r):
    count_false = 0
    if p is False:
        count_false += 1
    if q is False:
        count_false += 1
    if r is False:
        count_false += 1
    if count_false == 3:
        return True
    else:
        return False