def is_number(it):
    if not isinstance(it,str) or it is None:
        return False

    if it.isnumeric():
        return True

    if "." not in it:
        return False

    ls = list(it.split('.'))
    if len(ls) != 2:
        return False

    if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
        return True

    return False