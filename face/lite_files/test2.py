import tensorflow.keras
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time
import cv2

def select_image(index):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tf.contrib.lite.Interpreter(model_path="model_unquant.tflite")


    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open('image' + str(index) + '.jpg')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)

def take_image(index):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('image' + str(index) + '.jpg', frame)


index = 0

while True:
    take_image(index)
    time.sleep(.5)
    select_image(index)
    time.sleep(.5)
    index = index + 1
    print(index)

