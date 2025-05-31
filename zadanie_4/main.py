import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS

# Funkcja do wyznaczania rankingu na podstawie wyników
def rank_preferences(values, reverse=False):
    order = values.argsort()
    if reverse:
        order = order[::-1]
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(values) + 1)
    return ranks

# Przykładowa macierz decyzyjna - 4 laptopy, 4 kryteria
# Kryteria: [Cena (PLN), Wydajność (1-10), Bateria (godziny), Waga (kg)]
decision_matrix = np.array([
    [3200, 7, 6.5, 1.8],  # Laptop A
    [2900, 6, 8.0, 2.0],  # Laptop B
    [3500, 8, 5.5, 1.5],  # Laptop C
    [3100, 6.5, 7.0, 2.2] # Laptop D
])

# Typy kryteriów: -1 = minimalizacja, 1 = maksymalizacja
criteria_types = [-1, 1, 1, -1]

# Ręcznie przypisane wagi (suma = 1)
weights = np.array([0.3, 0.4, 0.2, 0.1])

# --- TOPSIS ---
topsis = TOPSIS()
topsis_scores = topsis(decision_matrix, weights, criteria_types)
topsis_ranks = rank_preferences(topsis_scores, reverse=True)

# --- SPOTIS ---
# Wyznaczenie dolnych i górnych granic dla każdego kryterium
bounds = np.array([
    [decision_matrix[:, i].min(), decision_matrix[:, i].max()]
    for i in range(decision_matrix.shape[1])
])

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, criteria_types)
spotis_ranks = rank_preferences(spotis_scores, reverse=False)

# Tabela z wynikami
results = pd.DataFrame({
    'Laptop': ['A', 'B', 'C', 'D'],
    'TOPSIS Score': np.round(topsis_scores, 4),
    'TOPSIS Rank': topsis_ranks,
    'SPOTIS Score': np.round(spotis_scores, 4),
    'SPOTIS Rank': spotis_ranks
})

print("Porównanie wyników metod TOPSIS i SPOTIS:\n")
print(results)
