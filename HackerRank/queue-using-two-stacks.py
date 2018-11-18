class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __repr__(self):
        return ("stack1:" + str(self.stack1) + " stack2:" + str(self.stack2))

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            self.transfer()
        self.stack2.pop()

    def transfer(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def peek(self):
        if not self.stack2:
            self.transfer()
        return self.stack2[-1]


def process_query(queries):
    q = Queue()
    for query in queries:
        if query[0] == 1:
            q.enqueue(query[1])
        elif query[0] == 2:
            q.dequeue()
        elif query[0] == 3:
            print(str(q.peek()))


if __name__ == '__main__':
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))
    process_query(queries)
