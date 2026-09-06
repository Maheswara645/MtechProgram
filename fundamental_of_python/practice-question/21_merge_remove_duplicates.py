class MergeRemoveDuplicates:
    def __init__(self):
        self.first = [1, 2, 3, 4]
        self.second = [3, 4, 5, 6]

    def merge(self):
        merged = []
        for item in self.first + self.second:
            if item not in merged:
                merged.append(item)
        return merged


if __name__ == "__main__":
    print(MergeRemoveDuplicates().merge())