class CountElement:
    def __init__(self):
        self.items = [2, 4, 2, 6, 2, 8]

    def count(self, target):
        occurrence_count = 0
        for item in self.items:
            if item == target:
                occurrence_count += 1
        return occurrence_count


if __name__ == "__main__":
    counter = CountElement()
    print(counter.count(2))