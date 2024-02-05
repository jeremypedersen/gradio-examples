from openai import OpenAI
import argparse
import gradio as gr

def text_to_text(role, prompt):

    # Call GPT-4
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
    ])

    return response.choices[0].message.content

# Set up argparse
parser = argparse.ArgumentParser(description="Run a Gradio app for text to speech conversion.")
parser.add_argument('--share', action='store_true', help='Enable Gradio sharing mode')
args = parser.parse_args()

# Initialize OpenAI client
client = OpenAI()

# Create the Gradio interface
iface = gr.Interface(
    fn=text_to_text,
    inputs=["text","text"],
    outputs="text",
    title="Text to Text with OpenAI's GPT model (GPT-4)",
    description="Enter a role (ex: 'you are a translator') and a prompt 'translate this text' and get back a response"
)

# Launch the app with or without sharing based on the --share flag
iface.launch(share=args.share)
