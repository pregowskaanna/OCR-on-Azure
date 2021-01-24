from fastapi import FastAPI, File, UploadFile, Header, Request, Form
import requests, os, sys
from pydantic import BaseModel
from typing import Optional


api_key = os.getenv('APPSETTING_azure_cognitive_services_api_key')
api_version = os.getenv('APPSETTING_azure_cognitive_services_api_version')
index_name = os.getenv('APPSETTING_azure_cognitive_services_index_name')
app = FastAPI()

class Index(BaseModel):
    context: str
    value: Optional[str] = None
        
class Value(BaseModel):
    score: float
    content: str
    metadata_storage_content_type: str
    metadata_storage_path: str
    language: str
    merged_content: str
    text: str
    layoutText: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{param}")
def read_indexer(param: str):
    url = "https://ocr-a.search.windows.net/indexes/" + index_name + "/docs?api-version=" + api_version + "&api-key=" + api_key + "&search=" + param
    response = requests.get(url).json()
    index = create_index(response)
    value = create_value(index['value'])
    return {"value": value[0]['text']}

@app.post("/indexes/")
def create_index(index: Index):
    return index

@app.post("/values/")
def create_value(value: Value):
    return value


@app.put("/files/create/")
async def create_file(request: Request, file: bytes = File(...)):
    # content_length = request.headers['content-type']
    import logging
    # logging.warning(content_length)
    # print(type(typs))
    headers = {
        "x-ms-type": str(file.strip().replace(b'\n', b'').replace(b'\r',b'')),
        "x-ms-content-length": str(len(file)),
        # "x-ms-version": ""

    }

    logging.warning(headers)

    filename = 'dddssss-no-org-filename.jpg'#file.filename

    uri_create = f"https://bfkhabfkjwhfohfejwgfkg.file.core.windows.net/personal/data/{filename}?sv=2019-12-12&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-03-25T18:15:04Z&st=2021-01-24T10:15:04Z&spr=https&sig=RPqLBc69dUglY1G6CwAgmhO4XIQyh47JU%2BA3JPwOBn4%3D"#?sv=2019-12-12&ss=bf&srt=co&sp=rwdlacx&se=2021-01-22T03:59:59Z&st=2021-01-21T19:59:59Z&spr=https&sig=8Gw3DdkeqrMecXJBmUgYAXPslIpLGApEKronGquesh4%3D"
    #try:

    response = requests.put(uri_create, headers=headers)
    
    #except requests.exceptions.HTTPError as e:

    response = await upload_file(filename, file)

    return {}

async def upload_file(filename, file: bytes = File(...)):
    # filename = file.filename
    
    # headers={"x-ms-type":file,
    # "x-ms-content-length":len(bytes(file))}
    headers={"x-ms-type": str(file.strip().replace(b'\n', b'').replace(b'\r',b'')),
    "x-ms-content-length": str(len(file))}

    uri_upload = f"https://bfkhabfkjwhfohfejwgfkg.file.core.windows.net/personal/data/{filename}?comp=range&sv=2019-12-12&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-03-25T18:15:04Z&st=2021-01-24T10:15:04Z&spr=https&sig=RPqLBc69dUglY1G6CwAgmhO4XIQyh47JU%2BA3JPwOBn4%3D"#?sv=2019-12-12&ss=bf&srt=co&sp=rwdlacx&se=2021-01-22T03:59:59Z&st=2021-01-21T19:59:59Z&spr=https&sig=8Gw3DdkeqrMecXJBmUgYAXPslIpLGApEKronGquesh4%3D"
    response = requests.put(uri_upload, headers=headers)
    return response

