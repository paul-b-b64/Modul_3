def single_root_words(root_word, *other_words):
    prom_spisok = []
    for i in range(len(other_words)):
        prom_spisok.append(other_words[i])
    same_words = []
    for i in prom_spisok:
        # prom_spisok[i].lower()
        # root_word.lower()
        if root_word.lower() in prom_spisok:
            same_words.append(prom_spisok[i])
    return same_words

print(single_root_words('Rich', 'riCHiest', 'orichalCum', 'CFFeers', 'richies'))


#     same_words = []
#
#     for i in range(len(other_words)):
#         # other_words[i].lower()
#         # root_word.lower()
#         if root_word in other_words[i]:
#            same_words.append(other_words[i])
#     return same_words
#
# print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))