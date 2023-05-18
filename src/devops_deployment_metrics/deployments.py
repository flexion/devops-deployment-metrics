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


def THE_FUTURE():
    return datetime(2100, 1, 1)


def THE_PAST():
    return datetime(1979, 1, 1)


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
