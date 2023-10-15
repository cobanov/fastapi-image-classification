import torch
import timm
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

from class_indices import class_indices


class Predictor:
    def __init__(self, model_name="resnet18") -> None:
        self.model = self.initialize_model(model_name)
        self.model.eval()
        self.config = resolve_data_config({}, model=self.model)
        self.transform = create_transform(**self.config)

    def initialize_model(self, model_name):
        return timm.create_model(model_name, pretrained=True)

    def predict(self, img):
        tensor = self.transform(img).unsqueeze(0)

        with torch.no_grad():
            out = self.model(tensor)

        probabilities = torch.nn.functional.softmax(out[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, 3)

        top_prob = top_prob.tolist()
        top_catid = top_catid.tolist()

        data = {"predictions": []}

        for idx, prob in zip(top_catid, top_prob):
            prediction = {
                "class_name": class_indices[idx],
                "probability": prob,
                "class_index": idx,
            }
            data["predictions"].append(prediction)

        return data
