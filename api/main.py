from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()
MODEL = tf.keras.models.load_model('../model')

def read_file_as_image(data)-> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    data = await file.read()
    image = read_file_as_image(data)
    prediction = MODEL.predict(image)
    if prediction>0.5:
        result="Fractured"
    else:
        result="Not Fractured"
    predicted_class = result
    confidence = prediction
    return {"class": predicted_class, "confidence": float(confidence)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
