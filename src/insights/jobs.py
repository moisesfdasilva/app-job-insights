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
    all_jobs_types = []
    for data in data_list:
        all_jobs_types.append(data["job_type"])
    result = set(all_jobs_types)
    return result

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    all_jobs_with_a_type = []
    for job in jobs:
        if (job["job_type"] == job_type):
            all_jobs_with_a_type.append(job)
    return all_jobs_with_a_type

    raise NotImplementedError
