from pyObjectId import *
def individual_serial(product) -> dict:
    return {
        "_id": PyObjectId(product["_id"]),
        "product_name": product["product_name"],
        "priceFrom": product["priceFrom"],
        "rating_point": product["rating_point"],
        "number_reviews": product["number_reviews"],
        "number_of_sales": product["number_of_sales"],
        "username_reviews": product["username_reviews"],
        "product_description": product["product_description"],
        "images": product["images"],
    }


async def list_serial(products) -> list:
    product_list = await products.to_list(lenght=None)
    return [individual_serial(product) for product in product_list]
