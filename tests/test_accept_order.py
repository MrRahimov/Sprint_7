import allure

class TestAcceptOrder:
    @allure.title("Принять заказ — успешный сценарий")
    def test_accept_order_success(self, api, new_courier, new_order):
        _, courier_id = new_courier
        _, track, order_id = new_order
        r = api.accept_order(order_id, courier_id)
        assert r.status_code == 200
        body = r.json()
        assert body.get("ok") is True

    @allure.title("Принять заказ — не передан courierId")
    def test_accept_order_missing_courier(self, api, new_order):
        _, track, order_id = new_order
        r = api.accept_order(order_id, courier_id=None)
        assert r.status_code == 400
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)

    @allure.title("Принять заказ — неверные идентификаторы")
    def test_accept_order_wrong_ids(self, api):
        r = api.accept_order(order_id=999999999, courier_id=999999999)
        assert r.status_code == 404
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)
