import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from mtcnn import MTCNN
import numpy as np
from PIL import Image

# Cargar el modelo MobileNetV2 preentrenado
mobilenet_model = MobileNetV2(weights='imagenet')

# Inicializar MTCNN
face_detector = MTCNN()

def load_and_preprocess_image(img_path):
    img = Image.open(img_path)
    img = img.convert('RGB')  # Asegurarse de que la imagen está en modo RGB
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict_image(img_path):
    img_array = load_and_preprocess_image(img_path)
    predictions = mobilenet_model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=5)[0]
    
    for _, class_name, score in decoded_predictions:
        print(f"Predicción: {class_name} ({score * 100:.2f}%)")
    
    # Ampliar la lista de clases relacionadas con personas
    person_classes = [
        'person', 'man', 'woman', 'boy', 'girl', 'baby', 'bridegroom', 'groom', 'clown',
        'scuba_diver', 'space_suit', 'swimmer', 'parachutist', 'thief'
    ]
    for _, class_name, score in decoded_predictions:
        if class_name in person_classes:
            return True
    
    # Si no se detecta una persona completa, usar MTCNN para detectar rostros
    img = Image.open(img_path)
    img = img.convert('RGB')  # Asegurarse de que la imagen está en modo RGB
    img_array = np.array(img)
    
    faces = face_detector.detect_faces(img_array)
    if faces:
        print(f"Rostros detectados: {len(faces)}")
        return True
    
    return False
