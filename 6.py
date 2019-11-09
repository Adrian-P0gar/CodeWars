'''Implement the function unique_in_order which takes as argument a sequence and returns
 a list of items without any elements with the same value next to each other and preserving the original order of elements.'''
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])


def unique_in_order(iterable):
    try:
        final_iterable = [iterable[0]]
        for i in iterable:
            if final_iterable[-1] != i:
                final_iterable.append(i)

        return final_iterable
    except IndexError:
        final_iterable = []
        return final_iterable


print(unique_in_order([1, 2, 2, 3, 3, 2]))
print(unique_in_order(''))
# x = 'AAAABBBCCDAABBB'
# print(",".join(x).split())
