import re
from collections.abc import Mapping, Sequence

import numpy as np





# def _tokenize(text: str) -> list[str]:
#     return re.findall(r"\b\w+\b", text.lower())


# def build_vocabulary(sentences: Sequence[str]) -> dict[str, int]:
#     words = sorted({word for sentence in sentences for word in _tokenize(sentence)})
#     return {word: index for index, word in enumerate(words)}


# def vectorize(sentence: str, vocabulary: Mapping[str, int]) -> np.ndarray:
#     vector = np.zeros(len(vocabulary), dtype=np.float32)
#     for word in _tokenize(sentence):
#         index = vocabulary.get(word)
#         if index is not None:
#             vector[index] += 1
#     return vector


# def vectorize_sentences(
#     sentences: Sequence[str],
# ) -> tuple[np.ndarray, dict[str, int]]:
#     vocabulary = build_vocabulary(sentences)
#     vectors = np.zeros((len(sentences), len(vocabulary)), dtype=np.float32)
#     for row, sentence in enumerate(sentences):
#         vectors[row] = vectorize(sentence, vocabulary)
#     return vectors, vocabulary
