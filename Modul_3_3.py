def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(4)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [15, 'Run', True]
values_dict = {'a': 34, 'b': 'Cemen', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 =[54.32, 'Return']
print_params(*values_list_2, 42)