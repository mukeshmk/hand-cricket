import os
import cv2

TRAINING_DATA_DIR = "training_data"

CLASS_MAP = {
    "empty": 0,
    "1": 1,
    "2": 2,
    "3": 3
}

def mapper(value):
    return CLASS_MAP[value]

def get_dataset(img_shape):
    # load images from the training data directory
    dataset = []
    lables = []
    for label_dir in os.listdir(TRAINING_DATA_DIR):
        # iterating each item in the training data directory
        path = os.path.join(TRAINING_DATA_DIR, label_dir)
        if not os.path.isdir(path):
            continue
        # iterating threw each file in the sub directory
        for image_file in os.listdir(path):
            # loading each image
            img = cv2.imread(os.path.join(path, image_file))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, img_shape)
            
            # adding them to the dataset
            dataset.append(img)
            lables.append(label_dir)
    
    return dataset, lables


def main():

    img_shape = (225, 225)
    dataset, lables = get_dataset(img_shape)

    print(str(len(dataset)) + " : " + str(len(lables)))

if __name__ == "__main__":
    main()
