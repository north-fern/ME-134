'''

Morgan Strong
code from Teachable Machines page
edited based on feedback on using tensorflow.lite instead
https://heartbeat.fritz.ai/running-tensorflow-lite-image-classification-models-in-python-92ef44b4cd47

some errors encountered, does not fully work. error thrown when executing tensorflow, now has issues with an unknown symbol
ImportError: /home/pi/Desktop/tf_pi/env/lib/python3.7/site-packages/tensorflow_core/lite/python/interpreter_wrapper/_tensorflow_wrap_interpreter_wrapper.so: undefined symbol: _ZN6tflite12tensor_utils24NeonVectorScalarMultiplyEPKaifPf

unknown how to fix; based on github comments it should be OK...
https://github.com/tensorflow/tensorflow/issues/19319
https://github.com/tensorflow/tensorflow/issues/21855

the models (both regular and lite) are attached, which is trained for eyebrows up, down, right wink, left wink, and neutral
currently it takes a picture and starts loading the model, but hits the unknown symbol and fails. 
'''



#import tensorflow.keras
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time
import cv2

def select_image(index):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    #error here first, removed the "tf.contrib" and changed to tf.lite as contrib had no lite, but tf did
    #https://github.com/tensorflow/tensorflow/issues/15401
    model = tf.lite.Interpreter(model_path="model_unquant.tflite")


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

    ## from here, we would actuate the motors 

