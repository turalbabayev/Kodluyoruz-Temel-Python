inputList = [[1, 2], [3, 4], [5, 6, 7]]


def reverse(liste):
    liste = liste[::-1]

    for i in range(len(liste)):
        (liste[i]) = (liste[i])[::-1]

    return liste        


print(reverse(inputList))