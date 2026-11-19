import numpy as np
from .store import VectorStore
from .search import exact_search

def main():
    store = VectorStore()
    fake_vectors = np.random.rand(10, 8).astype(np.float32)  # 10 items, 8 dimensions
    store.add_vectors(fake_vectors, ids=[f"doc_{i}" for i in range(10)])
    query = np.random.rand(8).astype(np.float32)
    results = exact_search(store, query, top_k=3)
    
    print(results)

if __name__ == "__main__":
    main()