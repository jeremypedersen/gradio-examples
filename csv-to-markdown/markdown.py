import gradio as gr
import pandas as pd
import os
import argparse
from io import StringIO
from tabulate import tabulate

# Function to convert CSV to Markdown
def csv_to_markdown(csv_file):

    # Fake "file" to read when we have issues reading the user's actual input
    ERROR = StringIO("Column 1,Column 2\nYour Table,Was Empty\nOr Had,Formatting Issues\n")

    try:
        # Determine filenames
        csv_name = csv_file.name
        markdown_name = csv_file.name.split('.')[0] + '.md'
        df = pd.read_csv(csv_name)  # Use .name to get the file path if csv_file is a file-like object
    except:
        df = pd.read_csv(ERROR, sep=",")
        markdown_name = 'error.md'

    # Convert the DataFrame to a Markdown table
    markdown_table = tabulate(df, tablefmt="pipe", headers="keys", showindex=False)

    # Save the Markdown table to a .md file
    with open(markdown_name, "w") as file:
        file.write(markdown_table)
    
    return markdown_name

# Set up argparse
parser = argparse.ArgumentParser(description="Run a Gradio app to convert CSV files to markdown tables.")
parser.add_argument('--share', action='store_true', help='Enable Gradio sharing mode')
args = parser.parse_args()
    
# Gradio interface
iface = gr.Interface(
    fn=csv_to_markdown,
    inputs=[gr.File(file_count="single", type="filepath", file_types=["text"], label="Upload CSV File (note: your file won't appear after uploading...this is normal. Just hit submit to generate your markdown file.)")],
    outputs=gr.File(label="Download Markdown File"),
    title="CSV to Markdown Converter",
    description="Upload a CSV file and convert it to a Markdown table. You can then download the resulting Markdown file."
)

# Launch the app with or without sharing based on the --share flag
iface.launch(share=args.share)