import streamlit as st
from PIL import Image

from utils.soil_predict import predict_soil
from utils.leaf_predict import predict_leaf
from utils.weather import get_weather
from utils.crop_recommend import recommend_crop


# ---------------------------
# LANGUAGE SELECTION
# ---------------------------

language = st.selectbox(
    "Select Language",
    ["English", "Kannada", "Hindi", "Telugu", "Tamil"]
)

translations = {

"English":{
"title":"Smart Agriculture AI System",
"soil":"Upload Soil Image",
"leaf":"Upload Leaf Image",
"location":"Enter Location",
"analyze":"Analyze",
"soil_result":"Soil Type",
"disease":"Leaf Disease",
"solution":"Solution",
"crop":"Recommended Crop",
"assistant":"Farmer Assistant",
"question":"Ask a farming question",
"advice":"Get Advice"
},

"Kannada":{
"title":"ಸ್ಮಾರ್ಟ್ ಕೃಷಿ AI ವ್ಯವಸ್ಥೆ",
"soil":"ಮಣ್ಣಿನ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ",
"leaf":"ಎಲೆ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ",
"location":"ಸ್ಥಳವನ್ನು ನಮೂದಿಸಿ",
"analyze":"ವಿಶ್ಲೇಷಿಸಿ",
"soil_result":"ಮಣ್ಣಿನ ಪ್ರಕಾರ",
"disease":"ಎಲೆ ರೋಗ",
"solution":"ಪರಿಹಾರ",
"crop":"ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ",
"assistant":"ರೈತ ಸಹಾಯಕ",
"question":"ಕೃಷಿ ಪ್ರಶ್ನೆ ಕೇಳಿ",
"advice":"ಸಲಹೆ ಪಡೆಯಿರಿ"
},

"Hindi":{
"title":"स्मार्ट कृषि एआई सिस्टम",
"soil":"मिट्टी की फोटो अपलोड करें",
"leaf":"पत्ते की फोटो अपलोड करें",
"location":"स्थान दर्ज करें",
"analyze":"विश्लेषण करें",
"soil_result":"मिट्टी का प्रकार",
"disease":"पत्ते की बीमारी",
"solution":"समाधान",
"crop":"सुझाई गई फसल",
"assistant":"किसान सहायक",
"question":"कृषि प्रश्न पूछें",
"advice":"सलाह प्राप्त करें"
},

"Telugu":{
"title":"స్మార్ట్ వ్యవసాయ AI వ్యవస్థ",
"soil":"మట్టి చిత్రం అప్‌లోడ్ చేయండి",
"leaf":"ఆకు చిత్రం అప్‌లోడ్ చేయండి",
"location":"స్థానం నమోదు చేయండి",
"analyze":"విశ్లేషించండి",
"soil_result":"మట్టి రకం",
"disease":"ఆకు వ్యాధి",
"solution":"పరిష్కారం",
"crop":"సిఫార్సు చేసిన పంట",
"assistant":"రైతు సహాయకుడు",
"question":"వ్యవసాయ ప్రశ్న అడగండి",
"advice":"సలహా పొందండి"
},

"Tamil":{
"title":"ஸ்மார்ட் வேளாண்மை AI அமைப்பு",
"soil":"மண் படத்தை பதிவேற்றவும்",
"leaf":"இலை படத்தை பதிவேற்றவும்",
"location":"இடத்தை உள்ளிடவும்",
"analyze":"ஆய்வு செய்யவும்",
"soil_result":"மண் வகை",
"disease":"இலை நோய்",
"solution":"தீர்வு",
"crop":"பரிந்துரைக்கப்பட்ட பயிர்",
"assistant":"விவசாயி உதவியாளர்",
"question":"விவசாய கேள்வி கேளுங்கள்",
"advice":"ஆலோசனை பெறவும்"
}

}

text = translations[language]

# ---------------------------
# TITLE
# ---------------------------

st.title(text["title"])


# ---------------------------
# IMAGE UPLOAD
# ---------------------------

soil_file = st.file_uploader(text["soil"], type=["jpg","png","jpeg"])
leaf_file = st.file_uploader(text["leaf"], type=["jpg","png","jpeg"])


# ---------------------------
# LOCATION INPUT
# ---------------------------

location = st.text_input(text["location"])


# ---------------------------
# ANALYZE BUTTON
# ---------------------------

if st.button(text["analyze"]):

    if soil_file and leaf_file and location:

        soil_img = Image.open(soil_file)
        leaf_img = Image.open(leaf_file)

        col1, col2 = st.columns(2)

        with col1:
            st.image(soil_img, caption="Soil Image")

        with col2:
            st.image(leaf_img, caption="Leaf Image")

        # Soil Detection
        soil_type = predict_soil(soil_img)
        st.success(f"{text['soil_result']}: {soil_type}")

        # Leaf Detection
        disease, solution = predict_leaf(leaf_img)
        st.error(f"{text['disease']}: {disease}")
        st.info(f"{text['solution']}: {solution}")

        # Weather
        weather = get_weather(location)
        st.subheader("Weather Information")
        st.write(weather)

        # Crop Recommendation
        crop = recommend_crop(soil_type, weather)
        st.success(f"{text['crop']}: {crop}")

    else:
        st.warning("Please upload both images and enter location")


# ---------------------------
# FARMER ASSISTANT
# ---------------------------

st.header(text["assistant"])

question = st.text_input(text["question"])

if st.button(text["advice"]):

    q = question.lower()

    if "red soil" in q:
        answer = "Best crops for red soil are groundnut, potato, pulses and millets."

    elif "sandy soil" in q:
        answer = "Sandy soil is suitable for watermelon, peanuts, carrots and coconut."

    elif "loamy soil" in q:
        answer = "Loamy soil supports crops like wheat, maize, sugarcane and vegetables."

    elif "fertilizer" in q:
        answer = "Use organic compost and balanced NPK fertilizer."

    elif "irrigation" in q:
        answer = "Drip irrigation helps save water and improves crop yield."

    elif "disease" in q:
        answer = "Remove infected leaves and apply appropriate fungicide."

    else:
        answer = "Maintain proper irrigation, apply organic fertilizer and monitor plant health."

    st.success(answer)