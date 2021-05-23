class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def swap_next(self, other):
        prevA, prevB = self, other
        nodeA, nodeB = self.next, other.next

        prevA.next, prevB.next = prevB.next, prevA.next
        if (nodeA and nodeB):
            nodeA.next, nodeB.next = nodeB.next, nodeA.next
        elif nodeA:
            nodeA.next = None 
        elif nodeB:
            nodeB.next = None


class LList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node

    def printll(self):
        out = ''
        node = self.head
        while node:
            out += node.data + ' '
            node = node.next
        print(out)

    def swap_kth(self, k):
        kth = n_minus_kth = None
        i = 1
        node = self.head

        while node:
            if n_minus_kth:
                n_minus_kth = n_minus_kth.next
            if i == k - 1:
                kth = node
            elif i == k + 1:
                n_minus_kth = self.head
            node = node.next
            i += 1

        if i < k:
            return

        if kth and n_minus_kth:
            print(f"k-1th element = {kth.data}, n-k-1th = {n_minus_kth.data}")
            kth.swap_next(n_minus_kth)


if __name__ == '__main__':

    llist = LList()
    [llist.append(Node(inp)) for inp in input().split()]
    print("Original list:")
    llist.printll()
    k = input()
    print("K = " + k)
    llist.swap_kth(int(k))
    print("List after swapping:")
    llist.printll()