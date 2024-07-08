def calculate_structure_sum(arg):
    pass

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]




# flag = False
flag = isinstance(data_structure[2], dict)
print(flag)

# for elem in data_structure:
#     if elem







# dict = {'Geeks': 10, 'for': 12, 'Geek': 31}
#
# # ks = list(dict.keys())
# # vs = dict.values()
# # its = dict.items()
def dict_to_list(dct): # преобразование словаря в список
    list_dict = []
    for i in dct.items():
        element = list(i)
        list_dict += element
    return list_dict

def sum_elts_list(list_): # сумматор элементов списка
    summa_ = 0
    for i in list_:
        if type(i) == str:
            summa_ += len(i)
        else: summa_ += i
    return summa_

# print(sum_elts_list(dict_to_list(dict)))







# print(type(dict))
# print(type(ks))
# print(type(vs))
# print(type(its))
# print(f'{ks}, {vs}, {its}')









# # Converting into list of tuple
# list = [(k, v) for k, v in dict.items()]
#
# # Printing list of tuple
# print(list)







# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# def how_deep(struct):
#     flag = False
#     count = 1
#     for i in struct:
#         if type(i) == tuple and not flag:
#             count += how_deep(i)
#             flag = True
#     return count
#
#
# ere = how_deep(data_structure)
# print(ere)
