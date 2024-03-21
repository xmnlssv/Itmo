import sys
import numpy as np

# Функция для обмена строк в матрице и векторе свободных членов, чтобы избежать деления на ноль в методе Гаусса.
def swap_lines(matrix, i, f):
    for j in range(i + 1, len(matrix)):
        if matrix[j][i] != 0:
            matrix[j], matrix[i] = matrix[i], matrix[j]
            f[j], f[i] = f[i], f[j]
            return [matrix, f]
    print("У матрицы нет уникальных решений!")
    sys.exit(0)

# Выводит текущее состояние матрицы и вектора свободных членов для визуализации процесса решения.
def print_matrix(matrix, f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(round(matrix[i][j], 5), end=" ")
        print(round(f[i], 5))
    print("------------------------------------------------")

# Вычисляет определитель матрицы, учитывая количество перестановок строк, для определения ее обратимости.
def det_calc(matrix, k):
    det = (-1) ** k
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det

# Реализует метод Гаусса для решения системы линейных уравнений, включая прямой и обратный ход.
def gauss_method_solution(matrix_list):
    matrix = matrix_list[0]
    n = len(matrix)
    f = matrix_list[1]
    swaps = 0
    for i in range(n - 1):
        if matrix[i][i] == 0:
            [matrix, f] = swap_lines(matrix, i, f)
            swaps += 1
        for k in range(i+1, n):
            c = matrix[k][i]/matrix[i][i]
            matrix[k][i] = 0
            for j in range(i+1, n):
                matrix[k][j] = matrix[k][j] - c * matrix[i][j]
            f[k] = f[k] - c * f[i]
        print("Шаг №", i + 1, ":")
        print_matrix(matrix, f)
    x = [0] * n
    print(swaps)
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + matrix[i][j] * x[j]
        if matrix[i][i] == 0:
            print("У матрицы нет уникальных решений!")
            sys.exit(0)
        x[i] = (f[i] - s) / matrix[i][i]
    print("Определитель матрицы: ", det_calc(matrix, swaps))
    print("------------------------------------------------")
    return x

# Доп. задание: проверка ответа с помощью функции из библиотеки
def gauss_method_solution_with_library(matrix_list):
    matrix = matrix_list[0]

    f = matrix_list[1]

    x = np.linalg.solve(matrix, f)
    return x
