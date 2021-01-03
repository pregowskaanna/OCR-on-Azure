from fastapi import FastAPI, File, UploadFile
import requests, os
from pydantic import BaseModel
from typing import Optional



api_key = os.getenv('APPSETTING_azure_cognitive_services_api_key')
app = FastAPI()

class Index(BaseModel):
    context: str
    value: Optional[str] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{param}")
def read_indexer(param: str):
    url = "https://ocr-a.search.windows.net/indexes/azureblob-index-2/docs?api-version=2020-06-30&api-key=" + api_key + "&search=" + param
    response = requests.get(url).json()
    index = create_index(response)
    return {"value": index['value']}

@app.post("/indexes/")
def create_index(index: Index):
    return index

@app.post("/files/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
