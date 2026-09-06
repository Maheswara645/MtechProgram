class SecondLargest:
    def __init__(self):
        self.items = [10, 40, 20, 50, 30]

    def find(self):
        unique_items = []
        for item in self.items:
            if item not in unique_items:
                unique_items.append(item)
        unique_items.sort(reverse=True)
        if len(unique_items) < 2:
            raise ValueError("The list must contain at least two distinct values")
        return unique_items[1]


if __name__ == "__main__":
    print(SecondLargest().find())