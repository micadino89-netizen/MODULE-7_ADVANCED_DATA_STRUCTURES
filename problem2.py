class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def iterative_size(root):
    if root is None:
        return 0
    queue, count = [root], 0
    while queue:
        node = queue.pop(0)
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count


if __name__ == "__main__":
    root = Node(15)
    root.left, root.right = Node(10), Node(25)
    root.left.left, root.left.right = Node(4), Node(12)
    root.right.left, root.right.right = Node(20), Node(30)
    root.left.left.left, root.left.left.right = Node(2), Node(6)

    print("size =", size(root))
    print("height =", height(root))
    print("iterative_size =", iterative_size(root))
