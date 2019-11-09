'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types. '''


def find_short(s):
    l = s.split()
    x = []
    z = []
    c = ''
    for i in l:
        x.append(i)
        for i in x:
            z.append(len(i))
            z.sort()
            c = z[0]
    return c


print(find_short("bitcoin take over the world maybe who knows perhaps"))
