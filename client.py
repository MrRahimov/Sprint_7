import requests
from settings import API_V1

class ScooterApi:
    def __init__(self):
        self.s = requests.Session()

    def create_courier(self, payload):
        return self.s.post(f"{API_V1}/courier", json=payload)

    def login_courier(self, payload):
        return self.s.post(f"{API_V1}/courier/login", json=payload)

    def delete_courier(self, courier_id: int):
        return self.s.delete(f"{API_V1}/courier/{courier_id}")

    def create_order(self, payload):
        return self.s.post(f"{API_V1}/orders", json=payload)

    def list_orders(self, params=None):
        return self.s.get(f"{API_V1}/orders", params=params)

    def get_order_by_track(self, track: int):
        return self.s.get(f"{API_V1}/orders/track", params={"t": track})

    def cancel_order(self, track: int):
        return self.s.put(f"{API_V1}/orders/cancel", params={"track": track})

    def accept_order(self, order_id: int, courier_id: int):
        return self.s.put(f"{API_V1}/orders/accept/{order_id}", params={"courierId": courier_id})
