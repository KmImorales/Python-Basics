Data Utilities Module
📄 Overview

This folder contains reusable Python utilities designed to streamline data preprocessing tasks. The data_utils module provides tools for dynamically processing datasets, including automatic type detection, memory optimization, and handling of numeric and categorical data.
📂 Structure
Files:

    data_process.py: Contains the process_dataset function, which:
        Reads datasets from various file paths and formats.
        Automatically adjusts column data types for efficiency.
        Handles numeric and categorical columns dynamically.

Folder Features:

    Extensible: Designed to be expanded with additional utilities for future projects.
    Portable: Can be reused across different capstone projects.

🚀 Highlights
Key Functionality:

    Dynamic Type Handling:
        Detects numeric columns and ensures appropriate data types (e.g., int64 or float64).
        Converts categorical data into the optimized category type.
    Customizable:
        Supports configurable delimiters and thresholds for unique value detection.
    Missing Data Handling:
        Optional parameters for handling missing data (e.g., drop or fill).
    Efficient for Large Datasets:
        Can be integrated with chunk processing for scalability.

💻 Usage Example

from data_utils.data_process import process_dataset

# Specify the dataset file path
file_path = 'path/to/your/dataset.csv'

# Process the dataset
processed_data = process_dataset(
    file_path, 
    delimiter=',', 
    categorical_threshold=0.2
)

# Display data types
print(processed_data.dtypes)

Output Example:

name       category
age           int64
score       float64
city       category
dtype: object

🤝 Contributions

This module is a work in progress. Suggestions for new utilities or enhancements are welcome!
🔗 Contact

GitHub: Fx250000