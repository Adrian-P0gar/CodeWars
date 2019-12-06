def sum_range(number1, number2):
    '''
    This function return sum of the numbers betwen number1, number2.
    '''
    preliminary_range_sum = 0
    if number1 > number2:
        for number in range(number2, number1):
            preliminary_range_sum += number
        return preliminary_range_sum + number1
    if number2 > number1:
        for number in range(number1, number2):
            preliminary_range_sum += number
        return preliminary_range_sum + number2
    else:
        return number1


print(sum_range(0, -1))
print(sum_range(1, 2))
print(sum_range(3, -2))
