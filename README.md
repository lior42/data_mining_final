# Data Mining Final Project

This repository contains the code and instructions for a data mining final project. Below are the steps to set up the project, download images for sampling, build the model, and try it out.

## Table of content

-   [Data Mining Final Project](#data-mining-final-project)
    -   [Table of content](#table-of-content)
    -   [Assignee details](#assignee-details)
    -   [Part 1 - Theory](#part-1---theory)
        -   [Question 1 - What is "Image recognition"](#question-1---what-is-image-recognition)
        -   [Question 2 - What is "Face Recognition"](#question-2---what-is-face-recognition)
        -   [Question 3 - When or why will we prefer to use "Image recognition" over other solutions](#question-3---when-or-why-will-we-prefer-to-use-image-recognition-over-other-solutions)
        -   [Question 4 - What steps are required or recommended for building an image-recognition application](#question-4---what-steps-are-required-or-recommended-for-building-an-image-recognition-application)
        -   [Question 5 - What techniques do you think can be used too scan an image](#question-5---what-techniques-do-you-think-can-be-used-too-scan-an-image)
    -   [Part 2 - Practical Knowledge](#part-2---practical-knowledge)
        -   [Framework in usage](#framework-in-usage)
            -   [Primary libraries](#primary-libraries)
            -   [Support libraries](#support-libraries)
        -   [Algorithm in usage](#algorithm-in-usage)
            -   [Primary algorithm - Train the AI](#primary-algorithm---train-the-ai)
            -   [Secondary algorithm - User interaction](#secondary-algorithm---user-interaction)
        -   [Installation and execution instructions](#installation-and-execution-instructions)
            -   [Step 1 - Installing Requirements](#step-1---installing-requirements)
            -   [Step 2 - Downloading Images for Sampling](#step-2---downloading-images-for-sampling)
            -   [Step 3 - Build the Model](#step-3---build-the-model)
            -   [Step 4 - Try It Out](#step-4---try-it-out)
    -   [Appendix - Resources](#appendix---resources)
    -   [Appendix - Tools used in development](#appendix---tools-used-in-development)

## Assignee details

**Censored**

## Part 1 - Theory

In here, we are answering the questions in the first section of the assignment.

### Question 1 - What is "Image recognition"

"Image recognition" is a generic name for algorithms specifically meant
for analyzing images and extracting useful information out of them, thus allow
us to take additional steps for making a decisive actions regarding their
content or applying a more traditional algorithms on top of them such as sorting.

one example of an idea for a project that uses image recognition:
Creating image recognition algorithm for categorizing your computer's "image" folder
to a given set of categories (such as "family photos", "vacations" and "work" for example)
and make it so that every time you save an image, it automatically put it in an appropriate
directory.

### Question 2 - What is "Face Recognition"

"Face recognition" is a process which involving using [Image recognition](#question-1---what-is-image-recognition)
to identifying faces within an image (if any) and extracting identifying details
about it.
typically it also connected to a categorizing algorithm for identifying a given person for example.

one example of an idea for a project that uses face recognition:
a security system that determine if a given person is allowed to pass or not.

### Question 3 - When or why will we prefer to use "Image recognition" over other solutions

We will opt for using algorithms based on image recognition over other solutions
in cases where:

1. No other solution is possible (Example: extracting data from user-generated content in your website)
2. Other solutions may raise too much additional complexity to an existing system in place (Example: adding a step of automated QA for a line of products in a factory)
3. Other solutions are in place, but may require an assistance to handle the workload (Example: radiologist using image recognition for a basic interpretation of a set of images of a person to help guide him toward a diagnosis).

### Question 4 - What steps are required or recommended for building an image-recognition application

mandatory steps:

1. Building a large set of pre-categorized images in one way or another (in this project: by creating a specific directory structure from a known source of information).
2. Creating a model which starts by cleaning the data (in this project: by applying multiple steps of convolution layers and max pooling layers inside the model's algorithm), then test the resulted data for known patterns (in this project: by applying multiple layers of "dense" algorithms).
3. creating a way for a typical user to test a new information (in this project: by creating a CLI interface).

Not mandatory steps, but typically recommended steps:

1. Building a framework for adding more information to the set by a trusted source (not implemented in this project).
2. Caching the model's output (in this project: "my_model.h5" file, automatically created during the "build_model" step).
3. Create an easy way of adjusting some of the parameters of the model, to adjust it for various cases (in this project: implemented via ".env" file).
4. Deploying the project onto a cloud, that can handle the massive workload much easier then a typical computer (example: using aws's EC-2 which can handle varying "peaked" workload, along with aws's EC-3 that can handle the massive storage requirements) and may offer additional support for this type of project (example: aws's SageMaker) (not implemented in this project).

### Question 5 - What techniques do you think can be used too scan an image

One technique that can be used to scan an image is by transform it into
a matrix/tensor, not only that is similar to the way that the computer's monitor
request it (therefor, it is relatively simple and probably very optimized already,
which is useful considering how much memory an image may need), it makes it
quite intuitive for applying various mathematical and statistical computations on
it which helps us to extract information out of it.

## Part 2 - Practical Knowledge

In this section, we will describe the necessary steps required to install and run the
program requested in the second section of the assignment.

### Framework in usage

#### Primary libraries

-   python (version 3.10 or higher)
-   tensorflow - for creating and executing the algorithm
-   OpenCV - for reading the images in the main program
-   numpy - for some of the calculations executed within the program

#### Support libraries

-   pydantic - for adding support for configurations
-   yapf - for added comfort while developing

### Algorithm in usage

#### Primary algorithm - Train the AI

1. Select all the images within data directory, use the subfolder name as tag.
2. Split the data for validation and training.
3. Save the tags->numeric values into `model_tags.json`.
4. Execute the model training (See below).
5. Save the node's state into a file `my_model.h5`.

#### Secondary algorithm - User interaction

1. Load the model and tags into memory.
2. Load the image given by the user input.
3. Transform it into 256x256 size.
4. Predict by the model.
5. Yield the tag predicted, also yields much confident does the model had by assigning the given tag.

### Installation and execution instructions

#### Step 1 - Installing Requirements

> Please follow these instructions to install the necessary requirements.
> Note that the instructions assume you are using Windows with PowerShell.
> If you are using a different environment, refer to the _venv_ documentation for the appropriate commands.

1. Open the command line and navigate to the project directory.
2. (Optional) Start a virtual environment by running the command `python -m venv ./.venv.`.
3. (Optional - if you performed step 2) Activate the environment using the command `./.venv/Scripts/activate.ps1`.
4. Install all dependencies by running the command `pip install -r ./requirements.txt`.

#### Step 2 - Downloading Images for Sampling

In this step, you will download images for sampling using a browser extension and a search engine. Follow these instructions:

1. Install the recommended [browser extension](https://download-all-images.mobilefirst.me/) for downloading images.
2. Use [DuckDuckGo](https://duckduckgo.com/) as the search engine. It allows you to filter images by license, which is important for avoiding legal issues, and turn off safe search, which is useful for censoring inappropriate images within the app.
3. Search for any topic of interest and go to the images tab.
4. Scroll down to load more images (repeat 2-3 times for better sampling).
5. Use the browser extension to download all the images on the page as a zip file.
6. Save the zip file in the root folder of the project and name it based on the topic without spaces (e.g., "flag.zip").
7. Repeat the process to gather unrelated images for the topic.
8. Run the extraction script by executing the command `python ./build_data_dir.py`.

> During Testing - the search terms "flags" and "random images" where used

#### Step 3 - Build the Model

Follow these steps to build the model:

1. (Optional) Modify the variables inside the .env file to improve predictions, avoid name collisions, or enhance performance metrics (hardware dependent).
2. Run the command `python ./src/build_model.py` and wait for it to finish (typically takes around 5 minutes).

#### Step 4 - Try It Out

To test the model, execute the command `python ./src/main.py -i [IMAGE_LOCATION]`, where `IMAGE_LOCATION` represents the path to a local image. Examine the outputs to see the results.

Feel free to reach out if you have any questions or encounter any issues.

## Appendix - Resources

-   [Wikipedia](https://en.wikipedia.org/wiki/Computer_vision)
-   [Building Neural Network Tutorial](https://www.youtube.com/watch?v=jztwpsIzEGc)

## Appendix - Tools used in development

-   [python](https://www.python.org/)
-   [Tensorflow](https://www.tensorflow.org/)
-   [OpenCV](https://opencv.org/)
-   [NumPy](https://numpy.org/)
-   [pydantic](https://docs.pydantic.dev/latest/)
-   [yapf](https://github.com/google/yapf)
-   [venv](https://docs.python.org/3/library/venv.html)
-   [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
-   [Visual Studio Code](https://code.visualstudio.com/)
-   [Python's vs-code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [Github](https://github.com/)
