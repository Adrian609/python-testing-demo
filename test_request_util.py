import request_util


class FakeResponse:
    def __init__(self, status=200, body=""):
        self.status = status
        self.body = body


def test_build_message_success(monkeypatch):  # using monkey patch fixture
    def fake_request():
        return FakeResponse()
    monkeypatch.setattr('request_util.make_request', fake_request)
    result = request_util.build_message()
    assert result["success"] is True


def test_build_message_failure(monkeypatch):
    def fake_request():
        return FakeResponse(status=400, body='not allowed here!')
    monkeypatch.setattr('request_util.make_request', fake_request)
    result = request_util.build_message()
    assert result['success'] is False
    assert result['error'] == 'not allowed here!'
