import concurrent.futures


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs_parallel(root, target, workers=4):
    if root is None:
        return []

    if root.value == target:
        return [root.value]

    paths = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(dfs_worker, child, target) for child in root.children]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                paths.append([root.value] + result)
                break

    return paths[0] if paths else []


def dfs_worker(node, target):
    if node.value == target:
        return [node.value]

    for child in node.children:
        path = dfs_worker(child, target)
        if path:
            return [node.value] + path

    return []


root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.children = [node2, node3]
node2.children = [node4, node6]
node3.children = [node5, node7]

resultado1 = dfs_parallel(root, 5)
print(f"Caminho até o nó 5: {resultado1}")

root2 = Node(10)
node20 = Node(20)
node30 = Node(30)
node40 = Node(40)
node50 = Node(50)
node60 = Node(60)
node70 = Node(70)
node80 = Node(80)
node90 = Node(90)

root2.children = [node20, node30]
node20.children = [node40, node50]
node30.children = [node60]
node40.children = [node70]
node60.children = [node80, node90]

resultado2 = dfs_parallel(root2, 90)
print(f"Caminho até o nó 90: {resultado2}")

resultado3 = dfs_parallel(root2, 100)
print(f"Caminho até o nó 100: {resultado3}")