from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    "Verifica se a palavra 'Job' aparece 3454 vezes no arquivo data/jobs.csv."
    output_job = {
        'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}
    response = read_brazilian_file(path="tests/mocks/brazilians_jobs.csv")
    assert response[0] == output_job
