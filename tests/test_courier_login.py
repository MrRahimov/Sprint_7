import pytest

class TestCourierLogin:
    def test_login_success_returns_id(self, api, new_courier):
        payload, _cid = new_courier
        r = api.login_courier({"login": payload["login"], "password": payload["password"]})
        assert r.status_code == 200 and isinstance(r.json().get("id"), int)

    @pytest.mark.parametrize("missing_key", ["login", "password"])
    def test_login_missing_required(self, api, new_courier, missing_key):
        payload, _ = new_courier
        body = {"login": payload["login"], "password": payload["password"]}
        body.pop(missing_key)
        r = api.login_courier(body)
        assert r.status_code in (400, 504)

    def test_login_wrong_creds(self, api):
        r = api.login_courier({"login": "no_such_user", "password": "bad"})
        assert r.status_code in (404, 401)

    def test_login_nonexistent_user(self, api):
        r = api.login_courier({"login": "ghost_user_123", "password": "any"})
        assert r.status_code in (404, 401)
