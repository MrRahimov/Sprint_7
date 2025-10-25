BASE = "https://qa-scooter.praktikum-services.ru"
API = f"{BASE}/api/v1"

COURIER = f"{API}/courier"
COURIER_LOGIN = f"{API}/courier/login"

ORDERS = f"{API}/orders"
def ACCEPT_ORDER(order_id: int | str) -> str:
    return f"{ORDERS}/accept/{order_id}"
