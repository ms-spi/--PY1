def get_count_char(str_):
    str_ = ''.join(str_.lower().split())
    dict_ = {}


    for i in str(str_):
        if i.isalpha():
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
    return dict_

def get_procent(dict_):
    sum_letters = sum(dict_.values())
    for k, v in dict_.items():
        dict_[k] = v * 100 / sum_letters
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_dict = {'д': 13, 'а': 18, 'н': 13, 'о': 29, 'е': 23, 'п': 9, 'р': 13, 'л': 16, 'ж': 2, 'и': 14, 'б': 5, 'у': 5, 'т': 18, 'з': 2, 'в': 14, 'ь': 6, 'с': 16, 'я': 4, 'ы': 5, 'к': 6, 'ч': 2, 'г': 1, 'м': 8, 's': 1, 'p': 1, 'l': 1, 'i': 2, 't': 1, 'х': 3, 'ф': 1, 'щ': 1, 'ю': 1, 'j': 1, 'o': 1, 'n': 1}

print(get_count_char(main_str))


print(get_procent(main_dict))
