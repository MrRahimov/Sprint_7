import allure

@allure.title("Принять заказ — успешный сценарий")
def test_accept_order_success(api, new_courier, new_order):
    _p, courier_id = new_courier
    _op, _track, order_id = new_order
    r = api.accept_order(order_id, courier_id)
    assert r.status_code == 200
    body = r.json()
    assert body.get("ok") is True

@allure.title("Принять заказ — не передан courierId")
def test_accept_order_missing_courier(api, new_order):
    _op, _track, order_id = new_order
    r = api.accept_order(order_id, courier_id=None)
    assert r.status_code == 400
    body = r.json()
    assert "message" in body and isinstance(body["message"], str) and body["message"]

@allure.title("Принять заказ — неверные идентификаторы")
def test_accept_order_wrong_ids(api):
    r = api.accept_order(order_id=999999999, courier_id=999999999)
    assert r.status_code in (400, 404)
    body = r.json()
    assert "message" in body and isinstance(body["message"], str) and body["message"]
