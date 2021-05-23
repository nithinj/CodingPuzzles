class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def LCA(root, val1, val2, lca):
    
    if not root:
        return 0

    left = LCA(root.left, val1, val2, lca)
    right = LCA(root.right, val1, val2, lca)

    if left == 2 or right == 2:
        return left + right

    found = 0
    if root.data == val1 or root.data == val2:
        found = 1

    if left + right + found == 2:
        lca.append(root)

    return left + right + found

def findLevel(root, val, level):
    if not root:
        return 0

    if root.data == val:
        return level

    return findLevel(root.left, val, level + 1) + findLevel(root.right, val, level + 1)

def find_dist(root, val1, val2):
    lca = []
    LCA(root, val1, val2, lca)
    return dist(lca[0], val1, 0) + dist(lca[0], val2, 0)

def buildtree1():
    root = Node(1)
    cur = root.left = Node(2)
    cur.left = Node(4)
    cur.right = Node(5)
    cur = root.right = Node(3)
    cur.left = Node(6)
    cur.left.right = Node(8)
    cur.right = Node(7)
    return root

if __name__ == "__main__":
    root = buildtree1()
    print("Dist(4, 5) = " + str(find_dist(root, 4, 5)))
    print("Dist(4, 6) = " + str(find_dist(root, 4, 6)))
    print("Dist(3, 4) = " + str(find_dist(root, 3, 4)))
    print("Dist(2, 4) = " + str(find_dist(root, 2, 4)))
    print("Dist(8, 5) = " + str(find_dist(root, 8, 5)))
    