class GreaterThanNumber:
    def __init__(self):
        self.items = [4, 12, 7, 20, 3, 15]

    def find(self, number):
        greater_items = []
        for item in self.items:
            if item > number:
                greater_items.append(item)
        return greater_items


if __name__ == "__main__":
    print(GreaterThanNumber().find(10))