import requests
import argparse
import gradio as gr
from pathlib import Path
from openai import OpenAI

def text_to_speech(text):

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
    )

    response.stream_to_file(speech_file_path)

    return speech_file_path

# Set up argparse
parser = argparse.ArgumentParser(description="Run a Gradio app for text to speech conversion.")
parser.add_argument('--share', action='store_true', help='Enable Gradio sharing mode')
args = parser.parse_args()

# Initialize OpenAI client
client = OpenAI()

# Create the Gradio interface
iface = gr.Interface(
    fn=text_to_speech,
    inputs="text",
    outputs="audio",
    title="Text to Speech Converter",
    description="Enter text and convert it to speech using OpenAI's text-to-speech API."
)

# Launch the app with or without sharing based on the --share flag
iface.launch(share=args.share)
