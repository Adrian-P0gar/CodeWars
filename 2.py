def get_sum(a, b):
    x = 0
    if a > b:
        for i in range(b, a):
            x = x + i
        return x + a
    if b > a:
        for i in range(a, b):
            x = x + i
        return x + b
    else:
        return a


print(get_sum(0, -1))
print(get_sum(1, 2))
print(get_sum(3, -2))
