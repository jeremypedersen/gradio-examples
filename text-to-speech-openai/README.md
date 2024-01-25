# Text-to-Speech with OpenAI's API

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
python3 tts.py --share
```

Simply remove the `--share` flag to run without creating a shareable Gradio proxy URL.