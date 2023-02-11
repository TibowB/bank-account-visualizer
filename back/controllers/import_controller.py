
from app import app
from services import ImportService
from fastapi import UploadFile
from ofxparse import OfxParser

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    import_service = ImportService(OfxParser)

    result = import_service.import_ofx_file(file.file)

    return result