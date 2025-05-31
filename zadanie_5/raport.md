
W ramach labów trzeba było znaleźć jakieś biblioteki do wybranego tematu. Ja wybrałem **analizę tekstu** – bo ciekawi mnie NLP i łatwo coś pokazać bez kombinowania.

Znalazłem dwie biblioteki:
- `TextBlob` – superprosta, fajna na start
- `spaCy` – trochę bardziej zaawansowana, ale też do ogarnięcia

---

## Jak używać?

Najpierw trzeba je zainstalować:

```bash
pip install textblob spacy
python -m spacy download en_core_web_sm
```

---

## Co robi skrypt?


1. TextBlob pokazuje **analizę sentymentu** (czy zdanie jest pozytywne/negatywne).
2. spaCy pokazuje **tokeny i części mowy** (czyli co jest czasownikiem, co rzeczownikiem itd.).

---

## Przykład działania:

```
TextBlob - analiza sentymentu:
Polaryzacja: 0.8
Subiektywnosc: 0.75

spaCy - tokeny i części mowy:
Python       -> PROPN
is           -> AUX
an           -> DET
amazing      -> ADJ
...
```

