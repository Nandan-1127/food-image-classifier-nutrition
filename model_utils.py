import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


CLASSES = [
    "Idli",
    "biryani",
    "burger",
    "cheesecake",
    "chole_bature",
    "crispy chicken",
    "donut",
    "fries",
    "gulab_jamun",
    "ice_cream",
    "kadai_paneer",
    "masala_dosa",
    "momos",
    "pani_puri",
    "pav_bhaji",
    "pizza",
    "samosa",
    "sushi",
    "taco",
    "vada_pav_"
]

MODEL_PATH = 'models/food_classifier.h5'
model = tf.keras.models.load_model(MODEL_PATH, compile=False)

def get_prediction(img_path):
    
    img = image.load_img(img_path, target_size=(160, 160))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)


    predictions = model.predict(img_array)
    
    idx = np.argmax(predictions[0])
    confidence = predictions[0][idx]
    
    return CLASSES[idx], confidence