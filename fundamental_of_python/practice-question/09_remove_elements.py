class RemoveElements:
    def __init__(self):
        self.items = [10, 20, 30, 40, 50]

    def remove_value(self, value):
        self.items.remove(value)
        return self.items

    def remove_at_index(self, index):
        self.items.pop(index)
        return self.items


if __name__ == "__main__":
    remover = RemoveElements()
    print(remover.remove_value(30))
    print(remover.remove_at_index(1))