# my_awesome_lib/data_utils.py

def convert_to_int(value):
    """Konwertuje stringa na int, jeśli się uda, inaczej wyrzuca błąd"""
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' nie jest liczbą całkowitą.")
        # Zwracamy None, jeśli konwersja się nie udała.
        return None


def split_string(value, separator=','):
    """Dzieli ciąg na listę, używając separatora."""
    if not value:
        print("Error: Pusty ciąg!")
        return []

    # Dzielimy po separatorze, domyślnie przecinek
    return value.split(separator)