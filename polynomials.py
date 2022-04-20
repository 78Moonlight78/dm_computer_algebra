from rational import *


# P-1
def ADD_PP_P(m1, P1, m2, P2):
    i = 0
    diff = abs(m1 - m2)
    res = [max(m1, m2), []]

    while i < diff:  # Добавялем в конечный многочлен те элементы, у которых нет пары с одинаковыми степенями.
        p = P1 if m1 > m2 else P2
        res[1] += [p[i]]
        i += 1

    i = 0

    while i <= min(m1, m2):  # Складываем элементы с одинаковыми степенями.
        if m1 >= m2:
            res[1] += [ADD_QQ_Q(P1[i + diff], P2[i])]
        else:
            res[1] += [ADD_QQ_Q(P1[i], P2[i + diff])]
        i += 1
    return res


# P-2
def SUB_PP_P(a, A, b, B):
    # Узнаём максимальную степень среди наших многочленов
    max_degree = max(a, b)
    # В зависимости от того, у какого многочлена больше старшая степень, добавляем к оставшемуся необходимое количество 'нулевых' коэффициентов.
    # К примеру, если у многочлена A старшая степень равна 5, а у многочлена B - 3, то мы добавляем к B два 'нулевых' коэффициента(в начало).
    if (a > b):
        differennce = a - b
        for i in range(differennce):
            B.insert(0, [0, 1, [0], 1, [1]])
    else:
        differennce = b - a
        for i in range(differennce):
            A.insert(0, [0, 1, [0], 1, [1]])
    result = []
    # Используем функцию SUB_QQ_Q() и заполняем массив result
    for i in range(max_degree + 1):
        result += [SUB_QQ_Q(A[i], B[i])]

    return max_degree, result


# P-3
def MUL_PQ_P(m, C, n):  # Домножение многочлена на рац. число
    for i in range(m + 1):  # Цикл по всем коэффициентам многочлена
        C[i] = MUL_QQ_Q(C[i], n)  # Функция перемножения рационального числа на рациональное число
    return [m, C]


# P-4
def MUL_Pxk_P(m, C, k):  # Умножение полинома на x^k:
    for i in range(k):  # k раз добавляем 0 в самый маленький разряд,
        C.append([0, 1, [0], 1, [1]])  # сдвигая другие разряды в большую сторону.
    m += k  # Не забываем увеличить степень.
    return [m, C]


# P-5
def LED_P_Q(C):
    return C[0]


# P-6
def DEG_P_N(mass):
    return len(mass) - 1


# P-7
def FAC_P_Q(C):
    A = [0]     # НОК и НОД не могут быть отрицательными
    numers = []     # числители
    denoms = []     # знаменатели
    for i in range(1, C[0] + 2):
        numers.append(C[i][1:1 + 2])
        denoms.append(C[i][3:3 + 2])
    a = GCF_NN_N(numers[0][0], numers[0][1], numers[1][0], numers[1][1])    # пара в числителе и зн-ле точно будет
    b = LCM_NN_N(denoms[0][0], denoms[0][1], denoms[1][0], denoms[1][1])
    if len(numers) > 2:
        for i in range(2, len(numers)):
            a = GCF_NN_N(a[0], a[1], numers[i][0], numers[i][1])
    if len(denoms) > 2:
        for i in range(2, len(denoms)):
            b = LCM_NN_N(b[0], b[1], denoms[i][0], denoms[i][1])
    for i in range(2):   # наверное можно проще
        A.append(a[i])
    for i in range(2):
        A.append(b[i])
    return A
# P-8 / MUL_PP_P
# Использованные модули: MUL_QQ_Q, ADD_PP_P
# Выполнил: Волосевич А.Н. (1310)
def MUL_PP_P(m1: int, C1: list, m2: int, C2: list) -> tuple:

    # Определене степени итогового многочлена
    res_m = m1 + m2

    # Определение итогового многочлена (пока состоящего из нулей)
    res_C = [[0, 1, [0], 1, [1]]] * (res_m + 1)


    # Перемножение элементов исходных массивов с помощью 2х циклов for:

    for ind_1 in range(m1+1): # Цикл по первому исходному массиву

        # Определене степени промежуточного многочлена
        mid_m = m1 + m2 - ind_1

        # Определение промежуточного многочлена
        mid_C = [[0, 1, [0], 1, [1]]] * (mid_m + 1)

        for ind_2 in range(m2+1): # Цикл по второму исходному массиву

            # Сохранение промежуточного результа
            mid_C[ind_2] =  MUL_QQ_Q(C1[ind_1], C2[ind_2]) # Перемножение коэффициентов

        # Сумма каждого промежуточного результата с текущим многочленом:
        res_m, res_C = ADD_PP_P(res_m, res_C, mid_m, mid_C)

    return res_m, res_C
# P-9
# P-10
# P-11
"""def GCF_PP_P(m1, C1, m2, C2):
    if m2 > m1:
        m1, m2 = m2, m1
        C1, C2 = C2, C1

    m3, C3 = MOD_PP_P(m1, C1, m2, C2)

    # Будем осуществлять деление до тех пор, пока остаток не равен нулю
    # 0 = 0, [0, 1, [0], 1, [1]]
    while m3 != 0 or C3 != [0, 1, [0], 1, [1]]:
        m1, C1 = m2, C2
        m2, C2 = m3, C3
        m3, C3 = MOD_PP_P(m1, C1, m2, C2)

    # Последний делитель(m2, C2) будет нашим НОД

    # Узнаем степень многочлена
    m2 = DEG_P_N(C2)
    if m2 == 0:
        C2[0] = 0
    return [m2, C2]
"""

# P-12
def DER_P_P(k, arr):
    for i in range(k, -1, -1):
        arr[k - i] = MUL_QQ_Q([0, 1, [i], 1, [1]], arr[k - i])
    arr = arr[0:-1]
    return [k - 1, arr]
# P-13
