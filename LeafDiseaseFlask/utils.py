import numpy as np
import tensorflow as tf
import cv2

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def get_rgb_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def load_saved_model():
    model_path = "./saved_model"
    model = tf.keras.models.load_model(model_path)
    return model

def predict(model, image):
    image_batch = np.expand_dims(image, 0)
    prediction = model.predict(image_batch)[0]
    return {
        "class": CLASS_NAMES[np.argmax(prediction)],
        "confidence": round(float(np.max(prediction)*100), 2),
    }
