from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as jobs_file:
        data_list = csv.DictReader(jobs_file)
        result = []
        for data in data_list:
            result.append(data)
        return result

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data_list = read(path)
    all_job_types = []
    for data in data_list:
        all_job_types.append(data["job_type"])
    result = set(all_job_types)
    return result

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
