from wc_tool import utilities


def test_count_bytes():
    data = "Hello, world!"
    result = utilities.count_bytes(data)
    assert result == 13


def test_count_lines():
    data = b"Line 1\nLine 2\nLine 3"
    result = utilities.count_lines(data)
    assert result == 2


def test_count_words():
    data = "This is a test sentence."
    result = utilities.count_words(data)
    assert result == 5


def test_count_chars():
    data = b"Hello, world!"
    result = utilities.count_chars(data)
    assert result == 13
