from pydantic import BaseModel


class ProductItem(BaseModel):
    id: int
    title: str
    price: float
    category: str

class ProductListResponse(BaseModel):
    products: list[ProductItem]
    total: int
    skip: int
    limit: int