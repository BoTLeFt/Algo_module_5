import fileinput


def next_permutation(first_permutation):  # Функция находит следующую перестановку в лексико-графическом параметре.
    # Основан на алгоритме Нараяна
    list_of_numbers = list(map(int, first_permutation.split()))
    answer = ""
    l = len(list_of_numbers)
    for i in range(l - 1, 0, -1):
        if list_of_numbers[i - 1] < list_of_numbers[i]:
            m = i
            for j in range(m, l):
                if list_of_numbers[m] >= list_of_numbers[j] > list_of_numbers[i - 1]:
                    m = j
            list_of_numbers[i - 1], list_of_numbers[m] = list_of_numbers[m], list_of_numbers[i - 1]
            j = l - 1
            while i < j:
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                i += 1
                j -= 1
            break
    for a in range(l):
        if a == l - 1:
            answer = answer + str(list_of_numbers[a])
        else:
            answer = answer + str(list_of_numbers[a]) + ' '
    return answer


if __name__ == '__main__':
    stream = fileinput.input()
    for line in stream:
        line = line.strip('\n')
        if line == '':
            continue
        list_of_first_permutation = sorted(list(map(int, line.split())))
        n = len(list_of_first_permutation)
        magic_str = ""
        for i in range(n):  # Строка необходимая для продолжения работы функции после достижения последней
            # перестановки по лексико-графическому порядку. Представляет из себя последнюю перестановку в
            # лексикографическом порядке
            if i == n - 1:
                magic_str += str(list_of_first_permutation[i])
            else:
                magic_str += str(list_of_first_permutation[i]) + ' '
        first_permutation = line
        print(first_permutation)
        new_permutation = next_permutation(first_permutation)
        while first_permutation != new_permutation and new_permutation is not None:
            if new_permutation == magic_str[::-1]:
                print(new_permutation)
                new_permutation = magic_str
            else:
                print(new_permutation)
                new_permutation = next_permutation(new_permutation)
