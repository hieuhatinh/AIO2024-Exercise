def count_chars(word):
    count_char_dict = {}
    for char in word:
        if char in count_char_dict:
            count_char_dict[char] += 1
        else:
            count_char_dict[char] = 1
    return dict(sorted(count_char_dict.items()))


string = 'Happiness'
string2 = 'smiles'
count_chars_string = count_chars(string)
count_chars_string2 = count_chars(string2)
print(count_chars_string)
print(count_chars_string2)
