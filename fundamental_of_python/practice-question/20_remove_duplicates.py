class RemoveDuplicates:
    def __init__(self):
        self.items = [1, 2, 2, 3, 1, 4, 3]

    def remove(self):
        unique_items = []
        for item in self.items:
            if item not in unique_items:
                unique_items.append(item)
        return unique_items


if __name__ == "__main__":
    print(RemoveDuplicates().remove())