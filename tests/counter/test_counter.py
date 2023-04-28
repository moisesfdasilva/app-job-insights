from src.pre_built.counter import count_ocurrences


def test_counter():
    "Verifica se a palavra 'Job' aparece 3454 vezes no arquivo data/jobs.csv."
    assert count_ocurrences(path="data/jobs.csv", word="Job") == 3454
