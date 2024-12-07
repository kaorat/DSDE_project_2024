import pandas as pd
import networkx as nx
import os

# Load the CSV file
# Add 'names' if the file has no header: names=["Title", "Author"]
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'author_for_network_analysis.csv')
df = pd.read_csv(file_path)

# Create an empty graph for co-authorship
co_authors = nx.Graph()

count = 0
# Group authors by title and add edges
for title, group in df.groupby("Title"):
    if(count >= 225):
        break
    authors = group["Author"].unique()
    for i, author1 in enumerate(authors):
        for author2 in authors[i+1:]:
            if co_authors.has_edge(author1, author2):
                co_authors[author1][author2]["weight"] += 1  # Increment weight if edge exists
            else:
                co_authors.add_edge(author1, author2, weight=1)  # Add new edge
    count+=1

# Save the co-authorship edge list
nx.write_edgelist(co_authors, "co_authorship_1.csv", delimiter=",", data=False)  # Save without weights