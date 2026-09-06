class CheckElement:
    def __init__(self):
        self.items = [10, 20, 30, 40, 50]

    def exists(self, target):
        for item in self.items:
            if item == target:
                return True
        return False


if __name__ == "__main__":
    checker = CheckElement()
    print(checker.exists(30))