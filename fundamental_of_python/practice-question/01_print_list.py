class PrintList:
    def __init__(self):
        self.numbers = [10, 20, 30, 40, 50]

    def run(self):
        for number in self.numbers:
            print(number)


if __name__ == "__main__":
    PrintList().run()