def delete(list_, index=None):
    if index is None:
        index = -1
        return list_[:index]
    elif index == -1:
        return list_[:index]
    else:
        return list_[:index] + list_[index + 1:]

# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  #
print(delete([0, 1, 1, 2, 3], index=1))  #
print(delete([0, 1, 2, 3, 4, 4]))  #