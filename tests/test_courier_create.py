import pytest
import allure

@allure.title("Создать курьера — happy path")
def test_create_courier_success(api):
    from utils import build_courier
    p = build_courier()
    r = api.create_courier(p)
    assert r.status_code == 201
    assert r.json().get("ok") is True

@allure.title("Создать курьера — дублирующий логин возвращает ошибку")
def test_create_courier_duplicate(api):
    from utils import build_courier
    p = build_courier()
    api.create_courier(p)
    r = api.create_courier(p)
    assert r.status_code == 409
    assert "Этот логин уже используется" in r.text or r.json().get("message")

@pytest.mark.parametrize("missing_key", ["login", "password"])
@allure.title("Создать курьера — отсутствует обязательное поле")
def test_create_courier_missing_required(api, missing_key):
    from utils import build_courier
    p = build_courier()
    p.pop(missing_key)
    r = api.create_courier(p)
    assert r.status_code == 400
    body = r.json()
    assert "message" in body and isinstance(body["message"], str) and body["message"]

@allure.title("Создать курьера — firstName отсутствует (необязательное поле)")
def test_create_courier_without_first_name_ok(api):
    from utils import build_courier
    p = build_courier()
    p.pop("firstName")
    r = api.create_courier(p)
    assert r.status_code == 201
    assert r.json().get("ok") is True
