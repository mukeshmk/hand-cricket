import os
import cv2
import argparse

TRAINING_DATA_DIR = "training_data"

def capture_images(label, label_path, sample_size):
    # open camera (device : 0) in video capture mode
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video")

    start = False
    count = 0

    while True:
        # read the image from the camera
        # returns ret, frame - 
        # where ret is a boolean True - a image was retrived; False - no image retrived
        # frame contains the image retrived
        ret, frame = cap.read()
        # checking if the image was retrived
        if not ret:
            print("Error getting image")
            continue

        # if required number of images have been captured
        if count == sample_size:
            pass#break

        # drawing a rectangle to indicate which section of the image is being saved 
        # params: img, point1, point 2, colour, thinkness of line
        cv2.rectangle(frame, (75, 75), (300, 300), (255, 255, 255), 2)
        
        # Displaying the Images which are to be catured
        cv2.imshow("Collecting images", frame)
        
        k = cv2.waitKey(10)
        if k == ord('q'):
            break

        count+=1

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', help='label of the image being captured', type=str)
    parser.add_argument('--samples', help='number of samples to be captured for that label', type=int)
    args = parser.parse_args()

    # args verification
    if args.label is None:
        print("Please the label of the image to capture")
        exit(1)

    if args.samples is None:
        print("Please specify the sample size (count) of the image to be captured")
        exit(1)

    # training_data folder creation
    if not os.path.exists(TRAINING_DATA_DIR):
        print("Creating output directory " + TRAINING_DATA_DIR)
        os.makedirs(TRAINING_DATA_DIR)

    label_path = TRAINING_DATA_DIR + "\\" + args.label
    # label folder creattion
    if not os.path.exists(label_path):
        print("Creating output directory " + label_path)
        os.makedirs(label_path)
    else:
        print("Label directory exists: generated images will be appended to the existing data")

    capture_images(args.label, label_path, args.samples)


if __name__ == "__main__":
    main()
