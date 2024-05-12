# ImageToResources

The ImageToResources project is an AI-powered tool that processes images to identify objects and determine the basic resources required to create them. This document provides instructions on setting up and using the tool.

## Prerequisites

Before you start, it is recommended to create a new virtual environment for this project to avoid dependency issues.

```bash
conda create -n newEnvName python=3.10
conda activate newEnvName
```

Clone the repository to your local machine and navigate to the project directory:

```bash
git clone [Repository URL]
cd ImageToResources/
```

## Installation

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Image to Text

This module uses the Salesforce open-source model to identify objects in images.

1. Navigate to `salesForce_imageToText.py`.
2. Uncomment the code under "# Setting up:".
3. Execute the file:

    ```bash
    python salesForce_imageToText.py
    ```

4. If the program terminates due to missing dependencies, install them into your virtual environment (`newEnvName`).
5. Re-run the file and continue to add missing dependencies until the model runs successfully and you receive the image description.
6. Comment out the code under "# Setting up:" once setup is complete.

## Text to Resource List

This component uses the open-source Llama3 model from Meta to generate a list of resources based on image descriptions.

### Setting Up Llama3

Ensure Llama3 is installed on your machine using Ollama. Visit [Ollama](https://ollama.com) for installation instructions.

Once installed list your Llama3 models using:

```bash
ollama list
```

Create and run a custom Llama3 model with the provided `Modelfile`:

```bash
ollama create promptEng -f Modelfile
ollama run promptEng
```

You can test the model by entering descriptions directly. Use `/bye` to stop interactive mode.

The model will continue running in the background, accessible via a local API.

### Testing Local API

1. Navigate to `textToPrompt.py`.
2. Uncomment the code under "# Usage example:".
3. Execute the script:

    ```bash
    python textToPrompt.py
    ```

4. The script sends a description to the local API, which returns a list of required resources.
5. Re-comment the code under "# Usage example:" once testing is complete, preparing the file for external use.

## Main Execution

Run the `main.py` to start the full process:

```bash
python main.py
```

This script integrates the image capture, description generation, and resource listing into a single workflow.

