import os
import json
import numpy as np
import math
from skimage.measure import block_reduce


def read_train_data():
    # Load the data dictionary with all the arrays
    with open(os.path.join(data_dir, data_filename)) as f:
        data_dict = json.load(f)

    # Load the text labels dictionary
    with open(os.path.join(data_dir, labels_filename)) as f:
        labels_dict = json.load(f)

    # Find the maximum size for any array and any text label
    # so that we can create fixed sized numpy arrays
    max_data_size = 0
    max_text_size = 0
    num_rows = 0
    for filename, val in data_dict.items():
        num_rows += 1

        data_size = len(data_dict[filename])
        if data_size > max_data_size:
            max_data_size = data_size

        text_size = len(labels_dict[filename])
        if text_size > max_text_size:
            max_text_size = text_size

    # We will reduce the size of our arrays
    # by using the block_reduce function
    # and averaging array values in intervals of FILTER_SIZE
    new_size = math.ceil(max_data_size / FILTER_SIZE)
    # Now we have our fixed size array for our down-sampled data
    data = np.zeros((num_rows, new_size))

    texts = []
    i = 0
    for filename, arr in data_dict.items():
        new_arr = block_reduce(np.array(arr), block_size=(FILTER_SIZE,), func=np.mean)
        new_arr_size = len(new_arr)
        # The array is probably smaller than the maximum allowed length
        # So let's set the boundary for that
        data[i, :new_arr_size] = new_arr

        text = labels_dict[filename]
        # We are padding text labels with empty strings if they are short
        texts.append(text.ljust(max_text_size))
        i += 1

    text_data = np.array(texts)
    return data, text_data


if __name__ == "__main__":

    SAMPLING_RATE = 5500
    FILTER_SIZE = SAMPLING_RATE // 100

    data_dir = "../data"
    data_filename = "data_sample_train.json"
    labels_filename = "labels_sample_train.json"

    data, text_data = read_train_data()

    print("Data array shape: ", data.shape, "\nFirst 5 rows:")
    print(data[:5], end='\n\n')

    print("Text labels shape: ", text_data.shape, "\nFirst 5 rows:")
    print(text_data[:5], end='\n\n')
