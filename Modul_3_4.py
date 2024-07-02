def single_root_words(root_word, *other_words):
    prom_spisok = list(other_words) # замена кортежа на список
    low_reg = [s.lower() for s in prom_spisok] # все элементы в нижний регистр
    same_words = []
    for i in range(len(low_reg)):
        if root_word.lower() in low_reg[i] or low_reg[i] in root_word.lower():
            same_words.append(other_words[i])
    return same_words

print(single_root_words('rich', 'riCHiest', 'orichalUm', 'CFFeers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Disable', 'Bagel'))