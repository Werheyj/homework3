def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(55))


# number = 55
# str_number = str(number)
# print(type(number), type(str_number))
# print()
