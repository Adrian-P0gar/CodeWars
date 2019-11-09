def to_weird_case(string):
    a = string.replace(" ", "")
    print(a)
    for i in a[::2]:
        i.upper()
    print(a)


to_weird_case('This is a test')

#'ThIs Is A TeSt'


"Modificare test"
