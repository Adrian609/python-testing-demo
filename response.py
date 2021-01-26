def build_message(response):
    # Dictionary
    message = {
        "success": True,
        "error": "",
    }
    if response.status >= 400:
        message['success'] = False
        message['error'] = response.body
    return message


def test_build_message_success(response):
    result = build_message(response())
    assert result['success'] is True


def test_build_message_failure(response):
    result = build_message(response(400, 'not allowed here!'))
    assert result["success"] is False
    assert result['error'] == 'not allowed here!'
