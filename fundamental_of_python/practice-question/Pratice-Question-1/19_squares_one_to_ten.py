class SquaresOneToTen:
    def create(self):
        squares = []
        for number in range(1, 11):
            squares.append(number * number)
        return squares


if __name__ == "__main__":
    print(SquaresOneToTen().create())