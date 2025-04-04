import threading


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_parallel(root):
    if root is None:
        return float('-inf')

    if root.left is None and root.right is None:
        return root.value

    results = [root.value]
    threads = []

    if root.left:
        left_thread = threading.Thread(target=lambda: results.append(find_max_parallel(root.left)))
        threads.append(left_thread)
        left_thread.start()

    if root.right:
        right_thread = threading.Thread(target=lambda: results.append(find_max_parallel(root.right)))
        threads.append(right_thread)
        right_thread.start()

    for thread in threads:
        thread.join()

    return max(results)


def build_tree(values):
    if not values:
        return None

    root = Node(values[0])
    for val in values[1:]:
        insert_node(root, val)

    return root


def insert_node(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert_node(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert_node(root.right, value)


tree = build_tree([15, 10, 20, 8, 12, 17, 25])
result = find_max_parallel(tree)
print(f"O valor máximo na árvore é: {result}")