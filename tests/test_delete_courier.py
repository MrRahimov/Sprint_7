class TestDeleteCourier:
    def test_delete_courier_success(self, api, new_courier):
        _p, cid = new_courier
        r = api.delete_courier(cid)
        assert r.status_code == 200 and r.json().get("ok") is True

    def test_delete_courier_no_id_path(self, api):
        r = api.s.delete("https://qa-scooter.praktikum-services.ru/api/v1/courier/")
        assert r.status_code in (400, 404)

    def test_delete_courier_nonexistent(self, api):
        r = api.delete_courier(99999999)
        assert r.status_code in (404, 400)
