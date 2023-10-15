# app.py
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
from predictor import Predictor
import os


app = FastAPI()

prd = Predictor()


@app.post("/predict/")
async def predict(file: UploadFile):
    try:
        # Check if the uploaded file is an image file
        file_ext = os.path.splitext(file.filename)[1]
        if file_ext.lower() == ".jpg":
            # Save the uploaded file temporarily
            image_path = "image.jpg"
            with open(image_path, "wb") as image_data:
                image_data.write(file.file.read())
            img = Image.open(image_path).convert("RGB")
            # Assuming that 'prd' is a predefined object for prediction
            result = prd.predict(img)
            return result
        else:
            return {"error": "Uploaded file must be in JPG format."}
    except Exception as e:
        return {"error": str(e)}
