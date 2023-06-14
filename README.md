# data mining final project

## Step 1 - installing requirements

> those instruction were written assuming you're on windows using powershell.
> check _venv_ documentation for other enviorments, it is not the same for other
> operating system and shell combo.


1. navigate to directory in command line
2. (Optional) start a virtual enviornment using the command `python -m venv ./.venv`
3. (Optional - if preformed step 2) activate the enviorment using the command `./.venv/Scripts/activate.ps1`
4. install all dependency using the command `pip install -r ./requirements.txt`


## Step 2 - downloading images for sampling

recommended: using the following [browser extension](https://download-all-images.mobilefirst.me/).

recommended: using [duck-duck-go](https://duckduckgo.com/) for searching, 
since it can also filter by license for any real usage (therefor, avoid lawsuits) 
and setting safe-search to off (unavailable in other search engines), 
which is usefull for using this model for cencoring in-appropriate images.

1. search any topic at mind and go to the images tab.
2. scroll a little bit down so it will add more images in the page (2-3 times recommended)
3. use the extension for download all the images in the page as zip file.
4. save the zip in the root folder of the project and name it with the topic in mind (without spaces, important).
5. repeat the process to gather unrelated images for the topic.
6. run the extraction script using the command `python ./build_data_dir.py`


## Step 3 - build the model

1. (optional) change the variables inside `.env` file for better prediction/avoiding name collisions/better preformance matrix (hardware dependent)
2. run the command `python ./src/build_model.py` and wait for it to finish (takes about 5 minutes on my pc)

## Step 4 - try it out
Run the command `python ./src/main.py -i [IMAGE_LOCATION]`, where `IMAGE_LOCATION` stands for a path to a local image
and look at the outputs.

