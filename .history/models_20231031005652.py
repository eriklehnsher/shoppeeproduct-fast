from pydantic import BaseModel, Field
from typing import List, 
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
    product_images: List[object]
    
    
    
class ProductModel(BaseModel):
    product_name: str
    priceFrom: str
    rating_point: float
    number_of_reviews: int
    number_of_sales: int
    username_reviews: str
    product_description: str
    product_images: List[object]