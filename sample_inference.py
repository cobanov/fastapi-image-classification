from PIL import Image
from predictor import Predictor

img = Image.open("./images/cat.jpg").convert("RGB")
prd = Predictor()
result = prd.predict(img)
print(result)
