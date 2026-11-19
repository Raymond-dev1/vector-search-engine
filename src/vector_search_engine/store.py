import numpy as np

class VectorStore:
    def __init__(self):
        self.vectors = None
        self.ids = []

    def add_vectors(self, vectors:np.ndarray, ids:list):
        if self.vectors is None:
            self.vectors = vectors
        else:
            self.vectors = np.vstack([self.vectors, vectors])
        self.ids.extend(ids)