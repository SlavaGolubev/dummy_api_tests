from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field

class CartProduct(BaseModel):
    id: int
    title: str
    price: Decimal = Field(gt=0)
    quantity: int = Field(gt=0)
    total: Decimal = Field(gt=0)
    discountPercentage: float = Field(ge=0)
    discountedTotal: Decimal | None = Field(ge=0, default=None)
    thumbnail: str

class CartResponse (BaseModel):
    id: int
    products: list[CartProduct] = list()
    total: Decimal = Field(ge=0, default=0)
    discountedTotal: Decimal = Field(ge=0, default=0)
    userId: int
    totalProducts: int = 0
    totalQuantity: int = 0

class DeletedCartResponse(CartResponse):
    isDeleted: bool
    deletedOn: datetime
