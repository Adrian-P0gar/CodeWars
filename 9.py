'''#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case. '''


def find_missing_letter(chars):

    c = []
    x = ""
    n = 0
    for i in chars:
        c.append(ord(i))

    while n < len(c):
        for i in range(len(c)-1):
            if c[i] + 1 != c[i + 1]:
                x = (c[i] + 1)
                n += 1

    return chr(x)


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))
