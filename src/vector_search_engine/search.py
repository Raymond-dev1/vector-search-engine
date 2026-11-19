import numpy as np
from .store import VectorStore

def cosine_similarity(a:np.ndarray , b:np.ndarray) -> np.ndarray: 
    a_norm = a/ np.linalg.norm(a)
    b_norm =  b /np.linalg.norm(b, axis=1,keepdims=True )
    return np.dot(b_norm, a_norm)

def exact_search(store:VectorStore,query_vector:np.ndarray, top_k:int=5)->np.ndarray:
    if store.vectors is None or len(store.vectors) == 0:
        return []
    
    scores = cosine_similarity(query_vector,store.vectors )
    top_indices = np.argsort(scores)[::-1][:top_k]

    res =[]
    for idx in top_indices:
        res.append({
            "id":store.ids[idx],
            "score":float(scores[idx])
        })
