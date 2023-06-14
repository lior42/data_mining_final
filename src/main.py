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
    tag_names.reverse()

    similarities = [np.dot(prediction[0], ident) for ident in my_tags.values()]

    sim_ids = np.argmax(similarities)

    conf = float(similarities[sim_ids])
    tag = ""

    if conf < app_settings.coherent_prediction:
        tag = tag_names[1 - sim_ids]
    else:
        tag = tag_names[sim_ids]

    print(
        f"Predicted tag:\"{tag_names[sim_ids]}\", with confident level of {conf:.3f}."
    )
    print(f"Confident level is set to {app_settings.coherent_prediction:.3f}.")
    print(f"Therefore, Final prediction is \"{tag}\".")


if __name__ == '__main__':
    main(sys.argv)