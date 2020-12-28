from fastapi import FastAPI, File, UploadFile


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/files/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}