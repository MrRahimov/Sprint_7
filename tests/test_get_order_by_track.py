class TestGetOrderByTrack:
    def test_get_order_by_track_success(self, api, new_order):
        _op, track, _oid = new_order
        r = api.get_order_by_track(track)
        assert r.status_code == 200 and "order" in r.json()

    def test_get_order_by_track_missing(self, api):
        r = api.get_order_by_track(None)
        assert r.status_code in (400, 404)

    def test_get_order_by_track_not_found(self, api):
        r = api.get_order_by_track(99999999)
        assert r.status_code in (404, 400)
