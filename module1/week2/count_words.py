def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        file.close()
    return data.split(' ')


def count_words(file_path):
    result_count_words = {}
    data = read_file(file_path)
    for word in data:
        word = word.lower()
        if word in result_count_words:
            result_count_words[word] += 1
        else:
            result_count_words[word] = 1
    return dict(sorted(result_count_words.items()))


file_path = 'F:\AIO2024\AIO2024-Exercise\module1\week2\P1_data.txt'
result_count_words = count_words(file_path)
print(result_count_words)
