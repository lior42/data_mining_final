# Data Mining Final Project

This repository contains the code and instructions for a data mining final project. Below are the steps to set up the project, download images for sampling, build the model, and try it out.

- [Data Mining Final Project](#data-mining-final-project)
  - [Framework in usage](#framework-in-usage)
    - [Primary libraries](#primary-libraries)
    - [Support libraries](#support-libraries)
  - [Algorithm in usage](#algorithm-in-usage)
    - [Primary algorithm - Train the AI](#primary-algorithm---train-the-ai)
    - [Secondary algorithm - User interaction](#secondary-algorithm---user-interaction)
  - [Installation and execution instructions](#installation-and-execution-instructions)
    - [Step 1 - Installing Requirements](#step-1---installing-requirements)
    - [Step 2 - Downloading Images for Sampling](#step-2---downloading-images-for-sampling)
    - [Step 3 - Build the Model](#step-3---build-the-model)
    - [Step 4 - Try It Out](#step-4---try-it-out)

## Framework in usage

### Primary libraries

- python (version 3.10 or higher)
- tensorflow - for creating and executing the algorithm
- OpenCV - for reading the images in the main program
- numpy - for some of the calculations executed within the program

### Support libraries

- pydantic - for adding support for configurations
- yapf - for added comfort while developing

## Algorithm in usage

### Primary algorithm - Train the AI

1. Select all the images within data directory, use the subfolder name as tag.
2. Split the data for validation and training.
3. Save the tags->numeric values into `model_tags.json`.
4. Execute the model training (See below). <!--TODO later-->
5. Save the node's state into a file `my_model.h5`.

### Secondary algorithm - User interaction

1. Load the model and tags into memory.
2. Load the image given by the user input.
3. Transform it into 256x256 size.
4. Predict by the model.
5. If the tag given by the prediction is lower then a given barrier, take the other tag.

## Installation and execution instructions

### Step 1 - Installing Requirements

> Please follow these instructions to install the necessary requirements. Note that the instructions assume you are using Windows with PowerShell. If you are using a different environment, refer to the _venv_ documentation for the appropriate commands.

1. Open the command line and navigate to the project directory.
2. (Optional) Start a virtual environment by running the command `python -m venv ./.venv.`.
3. (Optional - if you performed step 2) Activate the environment using the command `./.venv/Scripts/activate.ps1`.
4. Install all dependencies by running the command `pip install -r ./requirements.txt`.

### Step 2 - Downloading Images for Sampling

In this step, you will download images for sampling using a browser extension and a search engine. Follow these instructions:

1. Install the recommended [browser extension](https://download-all-images.mobilefirst.me/) for downloading images.
2. Use [DuckDuckGo](https://duckduckgo.com/) as the search engine. It allows you to filter images by license, which is important for avoiding legal issues, and turn off safe search, which is useful for censoring inappropriate images within the app.
3. Search for any topic of interest and go to the images tab.
4. Scroll down to load more images (repeat 2-3 times for better sampling).
5. Use the browser extension to download all the images on the page as a zip file.
6. Save the zip file in the root folder of the project and name it based on the topic without spaces (e.g., "flag.zip").
7. Repeat the process to gather unrelated images for the topic.
8. Run the extraction script by executing the command `python ./build_data_dir.py`.

### Step 3 - Build the Model

Follow these steps to build the model:

1. (Optional) Modify the variables inside the .env file to improve predictions, avoid name collisions, or enhance performance metrics (hardware dependent).
2. Run the command `python ./src/build_model.py` and wait for it to finish (typically takes around 5 minutes).

### Step 4 - Try It Out

To test the model, execute the command `python ./src/main.py -i [IMAGE_LOCATION]`, where `IMAGE_LOCATION` represents the path to a local image. Examine the outputs to see the results.

Feel free to reach out if you have any questions or encounter any issues.
