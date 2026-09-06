"""NumPy practice questions: array creation, attributes, operations, and slicing."""

import numpy as np


def main():
    # 1. Create a NumPy array from a Python list.
    numbers = np.array([10, 20, 30, 40])
    print("Array from list:", numbers)

    # 2. Arrays of zeros and ones.
    zeros = np.zeros(5, dtype=int)
    ones = np.ones((3, 3), dtype=int)
    print("\nZeros:", zeros)
    print("Ones:\n", ones)

    # 3. Array attributes.
    print("\nAttributes of ones array")
    print("ndim :", ones.ndim)
    print("shape:", ones.shape)
    print("size :", ones.size)
    print("dtype:", ones.dtype)

    # 4. Other ways to create arrays.
    print("\narange(1, 10):", np.arange(1, 10))
    print("linspace(0, 1, 5):", np.linspace(0, 1, 5))

    # 5 and 6. Element-wise operations and vectorization.
    first = np.array([10, 20, 30])
    second = np.array([1, 2, 3])
    print("\nAddition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    print("First array multiplied by 2:", first * 2)

    # 7. Aggregate operations.
    print("\nMean:", numbers.mean())
    print("Sum:", numbers.sum())
    print("Maximum:", numbers.max())
    print("Minimum:", numbers.min())

    # 8. Indexing and slicing.
    print("\nFirst 3 elements:", numbers[:3])
    print("Last 2 elements:", numbers[-2:])

    # 9. Reshape a 1D array into a 2 x 3 matrix.
    matrix = np.arange(1, 7).reshape(2, 3)
    print("\n2 x 3 matrix:\n", matrix)

    # 10. Matrix addition (same shape is required).
    matrix_two = np.array([[10, 20, 30], [40, 50, 60]])
    print("Matrix addition:\n", matrix + matrix_two)


if __name__ == "__main__":
    main()
