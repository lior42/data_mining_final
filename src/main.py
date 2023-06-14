from configs import app_settings
import sys
from tensorflow import keras as ks
import tensorflow as tf
import cv2
import numpy as np
import argparse
from pathlib import Path
import json


def main(args: list[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True)
    p_args = vars(parser.parse_args(args[1:]))
    img_path = Path(p_args["image"])

    if not img_path.exists():
        print("error")
        return

    my_model = ks.models.load_model(app_settings.save_file)
    img = cv2.imread(str(img_path.resolve()))
    img = tf.image.resize(img, (256, 256))

    prediction = my_model.predict(np.expand_dims(img / 255, 0))

    my_tags: dict[str,
                  int] = json.loads(Path(app_settings.tag_file).read_text())

    tag_names = list(my_tags.keys())
    # tag_names.reverse()
    # percentage = (abs(number1 - number2) / ((number1 + number2) / 2)) * 100

    similarities = [
        1 - abs(prediction[0] - float(ident)) for ident in my_tags.values()
    ]

    ind_max = np.argmax(similarities)
    conf = 1 - closeness(float(similarities[ind_max]), 1.0)

    print(
        f"Predicted tag:\"{tag_names[ind_max]}\", with confident level of {conf:.3f}."
    )

    if conf > app_settings.coherent_prediction:
        print(f"This is considered a strong prediction.")

    # print(f"Confident level is set to {app_settings.coherent_prediction:.3f}.")
    # print(f"Therefore, Final prediction is \"{tag}\".")


def closeness(num1, num2):
    avg = (num1 + num2) / 2
    dist = abs(num1 - num2)

    if avg == 0: return 1

    return dist / avg


if __name__ == '__main__':
    main(sys.argv)