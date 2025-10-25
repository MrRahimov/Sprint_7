import allure
from urls import BASE_URL

class TestDeleteCourier:
    @allure.title("Удалить курьера — успешный сценарий")
    def test_delete_courier_success(self, api, new_courier):
        _, cid = new_courier
        r = api.delete_courier(cid)
        assert r.status_code == 200 and r.json().get("ok") is True

    @allure.title("Удалить курьера — отсутствует id в пути")
    def test_delete_courier_no_id_path(self, api):
        r = api.s.delete(f"{BASE_URL}api/v1/courier/")
        assert r.status_code == 404
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)

    @allure.title("Удалить курьера — несуществующий id")
    def test_delete_courier_nonexistent(self, api):
        r = api.delete_courier(99999999)
        assert r.status_code == 404
        body = r.json()
        assert "message" in body and isinstance(body["message"], str)
