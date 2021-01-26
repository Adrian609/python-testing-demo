from urllib import request


def make_request():
    #raise RuntimeError('this should fail!') # monkey patching can give false test pass 
    response = request.urlopen('http://api.example.com')
    response.body = response.read()
    return response


def build_message():
    response = make_request()
    message = {
        'success': True,
        'error': '',
    }
    if response.status >= 400:
        message['success'] = False
        message['error'] = response.body
    return message
