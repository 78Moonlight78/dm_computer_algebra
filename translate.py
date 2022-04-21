def input_nat(text):
    new_arr = [int(i)for i in list(text)]
    return [len(text), new_arr]

def input_int(text):
    text = list(text)
    sign = 0
    if "-" in text:
        sign = 1
        text = [int(text[i]) for i in range(1, len(text))]
    elif "+" in text:
        sign = 0
        text = [int(text[i]) for i in range(1, len(text))]
    else:
        text = [int(i) for i in list(text)]
    return [sign, len(text), text]


def input_rational(text):
    i = 0
    if '/' in text:
        while text[i] != '/':
            i += 1
        return [*input_int(text[:i]), *input_nat(text[i+1:])]
    else:
        return [*input_int(text), 1, [1]]


def input_polynom(text1, text2):
    dict_pol = {}
    max_rang = 0
    arr = []
    text1, text2 = text1.split(), text2.split()
    if len(text1) == len(text2):
        for i in range(len(text1)):
            if text1[i] not in dict_pol.keys():
                if max_rang < int(text1[i]):
                    max_rang = int(text1[i])
                dict_pol[text1[i]] = text2[i]
            else:
                return False
    for i in range(max_rang, -1, -1):
        if str(i) in dict_pol.keys():
            if '/' in dict_pol[str(i)]:
                arr.append(input_rational(dict_pol[str(i)]))
            else:
                arr.append(input_int(dict_pol[str(i)]) + [1, [1]])
        else:
            arr.append([0, 1, [0], 1, [1]])
    return [max_rang, arr]


def output_nat(arr):
    return ("").join([str(i) for i in arr[1]])

def output_int(arr):
    if arr[0] == 0:
        return ("").join(["+"]+[str(i) for i in arr[2]])
    else:
        return ("").join(["-"]+[str(i) for i in arr[2]])

def output_rational(arr):
    return (output_int(arr[0:3]) + '/' + output_nat(arr[3:]))

def output_pol(arr):
    text = ''
    print(arr)
    max_rang, arr = arr
    for i in range(len(arr)):
        if [0, 1, [0], 1, [1]] != arr[i] and [1, 1, [0], 1, [1]] != arr[i]:
            if arr[i][3] != 1 and arr[i][4] != [1]:
                text += output_rational(arr[i]) + 'x^' + str(max_rang - i)
            else:
                text += output_int(arr[i][:4]) + 'x^' + str(max_rang - i)
    return text

