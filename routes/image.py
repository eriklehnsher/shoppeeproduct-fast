from ast import Param, Str
from os import remove, listdir
from typing import List
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.params import File, Security
from fastapi import Body
from fastapi.routing import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config import settings
import uuid
from PIL import Image


router = APIRouter()


# Upload a image
@router.post("/img")
async def upload_image(file: UploadFile = File(...)):
    path = f"{settings.upload_path}/products/"
    filename = file.filename

    # test.png >> ["test", "png"]
    extension = filename.split(".")[len(filename.split(".")) - 1]

    token_name = str(uuid.uuid4()) + "." + extension

    generated_name = path + token_name
    file_content = await file.read()
    with open(generated_name, "wb") as file:
        file.write(file_content)
    try:
        image = Image.open(generated_name)
        newSize = int(image.size[0] * 1), int(image.size[1] * 1)
        image.thumbnail(newSize, Image.LANCZOS)
        image.save(generated_name, optimize=True, quality=100)
    except IOError:
        remove(generated_name)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="File extension not allowed",
        )

    file_url = generated_name
    if file_url.split("/")[0] == ".":
        file_url = file_url[1:]
    return {"status": 200, "detail": "uploaded image", "file_url": file_url}


# Upload multi images
@router.post("/images/{type}")
async def upload_images(type: str, files: List[UploadFile] = File(...)):
    path = f"{settings.upload_path}/{type}/"
    files_url = []

    for file in files:
        filename = file.filename
        extension = filename.split(".")[len(filename.split(".")) - 1]
        token_name = str(uuid.uuid4()) + "." + extension
        generated_name = path + token_name
        file_content = await file.read()
        with open(generated_name, "wb") as file:
            file.write(file_content)
        try:
            image = Image.open(generated_name)
            newSize = int(image.size[0] * 0.5), int(image.size[1] * 0.5)
            image.thumbnail(newSize, Image.LANCZOS)
            image.save(generated_name, optimize=True, quality=85)
        except IOError:
            remove(generated_name)
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="File extension not allowed",
            )

        file_url = generated_name
        if file_url.split("/")[0] == ".":
            file_url = file_url[1:]
        files_url.append(file_url)

    return {"files_url": files_url}


@router.get("/carousels")
async def get_carousels():
    result = []
    path = f"{settings.upload_path}/carousel/"
    for image in listdir(f"{settings.upload_path}/carousel"):
        file_url = path + image
        if file_url.split("/")[0] == ".":
            file_url = file_url[1:]
        result.append(file_url)
    return {"images": result}
