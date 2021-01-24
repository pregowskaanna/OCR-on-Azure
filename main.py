from fastapi import FastAPI, File, UploadFile, Header, Request, Form
import requests, os, sys
from pydantic import BaseModel
from typing import Optional
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError


vault_url = os.getenv('azure_key_vault_url')
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

try:
    api_key = client.get_secret(secret.azureCognitiveServicesAPIKey)
    api_version = client.get_secret(secret.azureCognitiveServicesAPIVersion)
    index_name = client.get_secret(secret.azureCognitiveServicesIndexName)

except HttpResponseError as e:
    print("\nThis sample has caught an error. {0}".format(e.message))
    
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

@app.post("/files/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.put("/files/create/")
async def create_file(request: Request, file: UploadFile = File(...)):
    content_length = request.headers['content-length']
    headers={"x-ms-type":file.file,
    "x-ms-content-length": content_length}
    filename = file.filename

    uri_create = f"https://bfkhabfkjwhfohfejwgfkg.file.core.windows.net/personal/data/{filename}?sv=2019-12-12&ss=bf&srt=co&sp=rwdlacx&se=2021-01-22T03:59:59Z&st=2021-01-21T19:59:59Z&spr=https&sig=8Gw3DdkeqrMecXJBmUgYAXPslIpLGApEKronGquesh4%3D"
    #try:
    response = requests.put(uri_create, headers=headers)
    #except requests.exceptions.HTTPError as e:

    # response = upload_file(file)
    return response.raw

async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    
    headers={"x-ms-type":file,
    "x-ms-content-length":len(bytes(file))}
    uri_upload = f"https://bfkhabfkjwhfohfejwgfkg.file.core.windows.net/personal/data/{filename}?comp=range&?sv=2019-12-12&ss=bf&srt=co&sp=rwdlacx&se=2021-01-22T03:59:59Z&st=2021-01-21T19:59:59Z&spr=https&sig=8Gw3DdkeqrMecXJBmUgYAXPslIpLGApEKronGquesh4%3D"
    response = requests.put(uri_upload, headers=headers)
    return response


@app.post("/files/uploadtest/")
async def create_file2(
    file: UploadFile = File(...)
):

    filename = file.filename

    uri_create = f"https://bfkhabfkjwhfohfejwgfkg.file.core.windows.net/personal/data/{filename}?sv=2019-12-12&ss=bf&srt=co&sp=rwdlacx&se=2021-01-22T03:59:59Z&st=2021-01-21T19:59:59Z&spr=https&sig=8Gw3DdkeqrMecXJBmUgYAXPslIpLGApEKronGquesh4%3D"
    response = requests.post(uri_create)

    return response
