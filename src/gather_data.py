from pathlib import Path
import tensorflow as tf
from typing import Any
from configs import app_settings
import json


def gather_data(dir_: Path, train_size: float):
    """Executed by `build_model.py`, will return train and validation (in that order)"""
    data_raw: Any = tf.keras.utils.image_dataset_from_directory(str(dir_))

    classification = dict(
        zip(data_raw.class_names, range(len(data_raw.class_names))))

    tag_file = Path(app_settings.tag_file)
    tag_file.write_text(json.dumps(classification))

    data_scaled = data_raw.map(lambda x, y: (x / 255, y))

    train_sz = int(len(data_scaled) * train_size)
    val_sz = len(data_scaled) - train_sz

    train = data_scaled.take(train_sz)
    validation = data_scaled.skip(train_sz).take(val_sz)

    return train, validation