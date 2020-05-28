# Hand Cricket Simulator

An attempt to recreate the childhood experience of playing Hand Cricket against a computer using OpenCV Image Recognition.

# To run the program on your machine:
1. clone the repo: `git clone https://github.com/mukeshmk/hand-cricket.git`
2. create a virtual environment inside the folder: `python -m venv .venv`
3. activate the virtual environment: `.venv\Scripts\activate` (in case of Windows)
4. install the required packages for the game to run using: `pip install -r requirements.txt`
5. run the code: `python file_name.py`
6. make sure to `deactivate` once your done.

### To Generate data for training the model:

- run `python generate-training-data.py --label label_value --sample num_of_samples`  
- This program will open a start video capture using the default camera (`device: 0`) of your machine.
- In the video you will see a red colour rectangle:
- Hold you hand in the rectangle and make gesture as per `lable_value` make sure to throw in some variety.
- This will capture `num_of_samples` number of images and store it under `training_data\label_value` directory
- Do this for the following labels: `0`, `1`, `2`, `3`, `4`, `5` and `empty`.
- Check sample images provided under `sample_images` directory. or the actual training data under `training_data`.
