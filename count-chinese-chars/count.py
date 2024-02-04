import argparse
import gradio as gr
import re

def count_chars(text):
    # Define a regular expression pattern for Chinese characters
    chinese_char_pattern = r'[\u4e00-\u9fff]'

    # Use re.findall to find all Chinese characters in the text
    chinese_chars = re.findall(chinese_char_pattern, text)

    # Return the count of Chinese characters
    return str(len(chinese_chars))

# Set up argparse
parser = argparse.ArgumentParser(description="Run a Gradio app to count Chinese characters.")
parser.add_argument('--share', action='store_true', help='Enable Gradio sharing mode')
args = parser.parse_args()

# Create the Gradio interface
iface = gr.Interface(
    fn=count_chars,
    inputs="text",
    outputs="text",
    title="Text to Speech Converter",
    description="Enter text and count the number of Chinese characters it contains."
)

# Launch the app with or without sharing based on the --share flag
iface.launch(share=args.share)
