import pandas as pd
import json

def json_to_excel(json_file, excel_file):
    # Load the JSON data from the file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Convert JSON data to a pandas DataFrame
    df = pd.json_normalize(data)

    # Write DataFrame to Excel
    df.to_excel(excel_file, index=False)

    print(f"Conversion successful! Excel file saved as: {excel_file}")

# Example usage
json_file = 'trivy-scan-results.json'  # Path to your input JSON file
excel_file = 'trivy-scan-results.xlsx'  # Path to save the output Excel file

json_to_excel(json_file, excel_file)
