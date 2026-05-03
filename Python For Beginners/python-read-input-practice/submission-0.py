def add_two_numbers() -> int:
    user_input = input()
    num_list = user_input.split(",")
    return sum([int(x) for x in num_list])



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
