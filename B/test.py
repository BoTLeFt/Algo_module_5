import fileinput
import re


class Array:
    def __init__(self, list_of_data):
        self.data = list_of_data

    def bin_search(self, element, left=None, right=None):  # Функция бинарного поиска. Начальное положение - начало
        # в начале массива, конец в конце массива
        if left is None:
            left = 0
        if right is None:
            right = len(self.data) - 1
        if left > right:
            return -1
        current = (left + right) // 2  # Средний элемент, проверяем, больше или меньше заданого элемента
        if self.data[current] > element:
            right -= 1  # Если средний элемент больше заданого - двигаем правую
            # границу к среднему-1 (чтобы избежать зацикливания)
        elif self.data[current] < element:  # Если средний элемент больше заданого - двигаем правую границу к
            # среднему+1 (чтобы избежать зацикливания)
            left += 1
        else:
            while current != 0 and self.data[current - 1] == self.data[current]:  # Механизм для нахождения первого
                # вхождения искомого числа в массив. В условии об этом не сказано, но тест 14 это проверяет
                current -= 1
            return current
        return self.bin_search(element, left, right)


if __name__ == '__main__':
    stream = fileinput.input()
    buffer_list = []
    array = Array(buffer_list)
    for line in stream:
        if line == '\n':
            continue
        if re.match(r'^search [+-]?\d+$', line):
            command, element_for_search = line.split()
            print(array.bin_search(int(element_for_search)))
        else:
            buffer_list = list(map(int, line.split()))
            array = Array(buffer_list)
