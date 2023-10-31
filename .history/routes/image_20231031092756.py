# Trong file fastapi_app.py
from fastapi import FastAPI, UploadFile, APIRouter
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import base64
from db import images_collection
router = APIRouter()

# Kết nối đến MongoDB


@router.post("/upload/")
async def upload_image(file: UploadFile):
    # Đọc dữ liệu từ tệp hình ảnh
    image_data = await file.read()
    
    # Chuyển đổi dữ liệu hình ảnh thành chuỗi Base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    # Lưu tệp hình ảnh (dưới dạng chuỗi Base64) vào MongoDB và đợi cho đến khi tác vụ hoàn thành
    result = await images_collection.insert_one({"data": image_base64})
    
    if result.inserted_id:
        return JSONResponse(content={"detail": "Image uploaded and saved to MongoDB"})
    else:
        return JSONResponse(content={"detail": "Failed to save image to MongoDB"})