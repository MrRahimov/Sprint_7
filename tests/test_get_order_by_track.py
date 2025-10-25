import allure

class TestGetOrderByTrack:
    @allure.title("Получить заказ по треку — успешный сценарий")
    def test_get_order_by_track_success(self, api, new_order):
        _, track, _ = new_order
        r = api.get_order_by_track(track)
        assert r.status_code == 200 and "order" in r.json()

    @allure.title("Получить заказ по треку — отсутствует параметр track")
    def test_get_order_by_track_missing(self, api):
        r = api.get_order_by_track(None)
        assert r.status_code == 400
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)

    @allure.title("Получить заказ по треку — заказ не найден")
    def test_get_order_by_track_not_found(self, api):
        r = api.get_order_by_track(99999999)
        assert r.status_code == 404
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)
