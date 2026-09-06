class FruitsOperations:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry", "mango"]

    def run(self):
        print("First fruit:", self.fruits[0])
        print("Last fruit:", self.fruits[-1])
        self.fruits.insert(1, "orange")
        self.fruits.remove("banana")
        self.fruits.sort()
        self.fruits.reverse()
        return self.fruits


if __name__ == "__main__":
    print(FruitsOperations().run())