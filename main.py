from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

class IndexerData(BaseModel):
    context: str
    value: Optional[str] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{param}")
def read_indexer(param: str):
    api_key = azure_cognitive_services_api_key
    url = "https://ocr-a.search.windows.net/indexes/azureblob-index-2/docs?api-version=2020-06-30&api-key={api_key}&search="
    url = url + param
    response = requests.get(url)
    return {"url": url, "response": response}

@app.post("/files/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
