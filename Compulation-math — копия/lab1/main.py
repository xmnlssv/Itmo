from input import *
from math_solution import *
from discrepancies import *

greet()
[matrix, f] = user_input()
print("------------------------------------------------")
print("Исходная матрица: ")
print_matrix(matrix, f)
buf_matrix = []
for i in range(len(matrix)):
    buf_matrix.append(list(matrix[i]))
buf_f = list(f)
x1 = gauss_method_solution([matrix, f])
dis = get_discrepancies(buf_matrix, x1, buf_f)
x2 = gauss_method_solution_with_library([matrix, f])

for i in range(len(x1)):
    print("x[", i+1, "] =", round(x1[i], 5))
print("------------------------------------------------")
for i in range(len(dis)):
    print("r[", i+1, "] =", round(dis[i], 20))
print("------------------------------------------------")

print("Решение СЛАУ с помощью библиотеки:", x2)