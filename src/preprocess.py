def clean_data(df):
    """
    Perform basic data cleaning: drop unnecessary columns, handle nulls.
    """
    df = df.drop(columns=[
        'Base MSRP', 'Legislative District', 'DOL Vehicle ID',
        'Vehicle Location', 'VIN (1-10)'
    ])
    return df
