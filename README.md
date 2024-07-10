# Projekt: Regresja Liniowa z użyciem TensorFlow

## Opis projektu
- **Temat projektu**: Regresja liniowa z użyciem TensorFlow.
- **Cel projektu**: Trenowanie modelu regresji liniowej.
- **Funkcjonalności projektu**: Generowanie danych, trenowanie modelu, wyświetlanie wyników.
- **Technologie użyte w projekcie**: TensorFlow, Matplotlib, NumPy.

## Instrukcja uruchomienia projektu

1. Zainstaluj wymagane pakiety:
    ```sh
    pip install -r requirements.txt
    ```

2. Uruchom główny skrypt:
    ```sh
    python main.py
    ```
## Analiza wymagań

- **Wymagania funkcjonalne**:
    - Generowanie danych treningowych.
    - Trenowanie modelu regresji liniowej.
    - Wizualizacja wyników.

- **Wymagania niefunkcjonalne**:
    - Kod podzielony na moduły.
    - Obsługa błędów i wyjątków.
    - Testy jednostkowe.

## Implementacja

- **Struktura danych**: TensorFlow Variable, TensorFlow Tensor, NumPy .
- **Klasa i atrybuty**: Klasa `Model` z atrybutami `weight` i `bias`.
- **Moduły**: Kod podzielony na `main.py`, `model.py`, `utils.py`.
- **Błędy i wyjątki**: Obsługa błędów w `main.py`.
- **Generatory i listy składane**: Użyte w `generate_data`.
- **Biblioteka standardowa**: Użyto Matplotlib do wizualizacji wyników.
- **Framework AI**: Użyto TensorFlow do trenowania modelu.

## Testowanie

### Implementacja testów jednostkowych

Testy jednostkowe zostały zaimplementowane w pliku `test_model.py` przy użyciu frameworka `unittest`.

### Wyniki testów
Ran 2 tests in 0.237s

OK

## Ewentualne poprawki
 ### Na obecnym etapie nie wykryto żadnych błędów w implementacji testowanej funkcjonalności. Kod działa zgodnie z oczekiwaniami. Dalsze usprawnienia mogą obejmować:

- **Rozszerzenie testów jednostkowych o dodatkowe scenariusze testowe.**
- **Optymalizację procesu trenowania modelu.**
- **Oparcie modelu AI na prawdziwych danych**
### Wnioski
Projekt został zrealizowany zgodnie z założeniami. Udało się zaimplementować model regresji liniowej, przetestować go i zwizualizować wyniki. 
Dalsze prace mogą skupić się na rozszerzeniu funkcjonalności oraz optymalizacji kodu.

