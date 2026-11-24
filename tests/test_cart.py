import pytest

from tests.products import products
from models.auth_models import ErrorResponse
from models.cart_models import CartResponse, DeletedCartResponse


class TestCart:
    @pytest.mark.smoke
    def test_get_cart_by_existing_id(self, cart_api):
        response = cart_api.get_cart_by_id(1)
        assert response.status_code == 200, f'Ожидался ответ 200, но получили {response.status_code}'
        cart_data = CartResponse(**response.json())
        assert cart_data.id == 1

    @pytest.mark.regression
    def test_get_cart_by_unexisting_id(self, cart_api):
        response = cart_api.get_cart_by_id(999999)
        assert response.status_code ==404, f'Ожидался ответ 404, но получили {response.status_code}'
        error = ErrorResponse(**response.json())
        assert 'not found' in error.message

    @pytest.mark.smoke
    def test_create_cart(self, cart_api):
        response = cart_api.create_cart(1, products)
        assert response.status_code == 201, f'Ожидался ответ 201, но получили {response.status_code}'
        CartResponse(**response.json())

    @pytest.mark.regression
    @pytest.mark.parametrize('merge',
                             [True, False],
                             ids=['with merge', 'without merge'])
    def test_change_cart(self, cart_api, merge):
        cart_id = 1
        product_id = 1
        cart_data_response = cart_api.get_cart_by_id(cart_id)
        assert cart_data_response.status_code == 200, f'Ожидался ответ 200, но получили {cart_data_response.status_code}'
        cart_data = CartResponse(**cart_data_response.json())
        old_quantity = cart_data.totalQuantity

        new_quantity = 3
        cart_changes = [{"id": product_id,
                         "quantity": new_quantity}]
        change_cart_response = cart_api.update_cart(cart_id, cart_changes, merge=merge)
        assert change_cart_response.status_code == 200, f'Ожидался ответ 200, но получили {cart_data_response.status_code}'
        changed_cart = CartResponse(**change_cart_response.json())

        if merge:
            assert changed_cart.totalQuantity == old_quantity + new_quantity
        else:
            assert changed_cart.totalQuantity == new_quantity

    @pytest.mark.smoke
    def test_delete_cart(self, cart_api):
        cart_id = 1

        delete_cart_response = cart_api.delete_cart(cart_id)
        assert delete_cart_response.status_code==200, f'Ожидался ответ 200, но получили {delete_cart_response.status_code}'
        validated_response = DeletedCartResponse(**delete_cart_response.json())
        assert validated_response.isDeleted
