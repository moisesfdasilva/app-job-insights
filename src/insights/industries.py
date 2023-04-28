from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data_list = read(path)
    all_jobs_industries = []
    for data in data_list:
        if (data["industry"] != ""):
            all_jobs_industries.append(data["industry"])
    result = set(all_jobs_industries)
    return result

    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    all_jobs_with_a_industry = []
    for job in jobs:
        if (job["industry"] == industry):
            all_jobs_with_a_industry.append(job)
    return all_jobs_with_a_industry

    raise NotImplementedError
