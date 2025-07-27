import pandas as pd

def load_data(filepath):
    """
    Load dataset from CSV file.
    """
    return pd.read_csv(filepath)
