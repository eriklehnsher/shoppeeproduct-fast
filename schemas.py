def individual_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "product_name": product["product_name"],
        "productPrice": product["productPrice"],
        "priceFrom": product["priceFrom"],
        "rating_point": product["rating_point"],
        "number_of_reviews": product["number_of_reviews"],
        "number_of_sales": product["number_of_sales"],
        "username_reviews": product["username_reviews"],
        "product_description": product["product_description"],
        "images": list(product["images"]),
    }


async def list_serial(products) -> list:
    product_list = await products.to_list(length=None)
    return [individual_serial(product) for product in product_list]
