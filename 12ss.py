
# def fib(nr):
#     a, b, c = 0, 1, 1
#     print("1." + str(a))
#     print("2." + str(b))

#     i = 3
#     while i <= nr:
#         print(str(i) + ". " + str(c))
#         a = b
#         b = c
#         c = a + b
#         i += 1


def productFib(prod):
    a, b, c = 0, 1, 1
    g = [0, 1, 1]
    i = 0
    while c <= prod:
        a = b
        b = c
        c = a + b
        g.append(c)
        print(g)
    for i in g:

        if g[i] * g[i+1] == prod:
            print("asd")



productFib(4895)
def productFib(prod):
    a, b, c = 0, 1, 1
    g = [0, 1, 1]
    x = 0
    s = ([])
    n = 1
    while c < prod:
        a = b
        b = c
        c = a + b
        g.append(c)

        for n in g:
            if len(g) > 3 and (n * g[-1]) == prod:
                s.append(n)
                s.append(g[-1])
                s.append(True)
                print(s)