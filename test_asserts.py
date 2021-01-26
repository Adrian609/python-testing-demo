def test_long_string(): 
    string = ("This is a very, very, long string that has some difference"
              "that are hard to catch")
    expected = ("This is very, very long string that hes some difference"
                "that are expected tocatch")
    assert string == expected # Should return false

def test_nested_dictionaties():
    result = {'first': 12, 'second': 13,
            'others': {'success': True, 'msg': 'A success message!'}}
    expected = {'first': 12, 'second': 13,
            'others': {'success': True, 'msg': 'A success message!'}}
    assert result == expected

def test_missing_key():
    result = {'first': 12, 'second': 13,
              'others': {'success': True, 'msg': 'A success message!'}}
    expected = {'first': 12, 'second': 13,
                'others': {'success': True, 'msg': 'A success message!'}}
    assert result == expected
