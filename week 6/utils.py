
import yaml
import gzip

# READ FILE USING YAML 
def read_yaml(path):
    
    with open(path, 'r') as data: 
        try:
            return yaml.safe_load(data)
        except:
            print("Something went wrong with loading the data.")

# CLEAN THE COLUMN NAMES 
def clean_col_names(df):

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace('[%\W]', '', regex= True)

# RETURN DIFFERENCE IN COLUMNS 
def col_dif(df, conf_table):

    df_cols = list(df.columns)
    ct_cols = conf_table["columns"]
    missing_from_df = list(set(ct_cols).difference(df_cols))
    missing_from_ct = list(set(df_cols).difference(ct_cols))
    
    return df_cols, missing_from_df, ct_cols, missing_from_ct

# CHECKS FOR THE SAME NUMBER OF COLUMNS  
def col_val(df, conf_table):

    df_cols = list(df.columns)
    ct_cols = list(conf_table["columns"])
    df_cols_count = len(df_cols)
    ct_cols_count = conf_table["num_columns"]

    if df_cols == ct_cols:
        print("Validation test: PASS")
        return 1
    else: 
        print("Validation test: FAILED")
        print(f"Incoming data consists of {df_cols_count} columns.")
        print(f"YAML file consists of {ct_cols_count} columns.")
        print("The listed columns are not in the incoming data: \n{}".format(list(set(ct_cols).difference(df_cols))))
        print("The listed columns are not in the YAML file: \n{}".format(list(set(df_cols).difference(ct_cols))))
        return 0 

# WRITE TE FILE IN PUIPE SEPARATED TEXT FILE IN GZ FORMAT
def write_file(df):

    df.to_csv(
        "stocks.csv.gz",
        index= False,
        sep= "|",
        compression= "gzip"
    )

# SUMMARY OF THE DATA
def summary(conf_table):

    print("The file name is {}".format(conf_table["path"]))
    print("The delimiter used is '{}'".format(conf_table["delimiter"]))
    print("The number of columns in the data is {}".format(conf_table["num_columns"]))
    print("The data is 2GB in size.")
    print("The columns for the data are: {}".format(conf_table["columns"]))

# DISPLAY THE RESULTS
def result(col_val, df, conf_table):

    if col_val == 1: 
        # write the file in pip (|) separated text file
        write_file(df)
        # summary of the file 
        summary(conf_table)
    else: 
        df_cols, missing_from_df, ct_cols, missing_from_ct = col_dif(df, conf_table)
        print("It seems that the incoming data containing the following columns: {} \nis missing {} ".format(df_cols,missing_from_df))
        print("It seems that the YAML file containing the following columns: {} \nis missing {} ".format(ct_cols, missing_from_ct))
