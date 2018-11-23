class Editor:

    def __init__(self):
        self.text = []
        self.stack = []

    def __repr__(self):
        return "text: " + str(self.text)

    def append(self, word):
        self.text.extend(list(word))
        self.stack.append((1, len(word)))

    def delete(self, num):
        rem = self.text[-num:]
        self.stack.append((2, rem))
        del self.text[-num:]

    def print(self, ind):
        print(self.text[ind - 1])

    def undo(self):
        last = self.stack.pop()
        if last[0] == 1:
            del self.text[-last[1]:]
        elif last[0] == 2:
            self.text.extend(last[1])


if __name__ == '__main__':
    editor = Editor()
    n = int(input())

    for _ in range(n):
        line = input().split()
        op = line[0]
        if op == '1':
            editor.append(line[1])
        elif op == '2':
            editor.delete(int(line[1]))
        elif op == '3':
            editor.print(int(line[1]))
        elif op == '4':
            editor.undo()
