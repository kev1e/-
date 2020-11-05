class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left > self.right:
            print("L")
        elif self.left < self.right:
            print("R")
