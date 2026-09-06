class InsertElement:
    def __init__(self):
        self.items = [10, 20, 40, 50]

    def insert(self, position, value):
        self.items.insert(position, value)
        return self.items


if __name__ == "__main__":
    print(InsertElement().insert(2, 30))