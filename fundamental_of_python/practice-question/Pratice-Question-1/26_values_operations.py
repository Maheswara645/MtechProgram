class ValuesOperations:
    def __init__(self):
        self.values = [3, 5, 7, 2, 10]

    def run(self):
        print("Index 0:", self.values[0])
        print("Index 2:", self.values[2])
        self.values[1] = 6
        self.values.append(12)
        del self.values[3]
        self.values.sort(reverse=True)
        return self.values


if __name__ == "__main__":
    print(ValuesOperations().run())