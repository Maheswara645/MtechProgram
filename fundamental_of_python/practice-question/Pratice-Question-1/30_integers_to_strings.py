class IntegersToStrings:
    def __init__(self):
        self.numbers = [10, 20, 30, 40]

    def convert(self):
        string_values = []
        for number in self.numbers:
            string_values.append(str(number))
        return string_values


if __name__ == "__main__":
    print(IntegersToStrings().convert())