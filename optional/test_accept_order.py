class TestAcceptOrder:
    def test_accept_order_success(self, api, new_courier, new_order):
        _p, courier_id = new_courier
        _op, _track, order_id = new_order
        r = api.accept_order(order_id, courier_id)
        assert r.status_code == 200 and r.json().get("ok") is True

    def test_accept_order_missing_courier(self, api, new_order):
        _op, _track, order_id = new_order
        r = api.s.put(f"https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}")
        assert r.status_code in (400, 404)

    def test_accept_order_wrong_ids(self, api):
        r = api.accept_order(999999, 999999)
        assert r.status_code in (404, 400)
