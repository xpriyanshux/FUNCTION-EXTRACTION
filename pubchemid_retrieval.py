import pandas as pd
import requests

# Read the Excel file with metabolite names
df = pd.read_excel("F:/XXX/Text-minning/Metabolite_pubchem_ID.xlsx")  # Replace with your file path

# Function to search for PubChem ID
def search_pubchem_id(metabolite_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{metabolite_name}/cids/JSON"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'IdentifierList' in data:
            pubchem_id = data['IdentifierList']['CID'][0]
            return pubchem_id
    return None

# Chunk size for processing metabolite names
chunk_size = 100
total_names = len(df)

# Process metabolite names in chunks
for i in range(0, total_names, chunk_size):
    # Extract the chunk of metabolite names
    chunk = df.iloc[i:i+chunk_size]

    # Add a new column 'PubChem ID' and search for PubChem ID for each metabolite name
    chunk['PubChem ID'] = chunk['Metabolite'].apply(search_pubchem_id)

    # Save the updated chunk to an Excel file
    output_file = f"Metabolite_pubchem_ID_withIDs_{i+1}-{i+len(chunk)}.xlsx"
    chunk.to_excel(output_file, index=False)
    print(f"PubChem IDs extracted and saved to {output_file}")

print("All metabolite names processed.")
