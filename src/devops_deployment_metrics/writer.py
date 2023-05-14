# writer.py
#
# output lists of dicts to CSV files
from pathlib import Path

import pandas as pd


output_path = Path("data")
output_path.mkdir(exist_ok=True)


def write_csv(metrics: list[dict], outfile: str, date_format: str):
    # convert datetime to format
    df = pd.DataFrame.from_dict(metrics)
    df.to_csv(output_path / outfile, index=False, date_format=date_format)
