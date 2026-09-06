class AppendElement:
    def __init__(self):
        self.items = [10, 20, 30]

    def append(self, new_value):
        self.items.append(new_value)
        return self.items


if __name__ == "__main__":
    print(AppendElement().append(40))