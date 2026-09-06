class SortAscending:
    def __init__(self):
        self.items = [5, 1, 4, 2, 3]

    def sort(self):
        self.items.sort()
        return self.items


if __name__ == "__main__":
    print(SortAscending().sort())