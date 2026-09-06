class CountEvenOdd:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6]

    def count(self):
        even_count = 0
        odd_count = 0
        for item in self.items:
            if item % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return even_count, odd_count


if __name__ == "__main__":
    even_count, odd_count = CountEvenOdd().count()
    print("Even:", even_count)
    print("Odd:", odd_count)