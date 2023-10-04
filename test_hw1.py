"""Those are tests for hw1."""
import pytest

from hw1 import get_salary_stats

nan = None

test_data = {
    'it': {
        'Bob': 1450.5,
        'Jeremy': 999.9,
        'Elijah': 1000,
        'Charlie': 150.45,
    },
    'marketing': {
        'Rimus': 1500,
        'Thomas': 1250.5,
        'Richard': 79893.12312,
        'Charlie': 150.45,
    },
    'managment': {
        'Elon': 99999999999.99999999,
        'Tim': 100,
    },
}


test_data_values = (
    ('it', ((1450.5, 1000, 999.9), 95.82)),
    ('marketing', ((79893.12, 1500, 1250.5), 99.82)),
    ('managment', ((100000000000.0, 100), 100.0)),
)


data_limit_test = (
    ('it', 1000, ((1000, 999.9, 150.45), 59.72)),
    ('marketing', nan, ((79893.12, 1500, 1250.5), 99.82)),
    ('managment', 0, ((), 0)),
)


@pytest.mark.parametrize('department, expected', test_data_values)
def test_salary_stat(department: str, expected: tuple):
    """Test function.

    Args:
        department: str, name of the dept.
        expected: tuple that is expected.

    """
    assert get_salary_stats(test_data, department) == expected


@pytest.mark.parametrize('department, limit, expected', data_limit_test)
def test_salary_stat_limit(department: str, limit: int, expected: tuple):
    """Test function.

    Args:
        department: str, name of the dept.
        limit: int, limit of salary that we are not exceeding
        expected: tuple that is expected.

    """
    assert get_salary_stats(test_data, department, limit) == expected
