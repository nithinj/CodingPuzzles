
class Node():
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

def mindepth(root):
        que = []
        depth = 0
        que.append({'node': root, 'depth': 1})

        if not root:
                return 0

        while que:
                popped = que.pop(0)

                if not popped:
                        return depth

                node = popped['node']
                depth = popped['depth']

                if ((not (node.left)) and (not (node.right))):
                        return depth

                if node.left:
                        que.append({'node': node.left, 'depth': depth + 1})
                if node.right:
                        que.append({'node': node.right, 'depth': depth + 1})


def test1():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        print(str(mindepth(root)))

def test2():
        print(str(mindepth(None)))

def test3():
        root = Node(1)
        print(str(mindepth(root)))

test1() # answer = 2
test2() # answer = 0
test3() # answer = 1

