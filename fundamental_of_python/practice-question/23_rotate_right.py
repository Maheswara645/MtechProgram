class RotateRight:
    def __init__(self):
        self.items = [1, 2, 3, 4]

    def rotate(self):
        if self.items:
            return [self.items[-1]] + self.items[:-1]
        return []


if __name__ == "__main__":
    print(RotateRight().rotate())