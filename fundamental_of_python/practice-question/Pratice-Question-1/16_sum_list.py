class SumList:
    def __init__(self):
        self.items = [10, 20, 30, 40]

    def calculate(self):
        total = 0
        for item in self.items:
            total += item
        return total


if __name__ == "__main__":
    print(SumList().calculate())