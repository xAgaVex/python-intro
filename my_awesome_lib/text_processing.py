# my_awesome_lib/text_processing.py

def to_uppercase(text):
    """Zmienia tekst na wielkie litery."""
    if not text:
        return ""  # Zwracamy pusty string, jeśli wejście jest puste
    return text.upper()


def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem."""
    if not text:
        return False  # Jeśli tekst jest pusty, zwracamy False

    # Usuwamy wszystkie spacje i zamieniamy na małe litery
    text = text.replace(" ", "").lower()
    return text == text[::-1]  # Sprawdzamy, czy tekst jest taki sam od tyłu
