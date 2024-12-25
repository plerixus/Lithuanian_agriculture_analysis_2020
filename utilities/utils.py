
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

def prep_df_for_isolated_analysis(df, column_name):
    """
    Filters out rows where the values for specific columns are not 0, excluding the given column.
    Removes columns that are not selected
    Filters values where specific column is not 0

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The column to exclude from the zero-check.

    Returns:
        pd.DataFrame: A filtered DataFrame.
    """
    columns_to_check = [
        'f_2000_k',
        'f_2008_k',
        'f_2012_k',
        'f_2015_k',
        'f_2019_k',
        'f_2029_k',
        'f_2018_k',
        'f_2031_k',
        ]
    columns_to_check = [col for col in columns_to_check if col != column_name]
    filtered_df = df[(df[columns_to_check] == 0).all(axis=1)]
    filtered_df = filtered_df.drop(columns=columns_to_check)
    filtered_df = filtered_df[filtered_df[column_name] != 0]

    return filtered_df