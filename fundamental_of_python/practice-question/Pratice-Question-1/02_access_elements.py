class AccessElements:
    def __init__(self):
        self.numbers = [10, 20, 30, 40, 50]

    def run(self):
        print("First element:", self.numbers[0])
        print("Last element:", self.numbers[-1])
        print("Middle element:", self.numbers[len(self.numbers) // 2])


if __name__ == "__main__":
    AccessElements().run()