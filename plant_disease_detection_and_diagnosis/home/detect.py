from ultralytics import YOLO
import os
import json


# Get absolute path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "disease_detection.pt")
DISEASE_LABELS_PATH = os.path.join(os.path.dirname(__file__), "disease_labels.json")

# Load the model
model = YOLO(MODEL_PATH)

with open(DISEASE_LABELS_PATH, "r") as file:
    DISEASE_LABELS = json.load(file)

def get_disease_name(index):
    return DISEASE_LABELS.get(str(index), "Unknown Disease")


def detect_disease(images):
    results = model.predict(images)
    return [(get_disease_name(result.probs.top1), result.probs.top1) for result in results]
