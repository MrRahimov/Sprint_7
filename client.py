import requests
import allure
from urls import COURIER, COURIER_LOGIN, ORDERS, ACCEPT_ORDER

class ScooterApi:
    def __init__(self):
        self.s = requests.Session()

    @allure.step("Создать курьера")
    def create_courier(self, payload: dict):
        return self.s.post(COURIER, data=payload)

    @allure.step("Логин курьера")
    def login_courier(self, payload: dict):
        return self.s.post(COURIER_LOGIN, data=payload)

    @allure.step("Создать заказ")
    def create_order(self, payload: dict):
        return self.s.post(ORDERS, json=payload)

    @allure.step("Получить список заказов")
    def get_orders(self, params: dict | None = None):
        return self.s.get(ORDERS, params=params)

    @allure.step("Принять заказ: order_id={order_id}, courier_id={courier_id}")
    def accept_order(self, order_id: int | str, courier_id: int | str | None):
        # В API courierId передаётся как query-param
        params = {} if courier_id is None else {"courierId": courier_id}
        return self.s.put(ACCEPT_ORDER(order_id), params=params)

    @allure.step("Получить заказ по треку: track={track}")
    def get_order_by_track(self, track: int | str):
        return self.s.get(f"{ORDERS}/track", params={"t": track})

    @allure.step("Удалить курьера: id={courier_id}")
    def delete_courier(self, courier_id: int | str):
        return self.s.delete(f"{COURIER}/{courier_id}")
