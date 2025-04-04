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

    if not root.children:
        return []

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        future_to_child = {executor.submit(dfs_worker, child, target): child for child in root.children}

        for future in concurrent.futures.as_completed(future_to_child):
            child = future_to_child[future]
            path = future.result()
            if path:
                return [root.value] + path

    return []


def dfs_worker(node, target):
    if node.value == target:
        return [node.value]

    for child in node.children:
        path = dfs_worker(child, target)
        if path:
            return [node.value] + path

    return []