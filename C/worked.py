import fileinput
import re
from collections import deque


class Node:  # Вершина в бинарном дереве
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        answer = ''
        answer += '[' + str(self.key) + ' ' + self.value
        if self.parent is None:
            answer += '] '
        else:
            answer += ' ' + str(self.parent.key) + '] '
        return answer


class BinaryTree:
    def __init__(self):  # Для хранения бинарного дерева достаточно только иметь корень
        self.root = None

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            parent = None
            current = self.root
            while current is not None:  # Идем по дереву и в зависимости от значения ключа - идем
                # влево или вправо
                parent = current
                if key > current.key:
                    current = current.right
                elif key < current.key:
                    current = current.left
                else:
                    raise Exception('error')
            new_node = Node(key, value)
            new_node.parent = parent
            if key > parent.key:
                parent.right = new_node
            elif key < parent.key:
                parent.left = new_node
            else:
                raise Exception('error')

    def set(self, key, value):  # Находит искомую вершину по ключу с помощью search и изменяет значение на необходимое
        searched_node = self.search(key)
        if searched_node is None:
            raise Exception('error')
        else:
            searched_node.value = value

    def delete(self, key):  # Находит искомую вершину по ключу с помощью search и, в зависимости от ситуации,
        # верно замещает ее
        searched_node = self.search(key)
        if searched_node is None:
            raise Exception('error')
        right = searched_node.right
        left = searched_node.left
        if left is None and right is None:
            if searched_node == self.root:
                self.root = None
            elif searched_node == searched_node.parent.left:
                searched_node.parent.left = None
            elif searched_node == searched_node.parent.right:
                searched_node.parent.right = None
            else:
                raise Exception('error')
        elif left is not None and right is None:
            if searched_node == self.root:
                self.root = left
                left.parent = None
            elif searched_node == searched_node.parent.left:
                searched_node.parent.left = left
                left.parent = searched_node.parent
            elif searched_node == searched_node.parent.right:
                searched_node.parent.right = left
                left.parent = searched_node.parent
            else:
                raise Exception('error')
        elif left is None and right is not None:
            if searched_node == self.root:
                self.root = right
                right.parent = None
            elif searched_node == searched_node.parent.left:
                searched_node.parent.left = right
                right.parent = searched_node.parent
            elif searched_node == searched_node.parent.right:
                searched_node.parent.right = right
                right.parent = searched_node.parent
            else:
                raise Exception('error')
        elif left is not None and right is not None:
            current = left
            while current.right is not None:
                current = current.right
            searched_node.key = current.key
            searched_node.value = current.value
            if current.left is None:
                if current.parent.left == current:
                    current.parent.left = None
                elif current.parent.right == current:
                    current.parent.right = None
                elif searched_node == self.root:
                    searched_node.left = None
                else:
                    raise Exception('error')
            else:
                if current.parent == searched_node:
                    searched_node.left = current.left
                    current.left.parent = searched_node
                else:
                    current.parent.right = current.left
                    current.left.parent = current.parent
        else:
            raise Exception('error')

    def search(self, key, current=None):  # Поиск вершины по ключу, возвращает саму вершину, если она есть,
        # если такой вершины нет - None
        if self.root is None:
            return None
        if current is None:
            current = self.root
        if current.key == key:
            return current
        elif key < current.key:
            if current.left is not None:
                return self.search(key, current.left)
            else:
                return None
        else:
            if current.right is not None:
                return self.search(key, current.right)
            else:
                return None

    def max(self):  # Просто идет по правым потомкам до максимального эллемента
        if self.root is None:
            raise Exception('error')
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current

    def min(self):  # Просто идет по левым потомкам до минимального эллемента
        if self.root is None:
            raise Exception('error')
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current

    def __str__(self):
        return self.construct_string()

    def construct_string(self, queue=None, answer=''):
        if self.root is None:
            return '_'
        if queue is None:
            queue = deque()
            queue.append(self.root)
        new_queue = deque()
        level_line = ''
        is_next = False
        while len(queue) != 0:
            current = queue.popleft()
            if current == '_':
                new_queue.append('_')
                new_queue.append('_')
                level_line += '_ '
                continue
            else:
                level_line += str(current)
            if current.left is not None:
                is_next = True
                new_queue.append(current.left)
            else:
                new_queue.append('_')
            if current.right is not None:
                is_next = True
                new_queue.append(current.right)
            else:
                new_queue.append('_')
        answer += level_line[:-1]
        if not is_next:
            return answer
        answer += '\n'
        return self.construct_string(new_queue, answer)


def parse(input_stream):  # Обработка входных данных
    bin_tree = BinaryTree()
    for line in input_stream:
        line = line.strip('\n')
        if line == '':
            continue
        try:
            if re.match(r'^add [+-]?\d+ \S+$', line):
                command, key, value = line.split()
                bin_tree.add(int(key), value)
            elif re.match(r'^set [+-]?\d+ \S+$', line):
                command, key, value = line.split()
                bin_tree.set(int(key), value)
            elif re.match(r'^delete [+-]?\d+$', line):
                command, key = line.split()
                bin_tree.delete(int(key))
            elif re.match(r'^search [+-]?\d+$', line):
                command, key = line.split()
                node = bin_tree.search(int(key))
                print('1 ' + node.value if node is not None else '0')
            elif re.match(r'^print$', line):
                print(bin_tree)
            elif re.match(r'^max$', line):
                max_node = bin_tree.max()
                print(max_node.key, max_node.value)
            elif re.match(r'^min$', line):
                min_node = bin_tree.min()
                print(min_node.key, min_node.value)
            else:
                print("error")
        except Exception as msg:
            print(msg)


if __name__ == '__main__':
    stream = fileinput.input()
    parse(stream)
