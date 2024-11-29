import pandas as pd

# Load the CSV file
file_path = 'NetflixOriginals.csv'  # Replace with your file path
db = pd.read_csv(file_path)  

# Dynamically create variables for each column
for col in db.columns:
    var_name = col.lower().replace(" ", "_")  # Convert column name to lowercase and replace spaces with underscores
    globals()[var_name] = db[col].tolist()  # Create a variable with the column's values


