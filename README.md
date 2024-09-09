# Metabolite Functional Annotation and PubChem Analysis

This repository contains a collection of Python scripts designed for the functional annotation of metabolites. The workflow involves retrieving PubChem IDs, filtering based on DrugBank presence, and extracting functional data from PubMed and PubChem for further analysis.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Workflow](#workflow)
- [Scripts Overview](#scripts-overview)
  - [1. Retrieve PubChem IDs for Metabolites](#1-retrieve-pubchem-ids-for-metabolites)
  - [2. Check for DrugBank Presence](#2-check-for-drugbank-presence)
  - [3. Search PubMed for Metabolite Function](#3-search-pubmed-for-metabolite-function)
  - [4. Extract Text Data from PubChem](#4-extract-text-data-from-pubchem)
- [Usage](#usage)
- [License](#license)

## Overview
This project automates the annotation of metabolites using public databases like PubChem and PubMed. The process includes:
1. Searching PubChem to retrieve compound IDs for a list of metabolites.
2. Filtering out drug-like compounds by checking for DrugBank links.
3. Searching for functional data in PubMed based on predefined keywords.
4. Extracting text data from PubChem XML files for further annotation.

The final result is an annotated Excel file with PubChem IDs, relevant functions, and metadata for each metabolite.

## Requirements
To use the scripts in this repository, the following Python libraries are required:
- `requests`
- `pandas`
- `xml.etree.ElementTree`
- `Bio` (from Biopython)
- `openpyxl`

You can install the required dependencies using pip:
```bash
pip install requests pandas biopython openpyxl
```

Additionally, you need an email address for PubMed API access (via Entrez) and an optional API key for PubChem to ensure smooth operation.

## Workflow

The main steps involved in this project are as follows:

1. **Retrieve PubChem IDs**: Extract PubChem compound IDs for a given list of metabolites.
2. **Check for DrugBank Presence**: Filter out compounds that appear in DrugBank to ensure the focus remains on metabolites.
3. **PubMed Search**: Query PubMed using a set of predefined keywords to retrieve relevant functional information for each metabolite.
4. **Extract Data from PubChem**: Extract text fields from PubChem XML data for further functional annotation.

## Scripts Overview

### 1. Retrieve PubChem IDs for Metabolites
This script searches PubChem for compound IDs corresponding to each metabolite name provided in an Excel file. The results are saved in a new Excel file.

### 2. Check for DrugBank Presence
This script checks whether the retrieved PubChem compounds are linked to DrugBank. If a compound is found to be a drug, it is excluded from further analysis.

### 3. Search PubMed for Metabolite Function
The PubMed search script uses the Entrez API to search for functional data related to the metabolites using a predefined set of keywords. It retrieves and saves the relevant abstracts from PubMed.

### 4. Extract Text Data from PubChem
This script processes the PubChem XML files and extracts specific text fields, which are then annotated with the metabolite information. The extracted text is saved in an Excel file for further analysis.

## Usage

1. **Retrieve PubChem IDs**: Run the script to retrieve PubChem IDs for a list of metabolites.
2. **Check for DrugBank Presence**: Run the second script to filter out metabolites linked to DrugBank.
3. **Search for Functional Information on PubMed**: Use the third script to search PubMed and gather functional information based on keywords.
4. **Extract Data from PubChem**: Run the final script to extract text data from PubChem XML files.

### Example Usage
- Place your input Excel files with metabolite names in the appropriate directory.
- Run each script sequentially as outlined above to process the data.
- The final output will be an annotated Excel file with PubChem IDs, functional annotations, and extracted text data.
