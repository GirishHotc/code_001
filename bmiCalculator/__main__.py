import argparse

from bmiCalculator.bmi_calculator import summary_entrypoint

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # hyper parameters sent by the client are passed as command-line arguments
    # to the script.

    parser.add_argument(
        "--table_name",
        metavar="table_name",
        type=list,
        default='',
        required=False,
        help="table name for Data quality")

    parser.add_argument(
        "--dataframe",
        metavar="dataframe",
        type=str,
        default='',
        required=False,
        help="pandas data frame for data quality")

    parser.add_argument(
        "--s3_bucket",
        metavar="s3_bucket",
        type=str,
        default='s3://sg-netsuite-etl-s3',
        required=False,
        help="s3 bucket name where the summary reports get saved")

    parser.add_argument(
        "--default_file_path",
        metavar="default_file_path",
        type=str,
        default='config/default.yaml',
        required=False,
        help="Yaml file with the default values exception handling")

    args, _ = parser.parse_known_args()

    summary_entrypoint.main_data_function(
        dataframe=args.dataframe,
        table_name=args.table_name,
        s3_bucket=args.s3_bucket,
        default_file_path=args.default_file_path)
