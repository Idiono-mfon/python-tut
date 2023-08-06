
# For Loops


# for ball in balls:
#     print(ball)

# numbers = range(1000000)

# result = 0

# for num in numbers:

#     result += num

#     # result = result + num

# print(result)


# numbers = range(1000000)

# result = 1

# for num in numbers:

#     if (num == 0):
#         num += 1

#     result *= num

#     # result = result + num

# print(result)


# numbers = range(1000000)

# largest = numbers[0]

# for num in numbers:

#     if (num > largest):
#         largest = num

#     # result = result + num

# print(largest)


# def findMaxAndMin(list: list):

#     maxValue = max(list)

#     minValue = min(list)

#     print(maxValue, minValue)


# findMaxAndMin(numbers)

# numbers = range(100)

# odd_num_list = []

# for num in numbers:

#     if (num % 2 != 0):
#         odd_num_list.append(2 * num)

# print(odd_num_list)

balls = ["football", "handball", "volleyball", "soccer"]

for index in range(len(balls)):
    # 0 - Football
    # 1 - handball

    print(f"{index} ========== {balls[index]}")
