from pydantic import BaseModel
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from models import ProductInDB


async def list_products_as_json(products: AsyncIOMotorCollection) -> List[ProductInDB]:
    product_list = await products.find().to_list(None)
    return [ProductInDB(
        product_name=product["product_name"],
        priceFrom=product["priceFrom"],
        rating_point=product["rating_point"],
        number_of_reviews=product["number_of_reviews"],
        number_of_sales=product["number_of_sales"],
        username_reviews=product["username_reviews"],
        product_description=product["product_description"],
        images=product["images"]
    ) for product in product_list]