# Write a function that accepts an array of 10 integers(between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example:
# # => returns "(123) 456-7890"
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!


def create_phone_number(n):
    first_number = ""
    second_number = ""
    third_number = ""
    for i in n[:3]:
        first_number += str(i)
    for i in n[3:6]:
        second_number += str(i)

    for i in n[-4:]:
        third_number += str(i)

    return "({}) {}-{}".format(first_number, second_number, third_number)


list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(list_number))
