from numbers_checks import check_number_in_list, check_number_in_column, check_number_in_row


def test_check_number_in_list():
    numbers = []
    x = 90
    assert check_number_in_list(x, numbers)


def test_check_number_in_column():
    x = 90
    col = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert not check_number_in_column(x, col)


def test_check_number_in_row():
    x = 90
    row = [2, 13]
    assert check_number_in_row(x, row)
