import numpy as np


def nonzero_indices(arr):
    return np.nonzero(arr)

def identity_matrix(n):
    return np.eye(n)

def random_array(n):
    return np.random.rand(n, n, n)

def random_array1(n, m):
    a = np.random.rand(n, m)
    return np.sin(a)

def zeros_vector(n):
    return np.zeros(n)

def vector_with_one(n):
    vec = np.zeros(n)
    vec[4] = 1
    return vec

def vector_from_n_to_m(n, m):
    return np.arange(n, m+1)

def reverse_array(arr):
    return np.flip(arr)

def border_matrix(n, m):
    border = np.ones((n, m))
    border[1:-1, 1:-1] = 0
    return border

def below_diagonal_matrix(n):
    return np.tri(n, k=-1)

def chessboard_matrix(n):
    return np.indices((n, n)).sum(axis=0) % 2

def replace_max_with_zero(arr):
    arr[arr.argmax()] = 0
    return arr

def nearest_value(arr, value):
    return arr[np.abs(arr - value).argmin()]

def sum_last_two_axes(arr):
    return arr.sum(axis=(-2, -1))

def has_zero_columns(arr):
    return np.any(np.all(arr == 0, axis=0))

def subtract_mean_from_rows(matrix):
    return matrix - matrix.mean(axis=1, keepdims=True)

# Примеры использования:
n = 5
m = 10
arr = np.random.randint(0, 10, (3, 3, 3))
matrix = np.random.rand(5, 5)



# print("1. Ненулевые элементы:", nonzero_indices(arr))
# print("2. Единичная матрица:")
# print(identity_matrix(n))
# print("3. Массив со случайными значениями:")
# print(random_array(n))
# print("4. Вектор нулей размера", n, ":", zeros_vector(n))
# print("5. Вектор с единицей на пятой позиции:", vector_with_one(n))
# print("6. Вектор от n до m:", vector_from_n_to_m(n, m))
# print("7. Развернутый массив:", reverse_array(matrix))
# print("8. Матрица с границами из единиц:")
# print(border_matrix(n, m))
# print("9. Матрица с числами под диагональю:")
# print(below_diagonal_matrix(n))
# print("10. Шахматная матрица:")
# print(chessboard_matrix(n))
# print("11. Массив с заменой максимального элемента на ноль:")
# print(replace_max_with_zero(matrix))
# print("12. Ближайшее значение к 3:", nearest_value(matrix.flatten(), 3))
# print("13. Сумма по последним двум осям:", sum_last_two_axes(arr))
# print("14. Есть ли нулевые столбцы в массиве:", has_zero_columns(matrix))
# print("15. Матрица с вычтенным средним по строкам:")
# print(subtract_mean_from_rows(matrix))
