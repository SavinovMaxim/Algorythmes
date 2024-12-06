# Лаба №17 “Операции над БНП: поиск, добавление, удаление”
# Дерево вводится в программу в формате линейно-скобочной записи.
# Затем появляется меню, в котором доступна операция добавления, удаления и поиска вершины БДП.
# После выполнения операции программа должна возвращаться снова в меню. При выходе их него до
# завершения программы на экран должно быть выведено БДН любым способом
# (в виде линейно-скобочной записи или в графической форме).
class Node:  # Класс представляет узел бинарного дерева
    def __init__(self, data):
        self.data = data  # Хранит данные узла (значение)
        self.left = None  # Левый дочерний узел
        self.right = None  # Правый дочерний узел


# Функция для добавления нового узла в дерево
def insert(root, data):
    if not root:  # Если дерево пусто, создаем новый узел
        return Node(data)

    if data < root.data:  # Если данные меньше текущего узла, идем в левое поддерево
        root.left = insert(root.left, data)
    else:  # Иначе идем в правое поддерево
        root.right = insert(root.right, data)

    return root  # Возвращаем корень дерева после вставки


# Функция для удаления узла с заданным ключом
def delete(root, key):
    if not root:  # Если узел пустой, возвращаем None (ничего не нужно удалять)
        return root

    if key < root.data:  # Если ключ меньше текущего узла, ищем в левом поддереве
        root.left = delete(root.left, key)
    elif key > root.data:  # Если ключ больше текущего узла, ищем в правом поддереве
        root.right = delete(root.right, key)
    else:  # Когда ключ найден
        # Если у узла нет левого дочернего узла
        if not root.left:
            temp = root.right  # Сохраняем правое поддерево
            root = None  # Удаляем текущий узел
            return temp  # Возвращаем правое поддерево, которое становится на место текущего узла
        # Если у узла нет правого дочернего узла
        elif not root.right:
            temp = root.left  # Сохраняем левое поддерево
            root = None  # Удаляем текущий узел
            return temp  # Возвращаем левое поддерево, которое становится на место текущего узла

        # Если у узла есть два дочерних узла
        temp = minValueNode(root.right)  # Ищем минимальное значение в правом поддереве
        root.data = temp.data  # Заменяем данные текущего узла на минимальное значение
        root.right = delete(
            root.right, temp.data
        )  # Удаляем минимальный узел из правого поддерева

    return root  # Возвращаем корень дерева после удаления


# Функция для нахождения минимального узла в дереве
def minValueNode(node):
    current = node
    # Идем по левой ветви, пока не достигнем самого левого узла
    while current.left:
        current = current.left
    return current  # Возвращаем минимальный узел


# Функция для поиска узла по ключу в дереве и возврата пути к этому узлу
def search(root, key, path=None):
    if path is None:
        path = []  # Если путь не передан, создаем пустой список для пути

    # Проверка, является ли текущий узел искомым
    if not root or root.data == key:
        if root:
            path.append(root.data)  # Добавляем найденный узел в путь
        return root, path

    path.append(root.data)  # Добавляем текущий узел в путь

    # Сначала ищем в левом поддереве, если не нашли — в правом
    if key < root.data:
        return search(root.left, key, path)  # Ищем в левом поддереве
    return search(root.right, key, path)  # Ищем в правом поддереве


# Функция для обхода дерева в центральном порядке (inorder)
def inorder(root):
    if root:
        inorder(root.left)  # Сначала обходим левое поддерево
        print(root.data, end=" ")  # Затем выводим данные текущего узла
        inorder(root.right)  # И обходим правое поддерево


# Функция для вывода меню операций с деревом
def print_menu():
    print("\nВыберите операцию:")
    print("1. Добавить вершину")  # Операция добавления узла
    print("2. Удалить вершину")  # Операция удаления узла
    print("3. Найти вершину")  # Операция поиска узла
    print("4. Вывести дерево")  # Вывод дерева
    print("5. Выйти из программы")  # Выход из программы


# Функция для вывода дерева в формате линейно-скобочной записи
def print_tree(root):
    print("\nДерево (в виде линейно-скобочной записи):")
    print_tree_format(root)


# Функция для рекурсивного вывода дерева в формате линейно-скобочной записи
def print_tree_format(root):
    if not root:  # Если узел пустой, ничего не выводим
        return
    print(root.data, end=" ")  # Выводим значение текущего узла
    if root.left or root.right:  # Если у узла есть хотя бы один потомок
        print("(", end=" ")  # Открываем скобки для вывода поддеревьев
        print_tree_format(root.left)  # Рекурсивно выводим левое поддерево
        print(", ", end=" ")  # Разделитель между левым и правым поддеревьями
        print_tree_format(root.right)  # Рекурсивно выводим правое поддерево
        print(")", end=" ")  # Закрываем скобки


# Основная функция программы
def main():
    # Инициализация дерева с несколькими вершинами
    tree = Node(8)
    tree.left = Node(3)
    tree.left.left = Node(1)
    tree.left.right = Node(6)
    tree.left.right.left = Node(4)
    tree.left.right.right = Node(7)
    tree.right = Node(10)
    tree.right.right = Node(14)
    tree.right.right.left = Node(13)

    while True:
        print_menu()  # Выводим меню операций
        choice = input("Введите номер операции: ")  # Ожидаем ввода операции

        if choice == "1":  # Добавление вершины
            value = int(
                input("Введите значение для добавления: ")
            )  # Запрашиваем значение
            tree = insert(tree, value)  # Добавляем вершину в дерево
            print("Вершина добавлена.")
        elif choice == "2":  # Удаление вершины
            value = int(
                input("Введите значение для удаления: ")
            )  # Запрашиваем значение
            tree = delete(tree, value)  # Удаляем вершину из дерева
            print("Вершина удалена.")
        elif choice == "3":  # Поиск вершины
            value = int(input("Введите значение для поиска: "))  # Запрашиваем значение
            result, path = search(tree, value)  # Ищем вершину
            if result:
                print(f"Вершина {value} найдена. Путь к вершине: {path}")
            else:
                print(f"Вершина {value} не найдена.")
        elif choice == "4":  # Вывод дерева
            print_tree(tree)  # Печатаем дерево в линейно-скобочной записи
        elif choice == "5":  # Выход из программы
            print("Выход из программы.")
            break  # Завершаем программу
        else:
            print(
                "Некорректный ввод. Попробуйте снова."
            )  # Если пользователь ввел некорректный номер операции


# Запуск программы
if __name__ == "__main__":
    main()
