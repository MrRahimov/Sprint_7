import pytest
import allure
from utils import build_order

class TestCreateOrder:
    @allure.title("Создать заказ — разные варианты цвета")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [], None])
    def test_create_order_various_colors(self, api, colors):
        payload = build_order(colors=colors)
        r = api.create_order(payload)
        assert r.status_code == 201 and isinstance(r.json().get("track"), int)
