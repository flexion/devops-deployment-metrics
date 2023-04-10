# deployments.py
#
# logic related to dealing with deployments
# and deployment metrics
import logging
import traceback
from datetime import datetime
from datetime import timedelta
from math import isnan

import pandas as pd
from github import Github
from tqdm import tqdm

# import os

# from dotenv import load_dotenv


def THE_FUTURE():
    return datetime(2100, 1, 1)


def THE_PAST():
    return datetime(1979, 1, 1)


# def read_env():
#     load_dotenv()
#     username = os.getenv("GITHUB_USERNAME")
#     password = os.getenv("GITHUB_PASSWORD")
#     return username, password


def connect_to_github(username: str, password: str) -> any:
    # user, pass_word = read_env()
    g = Github(login_or_token=username, password=password, verify=True)
    user = g.get_user()
    logging.info(user.name)
    logging.info(user.login)
    return g


def get_deployments(
    owner: str, repo: str, deployment_workflow_id: str, username: str, password: str
) -> list[dict]:
    g = connect_to_github(username, password)
    url = f"{owner}/{repo}"
    logging.info(f"repository: {url}")
    this_repo = g.get_repo(url)
    all_runs = this_repo.get_workflow_runs()
    logging.info(f"returned {all_runs.totalCount} records")
    deployment_count = 0
    successful_deployment_count = 0
    deployments = []
    for run in tqdm(all_runs):
        if str(run.workflow_id) == deployment_workflow_id:
            deployment_count += 1
            if str(run.conclusion) == "success":
                successful_deployment_count += 1
            deployment = {
                "id": str(run.id),
                "conclusion": str(run.conclusion),
                "run_started": str(run.run_started_at),
            }
            logging.info(deployment)
            deployments.append(deployment)
    # The deployment object is a dict of run_number, conclusion, run_started for a given workflow_id
    logging.info(
        f"{deployment_count} deployments with {successful_deployment_count} successes"
    )
    logging.info(f"size of deployments: {len(deployments)}")
    return deployments


def get_deployment_frequencies_and_change_failures(
    deployments: list[dict], start_of_time: datetime, time_slice: int
) -> list[dict]:
    # start_of_time = datetime(2022, 3, 23)
    end_of_time = datetime.now()
    logging.info("convert list of dict to dataframe")
    df = pd.DataFrame.from_dict(deployments)
    df["run_started"] = pd.to_datetime(df["run_started"])
    logging.info(df)
    # from start to end, find all deployments in a two-week window
    start = start_of_time
    deployment_frequencies = []
    change_failures = []
    try:
        while start < end_of_time:
            end = start + timedelta(days=time_slice)
            mask = (df["run_started"] >= start) & (df["run_started"] < end)
            slice = df.loc[mask]
            # deployment_frequency object: start, count
            count = len(slice.index)
            deployment_frequency = {"date": start, "count": count}
            logging.info(f"d {deployment_frequency}")
            deployment_frequencies.append(deployment_frequency)
            failures = len(slice[slice["conclusion"] == "failure"])
            failure_percent = failures / count if count else 0
            change_failure = {"date": start, "percent": failure_percent}
            change_failures.append(change_failure)
            logging.info(f"c {change_failures}")
            start = end
    except:  # noqa: E722
        traceback.print_exc()
        exit(1)
    return deployment_frequencies, change_failures


def all_get_mttrs(deployments: list[dict]) -> list[dict]:
    logging.info("convert list of dict to dataframe")
    df = pd.DataFrame.from_dict(deployments)
    df["run_started"] = pd.to_datetime(df["run_started"])
    df.sort_values(by="run_started", inplace=True)
    last_failure = THE_FUTURE()
    last_success = THE_PAST()
    mttrs = []
    for row in df.itertuples(index=False, name="Pandas"):
        logging.debug(row)
        this_time = row.run_started
        conclusion = row.conclusion
        if conclusion == "failure" and last_failure > this_time:
            last_failure = this_time
        if conclusion == "success" and last_success < this_time:
            last_success = this_time
        logging.info(
            f"this_time: {this_time} last_success: {last_success} last_failure: {last_failure}"
        )
        if last_success > last_failure:  # We have resolved the issue
            mttr_duration = last_success - last_failure
            logging.info(f"mttr! {mttr_duration}")
            mttr_seconds = int(mttr_duration.total_seconds()) / 3660
            logging.info(f"{this_time}, {mttr_seconds}")
            last_failure = THE_FUTURE()
            mttr = {"date": this_time, "mttr": mttr_seconds}
            mttrs.append(mttr)
    return mttrs


def collate_mttrs(
    all_mttrs: list[dict], start_of_time: datetime, time_slice: int
) -> list[dict]:
    end_of_time = datetime.now()
    logging.info("convert list of dict to dataframe")
    df = pd.DataFrame.from_dict(all_mttrs)
    df["date"] = pd.to_datetime(df["date"])
    logging.info(df)
    # from start to end, find all deployments in a two-week window
    start = start_of_time
    mttrs = []
    try:
        while start < end_of_time:
            end = start + timedelta(days=time_slice)
            mask = (df["date"] >= start) & (df["date"] < end)
            slice = df.loc[mask]
            # mttr object: start, mttr
            mean_mttr = slice["mttr"].mean()
            mean_mttr = 0.0 if isnan(mean_mttr) else mean_mttr
            mttr = {"date": start, "mttr": mean_mttr}
            logging.info(f"{mttr}")
            mttrs.append(mttr)
            start = end
    except:  # noqa: E722
        traceback.print_exc()
        exit(1)
    return mttrs
