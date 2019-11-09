"""Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output."""


def friend(x):

    out_friend = []
    for i in x:
        if len(i) < 5 and len(i) > 3:
            out_friend.append(i)
    return out_friend


friends = ['y99J', 'xGe1', '4ko', 'J', 'PoO3', 'Sblo']

print(friend(friends))

# ['y99J', 'xGe1', '4ko', 'J', 'PoO3', 'Sblo'] should equal ['y99J', 'xGe1', 'PoO3', 'Sblo']
