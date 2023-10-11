"""Test module for function sort_dep from hw1.py."""


import pytest

from hw1 import sort_dep

test = (
    (
        (
            (
                ('dep4', [11, 21, 31, 41, 5]),
                ('dep2', [12, 33, 7, 5]),
                ('dep3', [5, 10, 4, 20]),
                ('dep1', [3, 4, 5]),
                ('dep5', [390, 2, 100]),
                ('dep6', [8]),
                ('dep7', [32, 40]),
            ),
            (
                None
            ),
            (
                (['dep5', 'dep7', 'dep4'], ['dep3', 'dep6', 'dep1'])
            ),
        )
    ),
    (
        (
            (
                ('depart4', [11, 21, 31, 41, 5]),
                ('depart2', [12, 33, 7, 5]),
                ('depart3', [5, 10, 4, 20]),
                ('depart1', [3, 4, 5]),
                ('depart5', [390, 2, 100]),
                ('depart6', [8]),
                ('depart7', [32, 40]),
            ),
            (
                20
            ),
            (
                (['depart5', 'depart7', 'depart2'], ['depart2', 'depart4', 'depart3'])
            ),
        )
    ),
    (
        (
            (
                ('dep_4', [11, 21, 31, 41, 5]),
                ('dep_2', [12, 33, 7, 5]),
                ('dep_3', [5, 10, 4, 20]),
                ('dep_1', [3, 4, 5]),
                ('dep_5', [390, 2, 100]),
                ('dep_6', [8]),
                ('dep_7', [32, 40]),
            ),
            (
                1000000
            ),
            (
                ((), ())
            ),
        )
    ),
    (
        (
            (
            ),
            (
                1000000
            ),
            (
                ((), ())
            ),
        )
    ),
    (
        (
            (),
            (
                None
            ),
            (
                ((), ())
            ),
        )
    ),
    (
        (
            (
                ('dep4', [0]),
                ('dep2', [0, 0, 0, 0]),
                ('dep3', [0, 0, 0]),
                ('dep1', [0, 0, 0]),
                ('dep5', [0, 0, 0]),
                ('dep6', [0]),
                ('dep7', [0, 0, 0, 0, 0, 0]),
            ),
            (
                None
            ),
            (
                ((), ())
            ),
        )
    ),
)


@pytest.mark.parametrize('input_data, limit, expected', test)
def test_calc_dep(input_data, limit, expected):
    """Created function that tests sort_dep function.

    Args:
        input_data: tuple - Department name and employee salary.
        limit: int -  Salary limit below which does not need to be taken into account.
        expected: tuple - expected value from function.
    """
    assert sort_dep(*input_data, limit=limit) == expected
