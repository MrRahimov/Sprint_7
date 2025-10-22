import pytest
from utils import build_courier

class TestCourierCreate:
    def test_create_courier_success(self, api, new_courier):
        payload, _cid = new_courier
        r = api.login_courier({"login": payload["login"], "password": payload["password"]})
        assert r.status_code == 200 and "id" in r.json()

    def test_create_courier_duplicate(self, api, new_courier):
        payload, _cid = new_courier
        r2 = api.create_courier(payload)
        assert r2.status_code == 409

    @pytest.mark.parametrize("missing_key", ["login", "password", "firstName"])
    def test_create_courier_missing_required(self, api, missing_key):
        p = build_courier()
        p.pop(missing_key)
        r = api.create_courier(p)
        if missing_key == "firstName":
            assert r.status_code == 201 and r.json().get("ok") is True
        else:
            assert r.status_code == 400
