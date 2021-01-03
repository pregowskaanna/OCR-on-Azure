from fastapi import FastAPI, File, UploadFile


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{param}")
def read_indexer(param: str):
    url = "https://ocr-a.search.windows.net/indexes/azureblob-index-2/docs?api-version=2020-06-30&search="
    url = url + param
    response = RedirectResponse(url=url)
    return {"response": response}

@app.post("/files/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
