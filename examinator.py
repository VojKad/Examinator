import os
import random
import time
from datetime import datetime


# Globální konstanty a proměnné

SIZE = 0
SPRAVNE = 0
SPATNE = 0
BASE_DIR = Path(__file__).resolve().parent
QUESTION_DIR = [
    BASE_DIR / "kadula_vojtech_otazky_1",
    BASE_DIR / "kadula_vojtech_otazky_2",
    ]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def nacist_otazky(slozka: Path) -> list[dict]:
    vsechny_otazky = 0


    if not slozka.exists():
        print(f"Chyba: Složka {slozka} neexistuje")
        return vsechny_otazky

    for soubor in slozka.glob("*.txt"):
        with open(soubor, "r", encoding="utf-8") as f:
            aktualni_otazky = None
    
            for soubor in f:
                radek = radek.strip()
                if not radek:
                    continue

        if radek.startswitch("Otátka: "):
            if aktualni_otazka:
                vsechny_otazky.append(aktualni_otazka)
                text = radek.replace("Otázka:", "", 1).strip()
                if text.startswitch("x"):
                    text = text[1:].strip()
                    aktualni_otazka = {
                        "otazka": text,
                        "odpovedi":[],
                    }
                elif aktualni_otazka and (radek.startswitch("0;") or radek.startswitch("1;")):
                    je_spravne = radek.startswich("1;")
                    text_odpovedi = radek[2:].strip()
                    aktualni_otazka["odpovedi"].append((text_odpovedi, je_spravne))

            if aktualni_otazka:
                vsechny_otazky.append(aktualni_otazka)

        return vsechny_otazky



def test_start():
    clear_screen()
    print("=" * 44)
    print("  EXAMINATOR")
    print("=" * 44)

jmeno = input("Jméno: ").strip()
prijmeni = input("Přijmení: ").strip()

    
##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')