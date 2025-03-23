
def is_valid_email(email):
    if email.count('@') != 1:
        return False

    local_part, domain = email.split('@')

    if not local_part or not domain:
        return False

    if '.' not in domain or domain.endswith('.'):
        return False

    return True


def rectangle_area(a, b):
    return a * b

def sort_list(list):
    return list.sort()

def convert_date(date):
    try:

        day, month, year = map(int, date.split('-'))
        if not (1 <= month <= 12):
            raise ValueError("Nieprawidłowy miesiąc")
        if not (1 <= day <= 31):
            raise ValueError("Nieprawidłowy dzień")
        if month in {4, 6, 9, 11} and day > 30:
            raise ValueError("Ten miesiąc ma tylko 30 dni")
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    raise ValueError("Luty ma maksymalnie 29 dni w roku przestępnym")
            else:
                if day > 28:
                    raise ValueError("Luty ma maksymalnie 28 dni w roku nieprzestępnym")

        return f"{year}/{month:02}/{day:02}"

    except ValueError:
        raise ValueError("Nieprawidłowy format daty")

def is_palidrome(text):
    text = text.lower().replace(" ", "")

    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False

    return True

