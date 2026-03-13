import cv2
import numpy as np

def predict_soil(image):

    # Convert PIL image to numpy array
    img = np.array(image)

    # Resize image for processing
    img = cv2.resize(img, (200, 200))

    # Calculate average color
    avg_color = img.mean(axis=(0, 1))
    r, g, b = avg_color

    # Soil classification rules

    # Sandy soil (light yellow / pale color)
    if r > 170 and g > 170 and b > 120:
        soil_type = "Sandy Soil"

    # Red soil (high red value)
    elif r > g and r > b and r > 140:
        soil_type = "Red Soil"

    # Loamy soil (balanced brown color)
    elif r > 100 and g > 80 and b < 90:
        soil_type = "Loamy Soil"

    # Default
    else:
        soil_type = "Loamy Soil"

    return soil_type