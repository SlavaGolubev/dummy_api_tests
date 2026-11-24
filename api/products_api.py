import requests

from api.base_client import BaseClient



class ProductsApi(BaseClient):
    def get_products(self, limit: int | None = None, skip: int | None = None) -> requests.Response:
        raw_params = {"limit": limit, "skip": skip}
        params = {k: v for k, v in raw_params.items() if v is not None}
        return self.get("/products", params=params)

    def get_product_by_id(self, id_: int) -> requests.Response:
        return self.get(f"/products/{id_}")

    def product_search(self, query: str) -> requests.Response:
        params = {"q": query}
        return self.get("/products/search", params=params)

    def add_product(self, title: str, price: float, category: str) -> requests.Response:
        body = {"title": title,
                "price": price,
                "category": category}

        return self.post("/products/add", json=body)
