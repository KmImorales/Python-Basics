import pandas as pd

def process_dataset(file_path, delimiter=';', categorical_threshold=0.1, handle_missing='none'):
    """
    This function:
    - Reads a dataset from a given file path using the specified delimiter.
    - Identifies numeric columns and ensures their types remain appropriate 
      (e.g., float or integer).
    - Automatically detects and converts categorical columns to the 'category' data type 
      based on a configurable threshold for unique value ratio.

    Parameters:
    - file_path (str): The path to the CSV file to be processed.
    - delimiter (str): The delimiter used in the CSV file (default is ';').
    - categorical_threshold (float): A ratio (0 to 1) indicating the maximum number 
      of unique values relative to the dataset size to classify a column as categorical.
      Example: If set to 0.1, columns with fewer than 10% unique values will be converted to 'category'.

    Returns:
    - pd.DataFrame: A DataFrame with adjusted data types where:
        - Numeric columns retain their type (int64 or float64).
        - Categorical columns are converted to the 'category' data type.

    Example Usage:
    file_path = 'path_to_file.csv'
    processed_data = process_dataset(file_path, delimiter=',', categorical_threshold=0.15)

    Notes:
    - Numeric columns with only integer values are explicitly cast to 'int64'.
    - Non-numeric columns or those with low cardinality are treated as categorical.
    """
    
    # Load the dataset
    data = pd.read_csv(file_path, sep=delimiter)

    # Handle missing values
    if handle_missing == 'drop':
        data = data.dropna()
    elif handle_missing == 'fill':
        data = data.fillna(method='ffill')

    # Identify numeric and categorical columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    categorical_columns = [
        col for col in data.columns if col not in numeric_columns and (
            pd.api.types.is_object_dtype(data[col]) or
            data[col].nunique() / len(data) <= categorical_threshold
        )
    ]

    # Convert categorical columns to 'category'
    data[categorical_columns] = data[categorical_columns].astype('category')

    # Ensure numeric columns retain appropriate types
    for col in numeric_columns:
        if pd.api.types.is_float_dtype(data[col]) and (data[col] % 1 == 0).all():
            data[col] = data[col].astype('int64')
    
    return data

