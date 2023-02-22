# pyright: reportUnusedVariable=false
# pyright: reportGeneralTypeIssues=false
# flake8: noqa

import pytest

import lotto.model.lotto_number


def test_range_success():
    proper_lotto_number = lotto.model.lotto_number.LottoNumber(45)
    assert proper_lotto_number.number in range(
        lotto.model.lotto_number.MIN_LOTTO_NUMBER, lotto.model.lotto_number.MAX_LOTTO_NUMBER + 1
    )


def test_range_fail():
    with pytest.raises(ValueError):
        invalid_lotto_number = lotto.model.lotto_number.LottoNumber(46)


def test_null_number():
    with pytest.raises(Exception):
        empty_lotto_number = lotto.model.lotto_number.LottoNumber()
