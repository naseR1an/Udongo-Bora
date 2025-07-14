import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# ✅ Load Pre-trained Model (Replace with your custom model path)
MODEL_PATH = os.path.join("disease_model", "model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

# 🏷️ Class labels (Update with your disease classes)
CLASS_NAMES = [
    "Healthy",
    "Leaf Blight",
    "Powdery Mildew",
    "Rust",
    "Bacterial Spot",
    "Early Blight"
]

def preprocess_image(img_file):
    """
    Preprocess the uploaded image for prediction.
    """
    img = image.load_img(img_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_disease(img_file):
    """
    Predict the crop disease from the uploaded image.
    """
    try:
        processed_img = preprocess_image(img_file)
        prediction = model.predict(processed_img)
        predicted_class = CLASS_NAMES[np.argmax(prediction)]
        confidence = round(np.max(prediction) * 100, 2)
        return predicted_class, confidence
    except Exception as e:
        return "Prediction failed", str(e)
