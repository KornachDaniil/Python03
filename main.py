import json  # Импортируем JSON


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

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)
        # print(node.data)

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

    def __del_leaf(self, s, p):  # Функция для удаления листьев
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):  # Функция для удаления одной ноды
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                s.right = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                s.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):  # Главная функция для удаления элементов бинарного дерева
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)

        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

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


# 1. Открываем файл JSON и выгружаем из него данные, затем выводим на экран
with open('my.json', 'r') as file:
    v = json.load(file)
print(type(v))
t = Tree()
for x in v:
    t.append(Node(x))
t.show_wide_tree(t.root)

# 2. Добавляем новую ноду в бинарное дерево
number = int(input("Введите значение для добавления: "))
v.append(number)
t.append(Node(number))
t.show_wide_tree(t.root)

# 3. Производим поиск по ключу и выводим ключ на экран, если найден
key = int(input("Введите ключ для поиска: "))
t.find_node(t.root, key)

# 4. Производим удаление ноды по ключу и выводим дерево на экран
key = int(input("Введите ключ для удаления: "))
t.del_node(key)
v.remove(key)
t.show_wide_tree(t.root)

# 5. Сохраняем бинарное дерево в файл JSON
with open('my.json', 'w') as file:
    json.dump(v, file)
