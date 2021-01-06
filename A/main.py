import fileinput


class Array:
    def __init__(self, list_of_data):
        self.data = list_of_data

    def search_of_most_common(self):
        dict_of_array = dict()
        for i in self.data:  # Создание словаря по входному массиву. Ключ - эллемент массива, значение - число вхождений
            if not (i in dict_of_array):
                dict_of_array[i] = 1
            else:
                dict_of_array[i] += 1
        max_value = None
        min_key = None
        for i in dict_of_array.keys():  # Приход по всему словарю
            if (max_value is None) or (dict_of_array[i] > max_value):  # Если значение ключа больше, чем максимально
                # зайденное - присваиваем максимальному значению значение данного ключа, при этом присваиваем
                # минимальному ключу нынешний
                max_value = dict_of_array[i]
                min_key = i
            elif max_value == dict_of_array[i]:  # Если значение ключа такое же, как минимальное - сравниваем ключи и
                # находим минимальный
                if (min_key is None) or (min_key > i):
                    min_key = i
        return min_key


def parse(input_stream):  # Обработка входных данных
    buffer_list = []
    for line in input_stream:
        if line == '\n':
            break
        line = line.replace('\n', '')
        buffer_list = list(map(int, line.split()))
    array = Array(buffer_list)
    print(array.search_of_most_common())


if __name__ == '__main__':
    stream = fileinput.input()
    parse(stream)
