class LengthWithoutLen:
    def __init__(self):
        self.items = [4, 8, 15, 16, 23, 42]

    def find_length(self):
        count = 0
        for _ in self.items:
            count += 1
        return count


if __name__ == "__main__":
    print(LengthWithoutLen().find_length())