
'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.'''


def find_uniq(arr):
    for n in arr:
        if arr[0] == arr[-1]:
            if n != arr[0]:

                return n
        else:
            if arr[0] == arr[1]:
                return arr[-1]
            else:
                return arr[0]


a = ([2, 2, 2, 1])
b = ([1, 2, 2, 2, 2])
c = ([3, 3, 4, 3, 3])
D = ([5, 4, 5, 5, 5, 5])
print(find_uniq(a))
print(find_uniq(b))
print(find_uniq(c))
print(find_uniq(D))
