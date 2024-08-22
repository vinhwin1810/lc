import requests
from google_docs_downloader import download

def fetch_google_doc(url):
    """
    Fetches the content of a Google Doc from the provided URL.
    """
    # Download the Google Doc content
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Error fetching the Google Doc")

def parse_and_print_grid(doc_content):
    """
    Parses the document content and prints the grid of characters.
    """
    # Split content by lines
    lines = doc_content.splitlines()

    # Print each line as a grid of characters
    for line in lines:
        print(line)

def display_character_grid_from_google_doc(doc_url):
    """
    Main function to fetch, parse, and print the grid from Google Doc.
    """
    # Fetch the document content
    doc_content = fetch_google_doc(doc_url)

    # Parse and print the grid
    parse_and_print_grid(doc_content)

# Example usage:
doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
display_character_grid_from_google_doc(doc_url)
