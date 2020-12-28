from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/files")
# def read_item(q: Optional[str] = None):
#     return {"file_id": file_id, "q": q}