'''Description:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]'''

# Test.describe("Basic tests")
# Test.assert_equals(count_smileys([]), 0)
# Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
# Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
# Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


def count_smileys(arr):
    dic = {1: ':D', 2: ':~D', 3: ':-D', 4: ';D', 5: ';~D', 6: ';-D',
           7: ':)', 8: ':~)', 9: ':-)', 10: ';)', 11: ';~)', 12: ';-)'}
    a = 0
    for i in arr:
        if i in dic.values():
            a = a + 1
    return a


print(count_smileys([]))
