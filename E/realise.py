import fileinput
import re


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return self.value


class MaxHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left_index(index):
        return 2 * index + 1

    @staticmethod
    def right_index(index):
        return 2 * index + 2

    def push(self, value, key):
        node = Node(key, value)
        self.data.append(node)
        current = len(self.data) - 1
        while current > 0 and self.data[current].key > self.data[self.parent(current)].key:
            self.data[current], self.data[self.parent(current)] = self.data[self.parent(current)], self.data[current]
            current = self.parent(current)

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        answer = self.data.pop()
        current = 0
        while True:
            buf = current
            if self.left_index(current) < len(self.data)\
                    and self.data[self.left_index(current)].key > self.data[buf].key:
                buf = self.left_index(current)
            if self.right_index(current) < len(self.data)\
                    and self.data[self.right_index(current)].key > self.data[buf].key:
                buf = self.right_index(current)
            if buf == current:
                break
            self.data[current], self.data[buf] = self.data[buf], self.data[current]
            current = buf
        return str(answer)


class Stack:
    def __init__(self):
        self.data = None
        self.current_size = 0
        self.max_size = None

    def set_size(self, max_size):
        if self.max_size is not None:
            raise Exception("error")
        self.max_size = max_size
        self.data = MaxHeap()

    def push(self, value):
        if self.max_size is None:
            raise Exception("error")
        if self.current_size + 1 > self.max_size:
            raise Exception("overflow")
        self.current_size += 1
        self.data.push(value, self.current_size)

    def pop(self):
        if self.max_size is None:
            raise Exception("error")
        if self.current_size == 0:
            raise Exception("underflow")
        self.current_size -= 1
        return self.data.pop()

    def __str__(self):
        if self.max_size is None:
            raise Exception("error")
        if self.current_size == 0:
            raise Exception("empty")
        array = []
        while len(self.data) > 0:
            array.append(self.data.pop())
        answer = ''
        n = len(array)
        for i in range(n - 1, -1, -1):
            answer += array[i] + ' '
            self.data.push(array[i], n - i - 1)
        return answer[:-1]


if __name__ == '__main__':
    stream = fileinput.input()
    stack = Stack()
    for line in stream:
        line = line.strip('\n')
        if line == '':
            continue
        try:
            if re.match(r'^set_size [+-]?\d+$', line):
                command, size = line.split()
                stack.set_size(int(size))
            elif re.match(r'^pop$', line):
                print(stack.pop())
            elif re.match(r'^push \S+$', line):
                command, val = line.split()
                stack.push(val)
            elif re.match(r'^print$', line):
                print(stack)
            else:
                print("error")
        except Exception as msg:
            print(msg)
