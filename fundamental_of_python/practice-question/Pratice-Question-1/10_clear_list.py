class ClearList:
    def __init__(self):
        self.items = [10, 20, 30, 40, 50]

    def clear(self):
        self.items.clear()
        return self.items


if __name__ == "__main__":
    print(ClearList().clear())