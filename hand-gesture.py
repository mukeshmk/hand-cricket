import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model

REV_CLASS_MAP = {
    0: "empty",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5"
}

def mapper(value):
    return REV_CLASS_MAP[value]

def main():
    img_shape = (225, 225)
    model = load_model("hand-gesture-model.h5")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # rectangle for input sub-frame
        cv2.rectangle(frame, (75, 75), (300, 300), (0, 0, 255), 2)

        # extract the region of image within the input sub-frame
        capture_region = frame[75:300, 75:300]
        img = cv2.cvtColor(capture_region, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, img_shape)

        # predict the move made
        pred = model.predict(np.array([img]))
        move_code = mapper(np.argmax(pred[0]))

        # display the move made
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Your Move: " + move_code, (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Hand Cricket", frame)

        k = cv2.waitKey(10)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()