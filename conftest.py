import pytest
from client import ScooterApi
from utils import build_courier, build_order

@pytest.fixture(scope="session")
def api():
    return ScooterApi()

@pytest.fixture
def new_courier(api):
    payload = build_courier()
    r = api.create_courier(payload)
    if r.status_code == 409:
        payload = build_courier()
        r = api.create_courier(payload)
    assert r.status_code == 201
    login_r = api.login_courier({"login": payload["login"], "password": payload["password"]})
    assert login_r.status_code == 200 and "id" in login_r.json()
    courier_id = login_r.json()["id"]
    yield payload, courier_id
    api.delete_courier(courier_id)

@pytest.fixture
def new_order(api):
    order_payload = build_order()
    r = api.create_order(order_payload)
    assert r.status_code == 201 and "track" in r.json()
    track = r.json()["track"]
    get_r = api.get_order_by_track(track)
    assert get_r.status_code == 200 and "order" in get_r.json()
    order_id = get_r.json()["order"]["id"]
    yield order_payload, track, order_id
    api.cancel_order(track)
