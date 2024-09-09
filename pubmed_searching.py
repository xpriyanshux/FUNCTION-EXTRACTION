from Bio import Entrez
import pandas as pd

# Set your email address for Entrez
Entrez.email = "your_email@example.com"  # Replace with your email address

# List of keywords
keywords = [
    "Adipose tissue", "White adipose tissue (WAT)", "Brown adipose tissue (BAT)", "Beige adipose tissue",
    "brite adipose tissue", "lipolysis", "lipogenesis", "glucose metabolism", "UCP1", "thermogenesis",
    "energy metabolism", "fatty acid metabolism", "stress", "anxiety", "pro-inflammation", "anti-inflammation",
    "immune system", "metabolic health", "mental health", "gut barrier integrity", "insulin resistance",
    "mental disorder", "lipid metabolism", "energy storage", "energy expenditure", "gut microbiota dysbiosis",
    "proteobacteria", "actinobacteria", "Bacteroides", "microbial diversity", "Shannon index"
]

# Read the Excel file with metabolite information
excel_file = "F:/NISER internship/Text-minning/metabolite.xlsx"
df = pd.read_excel(excel_file)

# List to store articles with relevant keywords and their abstracts
relevant_articles = []

# Iterate through each metabolite
for metabolite in df['Metabolites']:
    # Search for articles with relevant keywords
    query = f"{metabolite} AND ({' OR '.join(keywords)})"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=10)
    record = Entrez.read(handle)
    handle.close()

    # Get the list of article IDs
    id_list = record["IdList"]

    # Retrieve the abstracts of relevant articles
    for article_id in id_list:
        fetch_handle = Entrez.efetch(db="pubmed", id=article_id, rettype="abstract", retmode="text")
        abstract = fetch_handle.read().strip()
        fetch_handle.close()

        # Check if any of the keywords is present in the abstract
        if any(keyword.lower() in abstract.lower() for keyword in keywords):
            # Append the metabolite and its corresponding abstract to the relevant_articles list
            relevant_articles.append((metabolite, abstract))

# Create a new column named "Function" in the DataFrame
df['Function'] = [abstract for _, abstract in relevant_articles]

# Save the modified DataFrame to a new Excel file
output_file = "F:/NISER internship/Text-minning/metabolite_with_functions.xlsx"
df.to_excel(output_file, index=False)
