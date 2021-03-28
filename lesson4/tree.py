"""Скрипт, который обходит дерево поиском в ширину
и вывод порядка обхода

Функции:
    bfs(tree, node_name): обход дерева поиском в ширину
    и вывод порядка обхода
"""

def bfs(tree, node_name):
    """Реализует поиск в ширину дерева с указанной вершины
    и выводит на экран порядок обхода вершин

    Аргументы:
        tree (list): список смежности
        node_name (int, string): название начальной вершины
    """
    queue = []
    queue.insert(0, node_name)
    visited = {node_name}
    path = []
    while len(queue) != 0:
        node = queue.pop()
        path.append(node)
        visited.add(node)
        for item in tree[node]:
            if item not in visited:
                queue.insert(0, item)
    return ', '.join(str(i) for i in path)


def secure_bfs(tree, node_name):
    try:
        return bfs(tree, node_name)
    except Exception:
        return "Пожалуйста, проверьте корректность введённых данных"


if __name__ == '__main__':
    print(bfs([[1], [0]], 0))

    # Пример 1
    print("Пример 1")
    tree = [[1, 2], 
            [3, 4, 0],
            [5, 0],
            [6, 7, 8, 1],
            [1],
            [2],
            [3],
            [3],
            [3]]

    print(secure_bfs(tree, 0))

    print("Пример 2")
    tree = [[1, 2], 
            [3, 4, 0],
            [5, 6, 0],
            [1],
            [7, 8, 1],
            [2],
            [2],
            [4],
            [4]]
    print(secure_bfs(tree, 5))

    print("Пример 3")
    tree = {
        'a':['b','c'],
        'b':['d', 'e', 'a'],
        'c':['f', 'g', 'a'],
        'd':['b'],
        'e':['h','i', 'b'],
        'f':['c'],
        'g':['c'],
        'h':['e'],
        'i':['e']
    }
    print(secure_bfs(tree ,'f'))