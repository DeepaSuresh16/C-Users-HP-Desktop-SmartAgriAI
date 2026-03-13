import numpy as np
import cv2

def predict_leaf(image):

    img = np.array(image)
    img = cv2.resize(img,(200,200))

    avg = img.mean()

    if avg > 160:
        disease = "Healthy Leaf"
        solution = "Plant looks healthy"

    elif avg > 120:
        disease = "Early Blight"
        solution = "Use copper fungicide"

    elif avg > 80:
        disease = "Leaf Spot"
        solution = "Use fungicide spray"

    else:
        disease = "Severe Disease"
        solution = "Remove infected leaves"

    return disease, solution