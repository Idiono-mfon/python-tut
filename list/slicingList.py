names = ["James", "Dom", 2, 3, True, "John"]


my_nw_list = names[1:-1]

print(my_nw_list)

# We use membership operator to verify the existence iof element in a list

print("James" not in names)

# Changin item in a list
names[0] = "Dominion"

print(names)


balls = ["football", "handball", "volleyball", "soccer"]

# CHANGIN MULTIPLE ITEMS IN A LIST
# balls[1:3] = ["basketball", "Tennis"]
balls[1:2] = ["basketball", "basketball", "Tennis"]


print(balls)
