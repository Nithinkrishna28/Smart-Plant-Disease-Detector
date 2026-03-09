import random

diseases = [
    "Powdery Mildew",
    "Leaf Spot",
    "Bacterial Blight"
]

def detect():
    return random.choice(diseases)
