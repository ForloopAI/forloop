import pandas as pd
from idfops.pandas_operations import read_spreadsheet

#Package functions
def load_df(filename):
    try:
        df=read_spreadsheet(filename)[0]
    except FileNotFoundError as e:
        print("File was not found")
        df=None
    return(df)


def send_data_to_forloop(df):
    """TODO: Implementation"""
    pass


def import_batch_data():
    """
    Loading data from batches coming from the platform
    TODO: Implementation
    """
    pass