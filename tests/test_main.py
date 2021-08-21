from main import return_ok_string


class TestMain:
    def test_return_ok(self):
        assert return_ok_string() == "ok"
