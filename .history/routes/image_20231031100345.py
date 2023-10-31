# Trong file fastapi_app.py
from fastapi import FastAPI, UploadFile, APIRouter
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import base64
from db import images_collection
from fastapi import APIRouter, UploadFile
from fastapi.params import File
from starlette import status
import uuid
from PIL import Image
import os
router = APIRouter()

# Kết nối đến MongoDB


@router.post("/products/{product_id}/images/")
async def upload_image_for_product(
    product_id: str,
     file: UploadFile = File(...),
   
):
    upload_directory = "/uploads"
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)

    
    # Kiểm tra sự tồn tại của sản phẩm với product_id và xử lý lưu trữ hình ảnh tại đây
    filename = file.filename
    extension = filename.split(".")[-1]
    token_name = f"{uuid.uuid4()}.{extension}"
    generated_name = f"{upload_directory}/{token_name}"

    # Tiến hành xử lý hình ảnh (ví dụ: thay đổi kích thước) và lưu hình ảnh
    try:
        image = Image.open(generated_name)
        newSize = int(image.size[0] * 0.5), int(image.size[1] * 0.5)
        image.thumbnail(newSize, Image.ANTIALIAS)
        image.save(generated_name, optimize=True, quality=85)
    except IOError:
        # Xóa tệp hình ảnh nếu có lỗi
        os.remove(generated_name)
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "File extension not allowed"},
        )

    # Trả về URL của hình ảnh đã tải lên
    return JSONResponse(
        content={"status": 200, "detail": "Image uploaded", "file_url": generated_name},
    )