import pytest

from api.products_api import ProductsApi
from models.auth_models import ErrorResponse
from models.products_models import ProductListResponse, ProductItem


class TestProducts:

    @pytest.mark.parametrize(
        "limit, skip",
        [
            pytest.param(None, None, marks=pytest.mark.smoke),
            pytest.param(15, 3, marks=pytest.mark.regression),
        ],
        ids=['no_params', 'with_params']
    )
    def test_get_products(self, products_api: ProductsApi, limit, skip):
        response = products_api.get_products(limit=limit, skip=skip)
        assert response.status_code == 200
        products_data = ProductListResponse(**response.json())
        if limit:
            assert products_data.limit == limit
        else:
            assert products_data.limit == 30
        if skip:
            assert products_data.skip == skip
            assert products_data.products[0].id == skip + 1

    @pytest.mark.smoke
    def test_get_product_by_id(self, products_api: ProductsApi):
        response = products_api.get_product_by_id(2)
        assert response.status_code == 200
        product_data = ProductItem(**response.json())
        assert product_data.id == 2

    @pytest.mark.regression
    def test_get_product_by_nonexisting_id(self, products_api: ProductsApi):
        response = products_api.get_product_by_id(999999)
        assert response.status_code == 404, (
            f"Expected 404, got {response.status_code}: {response.text}"
        )
        error = ErrorResponse(**response.json())
        assert "not found" in error.message

    @pytest.mark.parametrize(
        "query, result",
        [
            pytest.param("lash", True, marks=pytest.mark.smoke),
            pytest.param("square pants", False, marks=pytest.mark.regression)
        ],
        ids=["valid_query", "invalid_query"]
    )
    def test_search_product(self, products_api: ProductsApi, query, result):
        response = products_api.product_search(query)
        assert response.status_code == 200
        search_result = ProductListResponse(**response.json())
        assert bool(search_result.total) == result

    @pytest.mark.smoke
    def test_product_add(self, products_api: ProductsApi):
        response = products_api.add_product("BMW Pencil", 15.5, "stationery")

        assert response.status_code == 201
        assert response.json()["title"] == "BMW Pencil"
