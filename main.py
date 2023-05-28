from data_validation import DataValidation
import argparse
import pandas as pd

def main(df,column_name):
    data_validation = DataValidation(df)
    missing_values = data_validation.get_missing_values(column_name)
    unique_value = data_validation.get_unique_values(column_name)
    print(f"the missing values in this dataframe in {column_name} is {missing_values}")
    print(f"the unique values in this dataframe in {column_name} is {unique_value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True)
    parser.add_argument('--column', type=str, required=True)
    args = parser.parse_args()
    df = pd.read_csv(args.data)
    main(df,args.column)