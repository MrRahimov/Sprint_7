class TestOrdersList:
    def test_orders_list_contains_orders_array(self, api, new_order):
        r = api.list_orders()
        assert r.status_code == 200 and isinstance(r.json().get("orders"), list)
