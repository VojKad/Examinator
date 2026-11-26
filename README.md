# Terminálová testovací aplikace (Python)

Jednoduchá konzolová aplikace v Pythonu pro spouštění znalostních testů z textových souborů. Projekt je postaven procedurálně (bez OOP – využívá funkce, seznamy a slovníky) a je navržen pro přehlednou práci v terminálu bez nutnosti scrollování.

## Hlavní funkce

* **Načítání otázek z definovaného adresáře:** Automaticky projde všechny `.txt` soubory ve zvolených složkách a spojí je do jedné společné banky otázek.

* **Evidence zkoušeného:** Před spuštěním testu vyžádá jméno a příjmení zkoušeného.

* **Vlastní délka testu:** Uživatel si zvolí počet otázek pro aktuální běh (s kontrolou platného rozsahu).

* **Náhodný výběr a zamíchání:** Otázky jsou vybrány náhodně (`random.sample`) a pořadí nabízených odpovědí se u každé otázky míchá (`random.shuffle`).

* **Čisté terminálové zobrazení:** Před každou otázkou se obrazovka terminálu vymaže (`cls` / `clear`), aby nebylo nutné posouvat okno.

* **Okamžité i celkové vyhodnocení:** Průběžné vyhodnocení jednotlivých odpovědí a závěrečné shrnutí výsledku.

## Struktura projektu

```
PythonWork2028_01/
├── test_app.py                  # Hlavní spustitelný skript aplikace
├── README.md                    # Dokumentace projektu
├── kadula_vojtech_otazky_1/     # Složka se soubory otázek (.txt)
│   └── otazky_zaklady.txt
└── kadula_vojtech_otazky_2/     # Další složka se soubory otázek (.txt)
    └── otazky_pokrocile.txt

```

## Formát souborů s otázkami

Otázky jsou uloženy v souborech `.txt` v kódování **UTF-8**. Každá otázka začíná klíčovým slovem `Otázka: x` a následují jednotlivé možnosti označené prefixem `1;` (správná odpověď) nebo `0;` (nesprávná odpověď).

### Příklad zápisu v `.txt`:

```
Otázka: xKterá z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu?
0; definice funkce my_function():
0; function my_function() {}
1; def my_function():
0; fun my_function():

Otázka: xJaký režim otevření souboru přidá nový řádek na konec existujícího souboru bez smazání obsahu?
0; Režim "w"
1; Režim "a"
0; Režim "r"
0; Režim "x"

```

## Požadavky a spuštění

* **Python 3.10+** (využívá pouze standardní knihovnu: `os`, `random`, `pathlib`)

* Žádné externí balíčky nejsou potřeba.

### Spuštění v terminálu (CMD / PowerShell / Bash):

1. Přejdi do složky se skriptem:

   ```
   cd cesta/k/projektu
   
   ```

2. Spusť aplikaci:

   ```
   python examinator.py
   
   ```

3. Zadej jméno, příjmení, počet otázek a odpovídej zadáním čísla zvolené možnosti.