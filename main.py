import json  # Импортируем JSON

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
        # GET HEIGHT OF THE TREE
        def dfs(node, count):
            if not node:
                return count
            return max(dfs(node.left, count + 1), dfs(node.right, count + 1))

        height = dfs(root, -1)

        # m and n IS PROVIDED FORMULA FROM PROBLEM DESCRIPTION
        m = height + 1
        n = (2 ** (m)) - 1

        # CREATE RESULT
        result = [["" for x in range(0, n)] for x in range(0, m)]

        # r and c IS PROVIDED FORMULA FROM PROBLEM DESCRIPTION
        r = 0
        c = (n - 1) // 2

        def plot(node, r, c):
            if not node:
                return

            result[r][c] = str(node.data)

            if node.left:
                lc = c - (2 ** (height - r - 1))
                plot(node.left, r + 1, lc)

            if node.right:
                rc = c + (2 ** (height - r - 1))
                plot(node.right, r + 1, rc)

        plot(root, r, c)

        return result


# 1. Открываем файл JSON и выгружаем из него данные, затем выводим на экран
with open('my.json', 'r') as file:
    v = json.load(file)
print(type(v))
t = Tree()
for x in v:
    t.append(Node(x))
# t.show_wide_tree(t.root)
print(*t.printTree(t.root), sep="\n")

# 2. Добавляем новую ноду в бинарное дерево
number = int(input("Введите значение для добавления: "))
t.append(Node(number))
if v_can_append is False:
    v.append(number)
# t.show_wide_tree(t.root)
print(*t.printTree(t.root), sep="\n")

# 3. Производим поиск по ключу и выводим ключ на экран, если найден
key = int(input("Введите ключ для поиска: "))
t.find_node(t.root, key)

# 5. Сохраняем бинарное дерево в файл JSON
with open('my.json', 'w') as file:
    json.dump(v, file)
