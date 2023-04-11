# writer.py
#
# output lists of dicts to CSV files
import pandas as pd


def write_csv(metrics: list[dict], outfile: str, date_format: str):
    # convert datetime to format
    df = pd.DataFrame.from_dict(metrics)
    df.to_csv(outfile, index=False, date_format=date_format)
