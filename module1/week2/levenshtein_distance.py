def levenshtein_distance(source_word, target_word):
    rows = len(source_word) + 1
    columns = len(target_word) + 1

    # initial matrix and complete the first row and column
    distance_matrix = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        distance_matrix[i][0] = i
    for j in range(columns):
        distance_matrix[0][j] = j

    # compute remaining cells in matrix
    for i in range(1, rows):
        for j in range(1, columns):
            if (source_word[i-1] == target_word[j-1]):
                distance_matrix[i][j] = min(
                    distance_matrix[i-1][j] + 1,
                    distance_matrix[i][j-1] + 1,
                    distance_matrix[i-1][j-1] + 0)
            else:
                distance_matrix[i][j] = min(
                    distance_matrix[i-1][j] + 1,
                    distance_matrix[i][j-1] + 1,
                    distance_matrix[i-1][j-1] + 1)
    # backtracking???
    return distance_matrix[rows-1][columns-1]


distance = levenshtein_distance(source_word='yu', target_word='you')
print(distance)
