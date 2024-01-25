# gradio-examples
Simple Gradio apps for doing AI demos

Each gradio app is packaged in its own folder and should be able to run standalone. I try to keep things clear by naming folders as clearly as possible: folder names should include both what the script does and where possible how it does it. For instance, Gradio code to call the OpenAI text-to-speed API might live in a folder called `text-to-speech-openai`. I try to include setup scripts which will install any dependencies needed by a given app. For Linux and macOS, scripts are named `setup.sh` while for Windows they are named `setup.ps1`. 

Each folder will also contain a `README` file which explains how to run the app, and `run.sh` and `run.ps1` scripts which you can use to get started testing the code quickly.

