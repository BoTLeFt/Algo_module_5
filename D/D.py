import fileinput


def partition(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    support_element = array[left]
    left_border_equal = left
    right_border_equal = left
    current = left + 1
    left_border_large = right + 1

    while current != left_border_large:
        if array[current] < support_element:
            array[current], array[left_border_equal] = array[left_border_equal], array[current]
            left_border_equal += 1
            right_border_equal += 1
            current += 1
        elif array[current] > support_element:
            array[current], array[left_border_large - 1] = array[left_border_large - 1], array[current]
            left_border_large -= 1
        else:
            right_border_equal += 1
            current += 1

    return left_border_equal - 1, right_border_equal + 1


def quick_sort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        left_border, right_border = partition(array, left, right)
        quick_sort(array, left, left_border)
        quick_sort(array, right_border, right)


if __name__ == '__main__':
    stream = fileinput.input()
    for line in stream:
        if line == '\n':
            continue
        arr = list(map(int, line.split()))
        quick_sort(arr)
        print(*arr)
