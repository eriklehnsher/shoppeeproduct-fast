from fastapi import APIRouter,Body,status, HTTPException
from models import ProductInDB,ProductModel
from fastapi.encoders import jsonable_encoder
from db import Products_db
from fastapi.responses import JSONResponse
from typing import Optional, List
from bson import ObjectId

router = APIRouter()


@router.post("/product/create", response_model=ProductInDB)
async def create_product(product:ProductModel= Body(...)):
    product = product.model_dump()
    new_product = await Products_db.insert_one(product)
    create_product = await Products_db.find_one({"_id": new_product.inserted_id})
    return create_product
@router.get("/product/all", response_model=List[ProductInDB])
async def list_cars():
    products = await Products_db.find().to_list(1000)
    return products

#Get all car for admin
@router.get("/product/list-new", response_model=List[ProductInDB])
async def list_cars():
    products = await Products_db.find().to_list(5)
    return products

