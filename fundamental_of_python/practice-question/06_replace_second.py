class ReplaceSecond:
    def __init__(self):
        self.items = [10, 20, 30, 40, 50]

    def replace(self, new_value):
        self.items[1] = new_value
        return self.items


if __name__ == "__main__":
    print(ReplaceSecond().replace(99))