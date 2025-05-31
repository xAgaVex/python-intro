

W ramach zajęć mieliśmy zrobić analizę z użyciem metod MCDM. Ja zdecydowałem się porównać 4 różne laptopy, patrząc na takie rzeczy jak:
- cena,
- wydajność,
- ile trzyma bateria,
- i ile waży.

Zastosowałem dwie metody: **TOPSIS** i **SPOTIS**, bo były wymagane.

---

## Dane, które użyłem

Zrobiłem sobie macierz decyzyjną z 4 laptopami i 4 kryteriami. Wagi wymyśliłem ręcznie (tak żeby miało sens):

| Kryterium      | Co z nim robimy     | Waga |
|----------------|---------------------|------|
| Cena           | im mniej tym lepiej | 0.3  |
| Wydajność      | im więcej tym lepiej| 0.4  |
| Bateria (h)    | więcej = lepiej     | 0.2  |
| Waga (kg)      | mniej = lepiej      | 0.1  |

---

## Jakie metody i po co?

- **TOPSIS** – porównuje każdy laptop do idealnego.
- **SPOTIS** – trochę inaczej, sprawdza kto jest najbliżej wzorcowego punktu.

Obie metody były dostępne w bibliotece `pymcdm`.

---

## Wyniki

W skrócie – każda metoda pokazała coś innego:

| Laptop | TOPSIS | SPOTIS |
|--------|--------|--------|
| A      | 2      | 3      |
| B      | 3      | 1      |
| C      | 1      | 2      |
| D      | 4      | 4      |

TOPSIS wybrał laptop **C**, a SPOTIS powiedział, że lepszy będzie **B**.

---

## Wnioski

Jak widać – zależy co dla kogo ważniejsze. Jak ktoś chce wydajność, to C. Jak balans, to B.

Obie metody dały sensowne wyniki i pokazały, że warto analizować na kilka sposobów.

---
