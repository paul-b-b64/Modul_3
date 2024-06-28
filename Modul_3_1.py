calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    cort_ = (len(string), string.upper(), string.lower())
    count_calls()
    return (cort_)

def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        list_to_search[i].lower()
    string.lower()
    comp_ = False
    if string in list_to_search:
        comp_ = True
    count_calls()
    return comp_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('просо', ['rb', 'просо', 'uj']))
print(is_contains('просо', ['rb', 'запрсов', 'uj']))
print(calls)


