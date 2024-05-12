# ImageToRessources

The ImageToRessources project is a tool that performs AI operations on images.
Before you start I recommand to create a new virtual environment for this project.

e.g.:
conda create -n newEnvName python=3.10

That way you are making sure not to get any dependency issues.

Clone the repository to your local machine.
Navigate to the project directory: ImageToRessources/

# Image to Text
The first step is to figure out what the objekt in an image is, we are using the open source model by salesForce to figure that out.
1. Go to the salesForce_imageToText.py.
2. Unhash the code following "# Setting up:".
3. Execute the file:
    python salesForce_imageToText.py
4. The program will most likely terminate due to some missing dependencies. Install the missing dependecies to the newEnvName you created in the begining.
5. Execute the file again and add missing dependecies until the model runs and you recieve the image description.
6. Hash out the code following "# Setting up:".

# Text to Resource List
To form a list of resources out of an image description we are passing the description to Metas open source LLM Llama3.
Therefore this project relies on the llama3 being installed locally on your machine. The easiest way to do that is by using:

Ollama -> https://ollama.com

Once installed you can list up your llama3 models with the following command through your terminal:
    ollama list
To recieve a list of the resources we need to create a model of llama3. The model is definde in the Modelfile.
Run the following command to create the model I prepared:
    ollama create promptEng -f Modelfile
Now run the ollama model with:
    ollama run promptEng
You can enter anything here and the model will try to list up the required resources to create it. 
Use the following command to stop using the model thorugh the command line:
    /bye

The ollama model will continue running in the background and we can access it throgh a local API, lets test that.
1. Open the textToPrompt.py
2. Unhash all the code following "# Usage example:"
3. Exetue the script:
    python textToPrompt.py
4. The model will generate a list of resources based on the image description following ""prompt":" in the data block.
5. Hash all the code following "# Usage example:" so the file is ready for external usage.


