class SplitListHalves:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6]

    def split(self):
        middle = len(self.items) // 2
        return self.items[:middle], self.items[middle:]


if __name__ == "__main__":
    first_half, second_half = SplitListHalves().split()
    print("First half:", first_half)
    print("Second half:", second_half)