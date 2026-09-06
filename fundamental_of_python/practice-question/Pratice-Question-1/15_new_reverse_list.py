class NewReverseList:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]

    def create_reversed(self):
        return self.items[::-1]


if __name__ == "__main__":
    print(NewReverseList().create_reversed())