from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data_list = read(path)
    all_jobs_max_salaries = []
    all_exceptions = []
    for data in data_list:
        try:
            max_salary = int(data["max_salary"])
        except ValueError:
            all_exceptions.append(data["max_salary"])
        else:
            all_jobs_max_salaries.append(max_salary)

    result = max(all_jobs_max_salaries)
    print(set(all_exceptions))
    return result


def get_min_salary(path: str) -> int:
    data_list = read(path)
    all_jobs_min_salaries = []
    all_exceptions = []
    for data in data_list:
        try:
            min_salary = int(data["min_salary"])
        except ValueError:
            all_exceptions.append(data["min_salary"])
        else:
            all_jobs_min_salaries.append(min_salary)

    result = min(all_jobs_min_salaries)
    print(set(all_exceptions))
    return result


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    result = False
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary_search = int(salary)
        max(min_salary, max_salary, salary_search)
        if (min_salary > max_salary):
            raise Exception
    except Exception:
        raise ValueError
    else:
        if (min_salary <= salary_search <= max_salary):
            result = True
        else:
            result = False
    return result


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    all_jobs_in_salary_range = []
    all_exceptions = []
    for job in jobs:
        try:
            is_in_salary_range = matches_salary_range(job, salary)
        except ValueError:
            all_exceptions.append([job, salary])
        else:
            if (is_in_salary_range):
                all_jobs_in_salary_range.append(job)
    print(all_exceptions)
    return all_jobs_in_salary_range
