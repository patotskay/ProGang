from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

from logger import CustomLogger

ANSWERS = []

class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")
logger = CustomLogger("./log.txt")


@app.get("/")
def root():
    logger.write("get root request", console=True)
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    ANSWERS.append(classifier(item.text)[0])
    logger.write(
        f"get root predict, result: {ANSWERS[-1]}",
        console=True
        )
   return ANSWERS[-1]


@app.post("/istoriya')
def get_istoriya(item: Item):
	logger.write(f"send istoriya", console=True)
	return {"last_answer": ANSWERS[-1]}
