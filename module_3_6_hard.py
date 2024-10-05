
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

#Функция isinstance() в Python, принадлежность экземпляра к классу

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data_structure, *args):     #функция, содержащая параметр, переменную (data_structure)
    sum_1 = 0

    if isinstance(data_structure, (list, set, tuple)):  #если в переменной(data_structure) есть список(list), тогда
        for i in data_structure:                        #для переменной(i) в переменной(data_structure) сумма(sum_1)
            sum_1 += calculate_structure_sum(i)         #будет увеличиваться на значения в списке[1, 2, 3], поочереди

    elif isinstance(data_structure, dict):              #если же в переменной(data_structure) есть словарь(dict), то
        for key, value in data_structure.items():       #тогда перебираем значения словаря и возвращаем методом (items)
            sum_1 += calculate_structure_sum(len(key))  #все пары(key, value) в переменную сумме(sum_1), считая каждый
            sum_1 += calculate_structure_sum(value)     #символ ключа числом

    elif isinstance(data_structure, (int, float)):      #если же в переменной(data_structure) есть целое число(int), или
        sum_1 += data_structure                         #число с плавающей запятой(float), тогда это число записываем
                                                        #в переменную сумме(sum_1)

    elif isinstance(data_structure, str):               #если же в переменной(data_structure) есть строки(str), тогда
        sum_1 += len(data_structure)                    #c помощью метода(len) возвращаем каждый символ строки в
                                                        #в переменную сумме(sum_1)

    return sum_1                                        #когда все значения в переменной(data_structure) перебраны и
                                                        #добавлены(подсчитаны) в переменную(sum_1), тогда возвращаем эту
                                                        #переменную в функцию(calculate_structure_sum(data_structure))

result = calculate_structure_sum(data_structure)
print(result)

