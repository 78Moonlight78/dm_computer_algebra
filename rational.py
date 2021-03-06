from integer import *

# Q-1 "Сокращение дроби"
# автор: Пелагейко Анастасия, 1310
def RED_Q_Q(Q):
    # получаем абсолютное число числителя (получаем натуральное число),
    # используя функцию, возвращающую абсолютную величину числа, 'ABS_Z_N' (результат - натуральное)
    Q[1], Q[2] = ABS_Z_N(Q[0], Q[1], Q[2])

    # получаем НОД числителя и знаменателя,
    # используя функцию, возварщающую НОД натуральных чисел, 'GCF_NN_N'
    # cA - количество цифр в НОД числителя и знаменателя, nodA - массив чисел НОД-а,
    cA, nodA = GCF_NN_N(Q[1], Q[2], Q[3], Q[4])

    # делим абстолютное значение чилителя и знаменатель на НОД числителя и знаменателя,
    # используя функцию, возвращающую частное от деления целого на целое, 'DIV_ZZ_Z'
    # т.к. знаменатель - натуральное, а в ф-ии 'DIV_ZZ_Z' - целое, то в качестве знака знаменателя передаём 0
    Q[1], Q[2] = DIV_NN_N(Q[1], Q[2], cA, nodA)
    Q[3], Q[4] = DIV_NN_N(Q[3], Q[4], cA, nodA)

    # возвращаем сокращённую дробь
    return Q


# Задача Q-2: "Проверка рационального числа на целое"
# Выполнил Богданов Г.В.
def INT_Q_B(Q):
    return 1 if Q[3] == 1 and Q[4][0] == 1 else 0


# Преобразование целого в дробное(Q-3)
# Выполнил: Ескин Кирилл
def TRANS_Z_Q(b1, n1, A1):
  return [b1, n1, A1, 1, [1]]

# Задача Q-4: "Преобразование дробного в целое (если знаменатель равен 1)"
# Выполнил Данилов А.С.
def TRANS_Q_Z(Q):
    return [Q[0], Q[1], Q[2]] if Q[3] == 1 and Q[4][0] == 1 else 0


# Q-5
# Выполнил Богданов Г.В.
def ADD_QQ_Q(Q1, Q2):
    denominator = LCM_NN_N(Q1[3], Q1[4], Q2[3], Q2[4])

    num1 = DIV_NN_N(denominator[0], denominator[1], Q1[3], Q1[4])
    num1 = TRANS_N_Z(num1[0], num1[1])
    minuend = MUL_ZZ_Z(Q1[0], Q1[1], Q1[2], num1[0], num1[1], num1[2])

    num2 = DIV_NN_N(denominator[0], denominator[1], Q2[3], Q2[4])
    num2 = TRANS_N_Z(num2[0], num2[1])
    subtrahend = MUL_ZZ_Z(Q2[0], Q2[1], Q2[2], num2[0], num2[1], num2[2])

    numerator = ADD_ZZ_Z(minuend[0], minuend[1], minuend[2], subtrahend[0], subtrahend[1], subtrahend[2])

    result = RED_Q_Q([numerator[0], numerator[1], numerator[2], denominator[0], denominator[1]])

    return result


#Q-6
# Выполнил Данилов А.С.
def SUB_QQ_Q(Q1, Q2):
    if Q1 == [0, 1, [0], 1, [1]]:
        number = MUL_ZM_Z(Q2[0], Q2[1], Q2[2]) # умножение числителя второй дроби на (-1).
        return [number[0], number[1], number[2], Q2[3], Q2[4]]
    elif Q2 == [0, 1, [0], 1, [1]]:
        return Q1
    else:
        # denominator (с англ. знаменатель) является знаменателем искомой дроби и представляет собой НОК
        # знаменателей исходных дробей. denominator - натуральное число, которое хранится в виде массива, где
        # первый элемент массива - количество разрядов, а второй - массив чисел натурального числа.
        denominator = LCM_NN_N(Q1[3], Q1[4], Q2[3], Q2[4])
        # minued (с англ. уменьшаемое) находится как произведение числителя первой дроби и частного НОКа и знаменателя
        # первой дроби (другими словами, приводим дроби к общему знаменателю).
        number1_N = DIV_NN_N(denominator[0], denominator[1], Q1[3], Q1[4])
        # натуральное число приводим в целому, чтобы умножить целое на целое.
        number1_Z = TRANS_N_Z(number1_N[0], number1_N[1])
        minuend = MUL_ZZ_Z(Q1[0], Q1[1], Q1[2], number1_Z[0], number1_Z[1], number1_Z[2])

        # аналогично находим subtrahend (вычитаемое)
        number2_N = DIV_NN_N(denominator[0], denominator[1], Q2[3], Q2[4])
        number2_Z = TRANS_N_Z(number2_N[0], number2_N[1])
        subtrahend = MUL_ZZ_Z(Q2[0], Q2[1], Q2[2], number2_Z[0], number2_Z[1], number2_Z[2])

        # Уменьшаемое (minuend) - вычитамое (subtrahend) = разность,что есть искомый числитель (с англ. numerator)
        numerator = SUB_ZZ_Z(minuend[0], minuend[1], minuend[2], subtrahend[0], subtrahend[1], subtrahend[2])

        # Теперь у нас есть числитель (numerator) и знаменатель (denominator) искомой дроби.
        # Сократим получившуюся дробь (если возможно) и вернем результат работы функции.
        result = RED_Q_Q([numerator[0], numerator[1], numerator[2], denominator[0], denominator[1]])

        return result


#Q-7
#Выполнила Прокофьева Ксения
def MUL_QQ_Q(A, B):
    # Умножаем дроби (числитель первой умножаенаем на числитель второй, знаменатель первой умножаем на знаменатель второй) используя функцию MUL_ZZ_Z.
    # Используем срез, чтобы присвоить переменной amount2 номер старшей позиции, а переменной number2 - массив цифр
    sign, amount1, number1 = MUL_ZZ_Z(A[0], A[1], A[2], B[0], B[1], B[2])
    amount2, number2 = MUL_ZZ_Z(0, A[3], A[4], 0, B[3], B[4])[1:]
    # Сокращаем дробь
    result = RED_Q_Q([sign, amount1, number1, amount2, number2])
    return result

# Задача Q-8: Деление дробей (делитель отличен от нуля)
# Выполнил Чибисов А.А.
def DIV_QQ_Q(A, B):
    # Делим дроби(числитель первой умножаенаем на знаменатель второй, знаменатель первой умножаем на числитель второй) используя функцию MUL_ZZ_Z.
    # Используем срез, чтобы присвоить переменной amount2 номер старшей позиции, а переменной number2 - массив цифр
    sign, amount1, number1 = MUL_ZZ_Z(A[0], A[1], A[2], B[0], B[3], B[4])
    amount2, number2 = MUL_ZZ_Z(0, B[1], B[2], 0, A[3], A[4])[1:]
    # Сокращаем дробь
    result = RED_Q_Q([sign, amount1, number1, amount2, number2])
    return result

print(ADD_QQ_Q([0, 1, [1], 1, [2]], [0, 1, [1], 1, [2]]))