import numpy as np


def main() -> None:
    # Create two simple vectors
    v1 = np.array([1.0, 2.0, 3.0])
    v2 = np.array([2.0, 0.0, 1.0])

    print("v1 =", v1)
    print("type of v1:", type(v1))          # <class 'numpy.ndarray'>

    # Length of a vector
    length = np.linalg.norm(v1)
    print("length of v1:", length)

    # Dot product
    dot = np.dot(v1, v2)
    print("dot product:", dot)

    # Cosine similarity (the formula we use)
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    print("cosine similarity:", cos)


if __name__ == "__main__":
    main()