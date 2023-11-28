for test_case in range(1, 11) :
    test_num = int(input())
    ans = 0
    matrix = []
    for row in range(100) :
        matrix.append(list(map(int, input().split())))
    max_value = 0
    # 행우선
    for i in range(100):
        sum_value = 0
        for j in range(100):
            sum_value += matrix[i][j]
        if max_value < sum_value:
            max_value = sum_value

    # 열우선
    for i in range(100):
        sum_value = 0
        for j in range(100):
            sum_value += matrix[j][i]
        if max_value < sum_value:
            max_value = sum_value
    # 대각선 \
    sum_value = 0
    for i in range(100):
        sum_value += matrix[i][i]
        if max_value < sum_value:
            max_value = sum_value

    # 대각선 /
    sum_value = 0
    for i in range(100):
        sum_value += matrix[i][100-1-i]

        if max_value < sum_value:
            max_value = sum_value

    print("#{} {}".format(test_case, max_value))