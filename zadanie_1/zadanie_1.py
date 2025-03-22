# Importujemy moduł random do wykorzystania jego funkcji
import random

# Tworzymy dwie listy
fruits = ["jabłko", "banan", "gruszka", "śliwka", "pomarańcza"]
colors = ["czerwony", "żółty", "zielony", "fioletowy", "pomarańczowy"]

# Łączymy listy za pomocą zip()
fruit_colors = list(zip(fruits, colors))
print("Owoce i ich kolory:", fruit_colors)

# Przykład użycia funkcji z modułu random - losowanie owocu
# Dokumentacja: https://docs.python.org/3/library/random.html
try:
    user_input = int(input("Podaj numer owocu (0-4): "))
    chosen_fruit = fruits[user_input]
    print(f"Wybrany owoc to: {chosen_fruit}, a jego kolor to: {colors[user_input]}")

# Obsługa wyjątku, gdy użytkownik poda coś, co nie jest liczbą
except ValueError:
    print("Błąd: Wprowadź liczbę od 0 do 4!")

# Obsługa wyjątku, gdy indeks jest poza zakresem listy
except IndexError:
    print("Błąd: Wprowadzony numer jest poza zakresem listy!")
