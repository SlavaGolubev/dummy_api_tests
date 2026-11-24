from typing import Optional

from pydantic import BaseModel


class ProductItem(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: list[str]
    brand: Optional[str] = None
    sku: str
    weight: int
    dimensions: dict
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: list[dict]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: dict
    images: list[str]
    thumbnail: str


class ProductListResponse(BaseModel):
    products: list[ProductItem]
    total: int
    skip: int
    limit: int