# test_writer
from pathlib import Path

import pandas
from devops_deployment_metrics import writer


def test_write_csv(mocker) -> None:
    """Does it call pandas to_csv?"""
    # Given
    # mocker.patch("Pandas.to_csv", return_value=None)
    test_list = [{"foo": "bar"}, {"baz": "qux"}]
    outfile = "quux"
    date_format = "date-format"
    # When
    ext = mocker.patch("pandas.DataFrame.to_csv")
    writer.write_csv(test_list, outfile, date_format)
    # Then
    assert ext.call_count == 1
    output_path = Path("data")
    pandas.DataFrame.to_csv.assert_called_once_with(
        output_path / outfile, index=False, date_format=date_format
    )
