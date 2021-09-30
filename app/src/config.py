import os

path = os.path.abspath("")
classes = (
    "plane",
    "car",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

PRED_TO_CLASS = {i: cl for i, cl in enumerate(classes)}
MODEL_PATH = os.path.join(path, "app/models", "savedmodel.pt")