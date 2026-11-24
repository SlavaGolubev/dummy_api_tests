import requests
from api.base_client import BaseClient


class CartAPI(BaseClient):
    def get_cart_by_id(self, cart_id: int) -> requests.Response:
        return  self.get(f"/carts/{cart_id}")

    def create_cart(self, user_id: int, product_list: list[dict]) -> requests.Response:
        body = {"userId": user_id, "products": product_list}
        return self.post(f"/carts/add", json=body)

    def update_cart(self, cart_id: int, product_list: list[dict], merge: bool=True) -> requests.Response:
        body = {"merge": merge, "products": product_list}
        return self.put(f"/carts/{cart_id}", json=body)

    def delete_cart(self, cart_id: int) -> requests.Response:
        return self.delete(f"/carts/{cart_id}")