from transformers import pipeline

qa_model = pipeline("question-answering")

context = """
Plants need proper soil, water and nutrients to grow.

Rice grows well in clay soil.
Wheat grows well in loamy soil.
Cotton grows well in black soil.
Groundnut grows well in sandy soil.

Leaf spot disease can be treated using fungicide spray.
Early blight can be controlled using copper fungicide.

Healthy plants require proper sunlight and irrigation.
"""

def farmer_chatbot(question):

    result = qa_model(
        question=question,
        context=context
    )

    return result["answer"]