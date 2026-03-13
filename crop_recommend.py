def recommend_crop(soil_type, weather):

    temperature, humidity = weather

    if soil_type == "Loamy Soil":
        return "Wheat, Sugarcane, Cotton"

    elif soil_type == "Sandy Soil":
        return "Groundnut, Watermelon, Millets"

    elif soil_type == "Clay Soil":
        return "Rice, Broccoli, Cabbage"

    elif soil_type == "Red Soil":
        return "Potato, Pulses, Oil Seeds"

    elif soil_type == "Black Soil":
        return "Cotton, Soybean, Sunflower"

    else:
        return "Maize, Vegetables"