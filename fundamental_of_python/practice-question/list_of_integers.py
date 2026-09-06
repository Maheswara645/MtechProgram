class IntegerList:
    def __init__(self):
        self.numbers = [10, 20, 30, 40, 50]

    def print_elements(self):
        for number in self.numbers:
            print(number)

    def print_selected_elements(self):
        print("First element:", self.numbers[0])
        print("Last element:", self.numbers[-1])
        print("Middle element:", self.numbers[len(self.numbers) // 2])


if __name__ == "__main__":
    integer_list = IntegerList()
    integer_list.print_elements()
    integer_list.print_selected_elements()