VERSION = "0.0.1"


def format_years(years):
    postfix = ''
    count = years % 100
    if (count >= 5 and count <= 20):
        postfix = 'лет'
    else:
        count = count % 10;
        if count == 1:
            postfix = 'год'
        elif count >= 2 and count <= 4:
            postfix = 'года'
        else:
            postfix = 'лет'
    return postfix
