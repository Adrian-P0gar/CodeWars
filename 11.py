
'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]'''

x = (["a", 0, 0, "b", None, "c", "d", 0, 1, False,
      0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9])
y = ([0, 1, None, 2, False, 0, 1])
c = ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])


def move_zeros(array):
    lista = []
    lista2 = []
    for i in array:

        if not (i == 0 and isinstance(i, bool) == False):
            lista.append(i)
        if i == 0 and isinstance(i, bool) == False:
            lista2.append(i)
    for i in lista2:
        lista.append(i)

    return lista



print(move_zeros(y))




# isinstance(i, bool)
