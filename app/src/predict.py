from app.src.model import Model
import app.src.config as config
from app.src.transforms import valid_transforms
import torch


def get_prediction(img):
    img = valid_transforms(img).unsqueeze(0).to("cpu")

    model = Model()
    model.load_state_dict(
        torch.load(config.MODEL_PATH, map_location=torch.device("cpu"))
    )
    model.eval()
    model.to("cpu")

    output = model(img).detach()
    pred_idx = output.numpy().argmax()

    return config.PRED_TO_CLASS[pred_idx]
