from pathlib import Path
from hexlet_pytest.example import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_example():
    before_example = read_file('before_example')
    expected = read_file('after_example')
    actual = reverse(before_example)

    assert actual == expected