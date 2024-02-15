from openai import OpenAI
import argparse
import gradio as gr
import urllib.request
from PIL import Image

def text_to_image(prompt):

    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url

    # Retrieve the image, and return PIL data to gradio
    urllib.request.urlretrieve(image_url, "image.png") 

    img = Image.open("image.png") 

    return img

# Set up argparse
parser = argparse.ArgumentParser(description="Run a Gradio app for text to speech conversion.")
parser.add_argument('--share', action='store_true', help='Enable Gradio sharing mode')
args = parser.parse_args()

# Initialize OpenAI client
client = OpenAI()

# Create the Gradio interface
iface = gr.Interface(
    fn=text_to_image,
    inputs="text",
    outputs="image",
    title="Text to Image with OpenAI's DALL-E 3 model",
    description="Enter a description of an image"
)

# Launch the app with or without sharing based on the --share flag
iface.launch(share=args.share)
