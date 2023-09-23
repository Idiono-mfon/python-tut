
fruits = ["apple", "banana", "cherry"]


def greet_person(person):

    print('Hello', person)


def print_time_table(time_number):

    print("======  {} Times Table".format(time_number))

    for j in range(1, 5000):

        print(f"{time_number} X {j} ======= {time_number * j}")


def print_range_time_table(range1, range2):

    for i in range(range1, range2):
        for j in range(1, 13):

            print(f"{i} X {j} ======= {i * j}")

        print("====== Completed {} Times Table".format(i))

# Pack keyword arguments into a list


def find_sum_mean(*args):

    total = sum(args)

    mean = total / len(args)

    return (total, mean)

#  function definiton with a default argument value


def get_name1(name="Flourish"):
    print('Good evening', name)

# Pack keyword arguments into a dictionary


def printStateAndCapital(**states):
    print(states)


# Passing lists into a function
def printFruits(fruits):
    for fruit in fruits:
        print(fruit)


def returnName(name):
    return name
    print("HELLO", name)


def do_nothing():
    pass


# print_time_table(7)

# print_range_time_table(range1=10, range2=20)

# greet_person("Divine")

# Unpacking the tuple
# total, mean = find_sum_mean(2, 3, 4, 5)

# print(total)

# print(mean)


# printStateAndCapital(lagos="Ikeya", ondo="Akure",
#                      Delta="Asabas", Enugu="Enugu")
get_name1("Jane")

printFruits(fruits)


print(returnName("James"))


def new_thing(thing):
    for k in range(50):
        print(k)
