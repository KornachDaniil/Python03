import json  # Импортируем JSON
import math

v_can_append = False


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):  # Функция поиска
        if node is None:
            return None, parent, False

        if value == node.data:
            global v_can_append
            v_can_append = True
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):  # Функция для добавления новой ноды
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    # def __find_min(self, node, parent):  # Хз зачем это тут
    #     if node.left:
    #         return self.__find_min(node.left, node)
    #
    #     return node, parent

    def find_node(self, root, key):  # Функция для поиска ноды
        if root is None:
            return

        if key == root.data:
            print("Ключ найден: ", root.data)
            return

        if root.left:
            self.find_node(root.left, key)

        if root.right:
            self.find_node(root.right, key)

    def printTree(self, root):
        def height(ro):
            if not ro:
                return 0

            l = ro.left
            r = ro.right
            if height(l) > height(r):
                return 1 + height(l)
            else:
                return 1 + height(r)

        def make(root, i, j):
            if root:
                l[i][j] = str(root.data)
                j_left = int(j - 2 ** (h - i - 1))
                j_right = int(j + 2 ** (h - i - 1))
                i = i + 1
                make(root.left, i, j_left)
                make(root.right, i, j_right)

        h = height(root) - 1
        m = h + 1
        n = 2 ** (m) - 1
        l = [["" for j in range(n)] for i in range(m)]

        i = 0
        j = int((n - 1) / 2)
        make(root, i, j)
        return l


# 1. Открываем файл JSON и выгружаем из него данные, затем выводим на экран
with open('my.json', 'r') as file:
    v = json.load(file)
print(type(v))
t = Tree()
for x in v:
    t.append(Node(x))
# t.show_wide_tree(t.root)
print(*t.printTree(t.root), sep='\n')  # * используется для распаковки элементов списка и передачи их как аргументов функции

# 2. Добавляем новую ноду в бинарное дерево
number = int(input("Введите значение для добавления: "))
t.append(Node(number))
if v_can_append is False:
    v.append(number)
#t.show_wide_tree(t.root)

# 3. Производим поиск по ключу и выводим ключ на экран, если найден
# key = input("Введите ключ для поиска: ")
# t.find_node(t.root, key)

print(*t.printTree(t.root), sep='\n')  # * используется для распаковки элементов списка и передачи их как аргументов функции

# 5. Сохраняем бинарное дерево в файл JSON
with open('my.json', 'w') as file:
    json.dump(v, file)
