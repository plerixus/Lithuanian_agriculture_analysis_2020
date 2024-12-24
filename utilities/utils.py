def hello():
    return "Hello"


def remove_exceptions_from_df(df):
    """
    Filters the given DataFrame by removing the valuse that are too extreme to give relevant data
    
    Args:
        df (pd.DataFrame): The input DataFrame to filter.
        
    Returns:
        pd.DataFrame: A filtered DataFrame.
    """
    conditions = (
        (df['f_2008_k'] == 100) |
        (df['f_2012_k'] == 100) |
        (df['f_2015_k'] == 30) |
        (df['f_2019_k'] == 500) |
        (df['f_2029_k'] == 100) |
        (df['f_2031_k'] == 100) |
        (df['f_116_k'] == 500)
    )
    
    return df[~conditions]