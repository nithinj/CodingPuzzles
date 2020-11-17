class Node(object):
    def __init__(self, data):
        self.data = data
        self.visited = 0

class Matrix(object):
    def __init__(self):
        self.nrows = 0
        self.ncols = 0
        self.mat = []
        self.r = 0
        self.c = 0
        self.out = []


    def append(self, row):
        self.mat.append(row)
        self.nrows += 1
        self.ncols = len(row)

    def left(self):
        if self.c != 0:
            self.c -= 1
            if not self.mat[self.r][self.c].visited:
                return True
            else:
                self.c += 1
        return False

    def up(self):
        if self.r != 0:
            self.r -= 1
            if not self.mat[self.r][self.c].visited:
                return True
            else:
                self.r += 1
        return False

    def right(self):
        if self.c != self.ncols - 1:
            self.c += 1
            if not self.mat[self.r][self.c].visited:
                return True
            else:
                self.c -= 1
        return False

    def bottom(self):
        if self.r != rows - 1:
            self.r += 1
            if not self.mat[self.r][self.c].visited:
                return True
            else:
                self.r -= 1
        return False
    
    def output(self):
        self.out.append(self.mat[self.r][self.c].data)
        self.mat[self.r][self.c].visited = 1

    def spiralPrint(self):
        self.output()
        while len(self.out) < (self.nrows * self.ncols):
            while self.right():
                self.output()
            while self.bottom():
                self.output()
            while self.left():
                self.output()
            while self.up():
                self.output()

        print("Sprial Matrix:")
        print(str(self.out))
            

if __name__ == '__main__':
    mat = Matrix()
    rows = int(input())
    for row in range(rows):
        lst = []
        [lst.append(Node(int(inp))) for inp in input().split()]
        mat.append(lst)
    mat.spiralPrint()
    