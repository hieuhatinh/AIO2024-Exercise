def max_sliding_window(num_list, k):
    n = len(num_list)
    max_number_list = []
    for i in range(n-k+1):
        curent_list = num_list[i:i+k]
        max_number = max(curent_list)
        max_number_list.append(max_number)

    return max_number_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
max_num_list = max_sliding_window(num_list, k=3)
print(max_num_list)
