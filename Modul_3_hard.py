data_structure = [
    [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def dict_to_list(dct): # преобразование словаря в список
    list_dict = []
    for i in dct.items():
        element = list(i)
        list_dict += element
    return list_dict

def ploskiy_spisok(massiv): # преобразование многомерного списка в одномерный
    flag = True
    while flag:
        list_vnutr = []
        for elem in massiv:
            if isinstance(elem, str) or isinstance(elem, int):
                list_vnutr.append(elem)
                flag = False
            if isinstance(elem, dict):
                list_vnutr += dict_to_list(elem)
                flag = True
            if (isinstance(elem, tuple) or
            isinstance(elem, list) or
            isinstance(elem, set)):
                list_vnutr += elem
                flag = True
        massiv.clear()
        massiv += list_vnutr
    return massiv

def sum_elts_list(list_): # сумматор элементов списка
    summa_ = 0
    for i in list_:
        if type(i) == str:
            summa_ += len(i)
        else: summa_ += i
    return summa_

def calculate_structure_sum(arg):
    sum_elts_list(ploskiy_spisok(arg))


result = calculate_structure_sum(data_structure)
print(result)

# print(sum_elts_list(ploskiy_spisok(data_structure)))



