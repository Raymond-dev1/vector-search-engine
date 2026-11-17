import numpy as np

from vector_search_engine.vector import vectorize, vectorize_sentences


def test_vectorize_sentences_counts_words_and_reuses_vocabulary() -> None:
    sentences = ["Cat sat, sat.", "cat slept"]

    vectors, vocabulary = vectorize_sentences(sentences)

    assert vocabulary == {"cat": 0, "sat": 1, "slept": 2}
    np.testing.assert_array_equal(
        vectors,
        np.array([[1, 2, 0], [1, 0, 1]], dtype=np.float32),
    )
    np.testing.assert_array_equal(
        vectorize("CAT sat unknown", vocabulary),
        np.array([1, 1, 0], dtype=np.float32),
    )


def test_vectorize_sentences_handles_empty_input() -> None:
    vectors, vocabulary = vectorize_sentences([])

    assert vocabulary == {}
    assert vectors.shape == (0, 0)
