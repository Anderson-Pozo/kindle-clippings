from fastapi import FastAPI, UploadFile, HTTPException
from .utils.extract import extract_data

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    if not file.filename.lower().endswith(('.txt')):
        raise HTTPException(status_code=400, detail="File extension is not valid")

    content = await file.read()
    result = extract_data(content)
    
    return {
      "total": len(result),
      "phrases_info": result
    }