# Text-to-Image with OpenAI's API

## Prerequisites

Install the openai pip package by running `setup.sh` from this folder, or with:

```
pip install -r requirements.txt
```

## Running the script

It's easy! Just invoke `run.sh` with:

```
./run.sh
```

Or run manually with Python, with:

```
python3 tti.py --share
```

Simply remove the `--share` flag to run without creating a shareable Gradio proxy URL.

## Notes

Script currently calls DALL-E 3, but I may add other models in the future. 
