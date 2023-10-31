from pydantic import BaseModel, Field
from typing import List
from pyObjectId import *

class ProductInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    product_name: str
    priceFrom: str
    rating_point: float
    number_of_reviews: int
    number_of_sales: int
    username_reviews: str
    product_description: str
    images: List[object] = Field(...)
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    
class ProductModel(BaseModel):
    product_name: str
    priceFrom: str
    rating_point: float
    number_of_reviews: int
    number_of_sales: int
    username_reviews: str
    product_description: str
    images: List[object] = Field(...)
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "product_name": "MITSUBISHI 2019",
                "priceFrom": "priceFrom__shopee",
                "rating_point": 2,
                "number_of_sales": 20,
                "number_of_reviews": 20,
                "product_description": "short description",
                "images": [],
              
            }
        }