# Przykład użycia bibliotek NLP: TextBlob i spaCy

# --- TEXTBLOB ---
from textblob import TextBlob

# --- SPACY ---
import spacy

text = "Python is an amazing language. I love working with it!"
blob = TextBlob(text)

print("TextBlob - analiza sentymentu:")
print("Polaryzacja:", blob.sentiment.polarity)
print("Subiektywnosc:", blob.sentiment.subjectivity)
print("")


# Wczytanie modelu języka angielskiego
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("spaCy - tokeny i części mowy:")
for token in doc:
    print(f"{token.text:<12} -> {token.pos_}")
