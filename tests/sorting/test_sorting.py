from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    """
        Verifica se a função ordena uma lista de dicionários pelo critério
        min_salary.
    """
    input_jobs_list = read(path="data/jobs.csv")
    sort_by(jobs=input_jobs_list, criteria="min_salary")

    output_job_company = "Fort Worth Independent School District"
    response_min_salary = read(path="data/jobs.csv")

    assert output_job_company in response_min_salary[0]["company"]

    """
        Verifica se a função ordena uma lista de dicionários pelo critério
        max_salary.
    """

    sort_by(jobs=input_jobs_list, criteria="max_salary")

    output_job_company = "JPMorgan Chase"
    response_max_salary = read(path="data/jobs.csv")

    assert output_job_company in response_max_salary[0]["company"]

    """
        Verifica se a função ordena uma lista de dicionários pelo critério
        date_posted.
    """

    sort_by(jobs=input_jobs_list, criteria="date_posted")

    output_job_company = "The LiRo Group"
    response_date_posted = read(path="data/jobs.csv")

    assert output_job_company in response_date_posted[0]["company"]
