class ReverseWithoutReverse:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]

    def reverse(self):
        reversed_items = []
        index = len(self.items) - 1
        while index >= 0:
            reversed_items.append(self.items[index])
            index -= 1
        return reversed_items


if __name__ == "__main__":
    print(ReverseWithoutReverse().reverse())