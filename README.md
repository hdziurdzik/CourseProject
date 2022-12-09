# CS410 Final Project
### An analysis of common restaurants mentioned in the UIUC subreddit given a specific query

Authors: Erin Dowdy (eedowdy2) and Hania Dziurdzik (haniakd2)

### Overview
The program works by ranking the documents by relevance to a query using the BM25 Okapi algorithm. It then extracts restaurant names from each document by finding the noun phrases in the document that contain a proper noun, and then classifying those phrases using a HuggingFace Zero-Shot Classification model. Finally, it takes the most common restaurants from the top N most relevant documents and displays them on a map.

### Implementation and Usage
The program is implemented in a Python Notebook. To use the program, open the `.ipynb` file in Google Colab and run the cells. The data is located in a separate `.json` file, which needs to be uploaded to Google Drive so the notebook can access it. 

### Dependencies
This program uses the Python packages `pandas`, `numpy`, `contractions`, `transformers`, `rank_bm25`, `nltk`, and `textblob`. If not already installed, these packages can be installed by running
 ```
 !pip install [package]
 ```
 in a cell in the notebook.

### Contribution
Erin did the web scraping and visualization parts of the project, while Hania did the algorithm for the ranking and extracting restaurant names out of documents.
