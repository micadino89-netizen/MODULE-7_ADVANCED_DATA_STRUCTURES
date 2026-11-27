class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.data)
    inorder(node.right, out)


def preorder(node, out):
    if node is None:
        return
    out.append(node.data)
    preorder(node.left, out)
    preorder(node.right, out)


def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.data)


def level_order(root):
    out = []
    if root is None:
        return out
    queue = deque([root])
    while queue:
        node = queue.popleft()
        out.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return out


def build_tree():
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(20)
    root.right.right = Node(30)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    return root


def show(label, values):
    print(f"{label}: " + " ".join(map(str, values)))


if __name__ == "__main__":
    root = build_tree()
    a, b, c = [], [], []
    inorder(root, a)
    preorder(root, b)
    postorder(root, c)
    show("Inorder", a)
    show("Preorder", b)
    show("Postorder", c)
    show("Level-order", level_order(root))
