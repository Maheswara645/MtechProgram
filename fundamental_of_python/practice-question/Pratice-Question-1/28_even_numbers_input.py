class EvenNumbersInput:
    def get_even_numbers(self, numbers):
        even_numbers = []
        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
        return even_numbers

    def run(self):
        values = input("Enter integers separated by spaces: ")
        numbers = [int(value) for value in values.split()]
        print(self.get_even_numbers(numbers))


if __name__ == "__main__":
    EvenNumbersInput().run()