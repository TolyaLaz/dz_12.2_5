from utils.dicts import get_val


def test_get_val():
    assert get_val({"a": "123", "b": "456"}, "b") == "456"
    assert get_val({"a": "123", "b": "456"}, "c") == "git"
    assert get_val({"a": "123", "b": "456"}, "a", "git") == "123"