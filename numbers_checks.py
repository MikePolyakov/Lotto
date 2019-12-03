def check_number_in_list(x, numbers):
    if x not in numbers:
        return True
    else:
        return False


def check_number_in_column(x, col):
    x_position = x // 10
    if x == 90:
        x_position = 8
    if col[x_position] < 1:
        return True
    else:
        return False


def check_number_in_row(x, row):
    if len(row) < 5:
        return True
    else:
        return False