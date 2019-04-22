from willamette_client import WillametteClient


class TestClient:

    def test_instantiation(self):
        base_url = 'http://willamette.quaerere.local:5000/api'
        client = WillametteClient(base_url)

        assert client.url_base == base_url
        assert client.v1.version == 'v1'
