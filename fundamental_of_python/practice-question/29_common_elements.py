class CommonElements:
    def __init__(self):
        self.first = [1, 2, 3, 4, 5]
        self.second = [3, 4, 5, 6, 7]

    def find(self):
        common = []
        for item in self.first:
            if item in self.second and item not in common:
                common.append(item)
        return common


if __name__ == "__main__":
    print(CommonElements().find())