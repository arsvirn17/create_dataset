import cv2
import numpy as np
import os
from random import shuffle

path = 'data'

IMG_SIZE = 28

def create_train_data():
    training_data = []
    label = 0
    for (dirpath, dirnames, filenames) in os.walk(path, topdown=True):
        print(dirpath)
        print(dirnames)
        # print(filenames)
        for dirname in dirnames:
            for(direcpath, direcnames, files) in os.walk(path+"/"+dirname, topdown=True):
                for file in files:
                    actual_path = path + "/" + dirname + "/" + file
                    # print(actual_path)
                    img = cv2.imread(actual_path, cv2.IMREAD_GRAYSCALE)
                    # print(img)
                    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                    training_data.append([np.array(img), label])
            label = label + 1
            print(training_data)

    shuffle(training_data)
    np.save('training_data.npy', training_data)
    return training_data        

train_data = create_train_data()
print(train_data)