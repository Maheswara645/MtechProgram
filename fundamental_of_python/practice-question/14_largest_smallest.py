class LargestSmallest:
    def __init__(self):
        self.items = [12, 5, 27, 3, 19]

    def find(self):
        largest = self.items[0]
        smallest = self.items[0]
        for item in self.items[1:]:
            if item > largest:
                largest = item
            if item < smallest:
                smallest = item
        return largest, smallest


if __name__ == "__main__":
    largest, smallest = LargestSmallest().find()
    print("Largest:", largest)
    print("Smallest:", smallest)