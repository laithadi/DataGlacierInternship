
import yaml 
import pandas as pd 
import logging

# FILE READING 

def config_file(filepath):

    with open(filepath, 'r') as file: 
        try: 
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            logging.error(exc)

def valid_col(df, config_table):

    df.columns = df.columns.str.lower()
    expected_cols = list(map(lambda x: x.lower(), config_table["columns"]))

    len_df_cols = len(list(df.columns))
    len_config_cols = len(list(config_table["columns"]))

    if len_df_cols == len_config_cols and list(df.columns) == list(expected_cols):
        print("Column length and name test: PASSED")
        print("The column names are: ", list(expected_cols))
        print("The number of columns is ", len_config_cols)
        return 1, len_df_cols, len_config_cols
    else: 
        mismatched_cols = list(set(expected_cols).difference(df.columns))
        print("Column length and name test: FAILED")
        print("Following columns are not in the YAML file: ")
        print(mismatched_cols)
        print("There are is a difference of {} number of columns that are mismatched.".format(len(mismatched_cols)))
        return 0, len_df_cols, len_config_cols
