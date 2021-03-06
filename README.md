# A Самый частый элемент массива (3 балла)
Реализуйте алгоритм поиска наиболее частого элемента массива, который работает за линейное время.

# Формат входных данных
Ввод осуществляется со стандартного потока ввода.

Первая и единственная строка всегда содержит входной массив.

Все данные гарантированно валидны, проверять данные на корректность не нужно.

# Формат результата
Результат поиска - самый частый элемент массива. Если таких чисел несколько, то наименьшее из них.

Результат работы программы выводится в стандартный поток вывода.

# B Бинарный поиск (5 баллов)
Реализуйте рекурсивно алгоритм бинарного поиска.

Реализация алгоритма должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

# Формат входных данных
Ввод осуществляется со стандартного потока ввода.

Первая строка всегда содержит отсортированный массив, в котором должен производится поиск.

Остальные строки имеют формат search K, где K - некоторое число.

Все данные гарантированно валидны, проверять данные на корректность не нужно.

# Формат результата
Результат поиска - первый индекс числа в массиве. Если число в массиве отсутствует, то результатом будет -1.

Результат работы программы выводится в стандартный поток вывода.

# C Двоичное дерево поиска (5 баллов)
Реализуйте двоичное дерево поиска.

Реализация самой структуры данных должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Тесты предполагают "левостороннюю" реализацию, т.е. если действие можно реализовать двумя симметричными способами, надо делать тот, который больше использует левую сторону.

# Формат входных данных
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются.

Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max или print, где K - целое число (64 бита вам хватит), ключ, V - произвольная строка без пробелов (значение).

# Формат результата
Команда add добавляет значение V в дерево по ключу K, set - изменяет данные по ключу, команда delete удаляет данные.

Команда search выводит либо "1 V", либо "0", где V - значение для найденного ключа.

Команды min и max выводят "K V", где K - минимальный или максимальный ключ дерева соответственно, V - значение по этому ключу.

Команда print выводит все дерево целиком.

Дерево выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень дерева в формате "[K V]" или "_", если дерево пустое.

Каждая последующая строка содержит один уровень дерева. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.

В любой непонятной ситуации результатом работы любой команды будет "error".

Результат работы программы выводится в стандартный поток вывода.

# D Быстрая сортировка (4 балла)
Реализуйте эффективный алгоритм быстрой сортировки, который обсуждался на семинаре.

# Формат входных данных
Ввод осуществляется со стандартного потока ввода.

Первая и единственная строка всегда содержит входной массив.

Все данные гарантированно валидны, проверять данные на корректность не нужно.

# Формат результата
Результат работы - отсортированный массив.

Результат работы программы выводится в стандартный поток вывода.

# E Стек на основе кучи (6 баллов)
Реализуйте стек, используя только кучу.

Стек должен работать поверх кучи и ничего не знать про детали ее реализации. Можно использовать реализацию кучи, предоставляемую стандартной библиотекой языка.

Реализации стека и кучи должны быть инкапсулированы и не зависеть от ввода/вывода.

Тесты для этого задания — такие же, как и в задаче про стек из первого модуля.

# Формат входных данных
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются.

Первая строка всегда содержит "set_size N", где N - максимальный размер стека, целое число.

Каждая последующая строка содержит ровно одну команду: push X, pop или print, где X - произвольная строка без пробелов.

# Формат результата
Команда print выводит содержимое стека (снизу вверх) одной строкой, значения разделяются пробелами. Если стек пуст, то выводится "empty".

В случае переполнения стека выводится "overflow".

Команда pop выводит элемент или "underflow", если стек пуст.

В любой непонятной ситуации результатом работы любой команды будет "error".

Результат работы программы выводится в стандартный поток вывода

# F Перестановки (5 баллов)
Реализуйте алгоритм генерации перестановок с началом в произвольной перестановке.

Реализация алгоритма должна быть инкапсулирована и не зависеть от ввода/вывода.

# Формат входных данных
На стандартном потоке ввода в первой и единственной строке задаётся перестановка — несколько чисел, разделенных пробелами.

# Формат результата
На стандартный поток вывода выводятся построчно все последующие перестановки, включая входную, в лексикографическом порядке.
