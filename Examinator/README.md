# EXAMINATOR
*projektové zadání*


## 1. Cíl projektu a omezení

Vytvořte **terminálovou aplikaci v Pythonu**, která simuluje písemné zkoušení pomocí testových otázek z textových souborů.

**Základní omezení pro tuto verzi zadání:**
- Nepoužívejte OOP (žádné vlastní třídy a instance).  
- Aplikace běží v terminálu / konzoli.  
- Aplikace pracuje pouze s lokálními soubory (žádné API, databáze apod.).  


## 2. Průběh práce s aplikací

Aplikace se po spuštění chová následovně:  

1. Načte všechny soubory s otázkami z podadresáře `Testy_zdroj_otazek`.  
2. Zkontroluje, že existuje alespoň minimální požadovaný počet otázek (viz níže), jinak test nepovolí spustit.  
3. Vyzve uživatele k zadání:  
   - jména a příjmení zkoušeného,  
   - počtu otázek pro aktuální test (např. 5, 10, 15…).  
4. Z dostupných otázek náhodně vybere zadaný počet a:  
   - náhodně **zamíchá jejich pořadí**,  
   - u každé otázky také náhodně **zamíchá pořadí odpovědí**.  
5. Každá otázka se zobrazí **postupně, po jedné**:  
   - před zobrazením nové otázky aplikace **vyčistí terminál**, aby nebylo nutné scrollovat (např. volání systémového příkazu podle OS),  
   - zobrazí text otázky, odpovědi (označené písmeny A, B, C, D) a informaci o autorovi a názvu souboru, ze kterého otázka pochází.  
6. Uživatel vybírá odpověď zadáním písmene (`A`, `B`, `C`, `D`), aplikace:  
   - kontroluje validitu vstupu (opakované dotazování, dokud není zadán platný znak),  
   - vyhodnotí, zda je odpověď správná.  
7. Po zodpovězení všech otázek aplikace:  
   - spočítá počet správných a chybných odpovědí,  
   - vypočítá procentní úspěšnost,  
   - určí známku podle definované stupnice.  
8. Výsledek uloží do souboru v podadresáři `Vysledky_testu` (viz přesná specifikace níže) a zároveň přehledně zobrazí v terminálu.  
9. Aplikace nabídne možnost:  
   - spustit **nový test** se stejným studentem,  
   - spustit **nový test s jiným studentem**,  
   - nebo **aplikaci ukončit**.  



## 3. Známkování a výsledky

### 3.1 Stupnice známek

Výchozí stupnice (hranice lze změnit pomocí konstant na jednom místě v kódu):  

- 1: (100; 90) %  
- 2: ⟨90; 75) %  
- 3: ⟨75; 60) %  
- 4: ⟨60; 45) %  
- 5: ⟨45; 0) %  


V kódu definujte např. slovník nebo seznam hranic na jednom místě, abyste mohli stupnici snadno změnit (např. pro jiný předmět).  

### 3.2 Soubor s výsledkem testu

Výsledek se vždy uloží do podadresáře `Vysledky_testu`.  

#### Název souboru

Formát názvu:  

`prijmeni_jmeno_YYYYMMDD_HHMMSS_pocetOtazek_znamka.txt`  

Příklad:  

`valek_vladislav_20241006_132845_10_2.txt`  

- `prijmeni` – vše malými písmeny, bez diakritiky, mezery nahrazené podtržítkem (doporučeno sjednotit v kódu).  
- `jmeno` – totéž.  
- `YYYYMMDD` – datum vyhodnocení (rok, měsíc, den),  
- `HHMMSS` – čas vyhodnocení (hodina, minuta, sekunda),  
- `pocetOtazek` – celý počet otázek v testu,  
- `znamka` – výsledná známka 1–5.  

#### Obsah souboru

Uvnitř souboru bude struktura přesně v následujícím tvaru (text lze lokalizovat, ale **pořadí a význam řádků musí zůstat**):  

**Ukázkový soubor** `valek_vladislav_20241006_132845_10_2.txt`:  

```text
Vypracoval/a: Vladislav Válek
Otázek v testu: 10
Výsledná známka: 2
Procentní úspěšnost: 80 %
Stupnice: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>
Datum a čas vyhodnocení: 6.10.2024, 13:25:45

----------------------
Chybně zodpovězeno:

Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
definice funkce my_function(): 
function my_function() {} 
def my_function(): 
fun my_function():

Otázka: Který z následujících příkazů vytvoří řetězec v Pythonu? 
'Hello, World!' 
Hello, World! 
12345 
["Hello", "World"]
----------------------
```

**Požadavky:**
- V části „Chybně zodpovězeno:“ uveďte **přesný text otázky a všechny čtyři odpovědi** v pořadí, v jakém byly studentovi zobrazeny.  
- Není nutné v tomto základním zadání označovat, která byla správná / vybraná; to je možné přidat v rozšíření.  

***

## 4. Formát souborů s otázkami

### 4.1 Umístění a pojmenování

- Všechny soubory s otázkami budou uloženy v podadresáři `Testy_zdroj_otazek`.  
- Název souboru s otázkami má tvar:  

  `prijmeni_jmeno_otazky_libovolne_pojmenovani_dle_tematu_otazek.txt`  

  Příklad:  

  `valek_vladislav_otazky_funkce_bloky_list.txt`  

- V projektu musí být alespoň **15 platných otázek celkem**, rozdělených alespoň do **dvou souborů**. Tím se ověří načítání otázek z více souborů.

### 4.2 Struktura souboru

Každý soubor MUSÍ přesně dodržovat následující strukturu:  

1. **První řádek**: autor otázek, ve formátu:  
   ```text
   Autor: Vladislav Válek
   ```  
2. Následují prázdné řádky podle vzoru (doporučeno alespoň jeden prázdný řádek).  
3. Každé zadání otázky:  
   - Před každou otázkou jsou **2 prázdné řádky**.  
   - Řádek s textem začíná přesně:  
     ```text
     Otázka: <text otázky>
     ```  
4. Za každou otázkou následují přesně **4 řádky odpovědí**, každý ve formátu:  
   ```text
   X; text odpovědi
   ```  
   kde `X` je:  
   - `0` – odpověď je **špatně**,  
   - `1` – odpověď je **správně**.  
5. V každé otázce je **přesně jedna** odpověď se značkou `1;` (správná), ostatní tři mají `0;`.  
6. V souboru nesmí být jiné textové řádky než:  
   - řádek s autorem,  
   - prázdné řádky,  
   - řádky s „Otázka: …“,  
   - řádky s odpověďmi `0;` / `1;`.  

### 4.3 Ukázkový soubor s otázkami

Soubor `valek_vladislav_otazky_funkce_bloky_list.txt`:

```text
Autor: Vladislav Válek


Otázka: Jakým způsobem se v Pythonu odliší blok řádků kódu, který patří k jedné funkci?
0; Blok je uzavřen do trojitých uvozovek.
0; Každý řádek začíná otazníkem.
1; Všechny řádky jsou odsazeny ideálně o 4 mezery.
0; Celý blok je uzavřen do složených závorek.


Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
0; definice funkce my_function(): 
0; function my_function() {} 
1; def my_function(): 
0; fun my_function():


Otázka: Jakým způsobem definujeme seznam v Pythonu? 
1; Použitím hranatých závorek: [1, 2, 3] 
0; Použitím kulatých závorek: (1, 2, 3) 
0; Použitím složených závorek: {1, 2, 3} 
0; Pomocí příkazu create list
```

Aplikace musí:  
- načíst jméno autora z prvního řádku a u každé otázky jej umět zobrazit,  
- znát i název souboru (např. `valek_vladislav_otazky_funkce_bloky_list.txt`) a u každé otázky jej zobrazit.  

***

## 5. Validace vstupů a robustnost

Aplikace musí kontrolovat zejména:  

- **Adresáře** `Testy_zdroj_otazek` a `Vysledky_testu`:
  - adresář `Testy_zdroj_otazek` musí být součástí projektu a obsahovat soubory s otázkami; pokud chybí, aplikace oznámí chybu a ukončí se,
  - adresář `Vysledky_testu` aplikace automaticky vytvoří, pokud ještě neexistuje.
- **Existenci a čitelnost souborů s otázkami**:  
  - pokud v adresáři nejsou žádné validní soubory s otázkami, aplikace informuje uživatele a test nespustí.  
- **Správný formát souborů**:  
  - prázdné řádky navíc a řádky obsahující pouze mezery se ignorují,
  - otázka musí mít přesně 4 odpovědi a právě jednu správnou odpověď označenou `1;`,
  - pokud je otázka chybná (např. nemá 4 odpovědi nebo právě jednu správnou), aplikace ji přeskočí, vypíše varování a pokračuje dalšími otázkami,
  - pokud soubor nelze přečíst nebo v něm chybí první řádek s autorem, aplikace přeskočí celý soubor a vypíše varování,
  - pokud po načtení nezůstane alespoň 15 platných otázek, aplikace test nespustí a informuje uživatele.
- **Počet otázek v testu**:  
  - zadávaný počet otázek v testu musí být kladné celé číslo a nesmí přesáhnout celkový počet dostupných otázek,  
  - při neplatném vstupu se uživatel znovu dotazuje.  
- **Vstupy uživatele během testu**:  
  - zadání odpovědi `A`, `B`, `C`, `D` (nezávisle na velikosti písmen),  
  - při zadání jiného znaku je uživatel znovu vyzván.  

***

## 6. Zobrazení jedné otázky – konkrétní příklad

Příklad obrazovky pro jednu otázku po zamíchání odpovědí:

```text
Student: Vladislav Válek
Otázka 3 / 10
Autor: Vladislav Válek
Soubor: valek_vladislav_otazky_funkce_bloky_list.txt

Otázka: Jakým způsobem definujeme seznam v Pythonu?

A) Použitím složených závorek: {1, 2, 3}
B) Použitím kulatých závorek: (1, 2, 3)
C) Pomocí příkazu create list
D) Použitím hranatých závorek: [1, 2, 3]

Zadej svou odpověď (A, B, C, D): 
```

Po potvrzení odpovědi může aplikace volitelně zobrazit krátkou zpětnou vazbu (např. „Správně!“ / „Chybně.“), nebo jít rovnou na další vyčištěnou obrazovku.  

***

## 7. Návrhy na rozšíření

- Ošetření krizových situací ještě důkladněji:  
  - neexistující soubory, poškozené soubory, prázdné řádky navíc, různé počty odpovědí, více správných odpovědí apod.  

- Otázky typu **ano/ne** (pouze 2 varianty, např. „1; Ano“, „0; Ne“).  

- Otázky s **různým počtem odpovědí** (např. 3, 5 variant).  

- **Více správných odpovědí**:  
  - systém hodnocení: za každou správně zatrženou odpověď část bodu, za zatržení špatné odpovědi 0 bodů.  

- „**God mode**“ – speciální režim pro autora testu, ve kterém se zobrazí označení správných odpovědí (např. pro ladění).  

- Podpora vstupu z **JSON** souborů místo/vedle textových.  

- U každé otázky parametr `difficulty`, který se dynamicky upravuje podle úspěšnosti studenta; možnost generovat testy s danou náročností (např. „lehké“, „střední“, „těžké“).  

***

## 8. Technické požadavky kódování

- Nepoužívat vlastní třídy (OOP), vše řešit pomocí funkcí a základních datových struktur (seznamy, slovníky, n-tice).  
- Vyčlenit konfiguraci (např. hranice na známky, cesty k adresářům) na jedno místo v souboru jako **konstanty** nebo **nastaveni**.  

- Kód musí být přehledně strukturovaný do funkcí (např. `load_questions`, `run_test`, `evaluate_result`, `save_result_file`, `clear_screen`, `get_user_answer` atd.).  


## Startovní soubor

V balíčku je záměrně nedokončený soubor `Examinator_app_empty.py`. Studenti v něm vytvoří aplikaci podle tohoto zadání; hotové soubory `examinator.py` ani `test_examinator.py` součástí balíčku nejsou.

Po dokončení lze aplikaci spustit příkazem:

```text
python Examinator_app_empty.py
```
