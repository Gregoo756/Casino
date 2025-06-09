import random
import time
import json
import os
from colorama import Fore, init, Style

init()

# Uwaga to jest tylko backend pod maina

def spacje():             # Żeby był odstęp między grami
    for i in range(20):
        print("\n")
hello = """
  ██████╗   ██████╗  ██╗   ██╗ ██╗      ███████╗ ████████╗ ████████╗ ███████╗
  ██╔══██╗ ██╔═══██╗ ██║   ██║ ██║      ██╔════╝ ╚══██╔══╝ ╚══██╔══╝ ██╔════╝
  ██████╔╝ ██║   ██║ ██║   ██║ ██║      █████╗      ██║       ██║    █████╗  
  ██╔══██╗ ██║   ██║ ██║   ██║ ██║      ██╔══╝      ██║       ██║    ██╔══╝  
  ██║  ██║ ╚██████╔╝ ╚██████╔╝ ███████╗ ███████╗    ██║       ██║    ███████╗
"""


# typy zakładów #Dodaj klasy (roulette-classes.py), prace jako opcja 5 exit jako 4
roulette_black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
roulette_red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
roulette_green = [0]
high_numbers = list(range(18, 37))
low_numbers = list(range(1, 19))
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]


# System kasy i zapisywanie w JSON'ie
if os.path.exists("kasa.json"):             #Jak jest taki folder jak kasa.json to go otwiera jak nie to przyjmuje 1000
    with open("kasa.json", "r") as file:
        data = json.load(file)
        kasa = data["kasa"]
else:
    kasa = 1000  # Deafult kasy

#Bet na miejsce
def bety():
    print(Fore.CYAN + "Wybierz swój zakład:")
    print("1: Black \n2: Red \n3: Green \n4: 18–36 \n5: 1–18 \n6: Even \n7: Odd")
    time.sleep(1.5)

#Postawienie
def stawka():
    global kasa
    while True:
        try:
            kwota = int(input(f"\nMasz {kasa} zł. Ile chcesz postawić?: "))
            if kwota > kasa:
                print("Nie masz tyle kasy, spróbuj ponownie.")
            elif kwota <= 0:
                print("Wprowadź kwotę większą niż 0.")
            else:
                kasa -= kwota
                return kwota
        except ValueError:
            print("Wpisz poprawną liczbę.")

def gra(kwota):
    global kasa
    bety()
    choice_input = input(Fore.CYAN + "Wybierz na co chcesz postawić (1–7): ")
    if not choice_input.isdigit():
        print("Niepoprawny wybór.")
        return

    choice = int(choice_input)
    wybrany = random.choice(list(range(37)))
    print(f"Wylosowana liczba to: {wybrany}")

    if choice == 1:
        print("Wybrałeś: Black")
        if wybrany in roulette_black:
            kasa += kwota * 2
            print("Numer jest czarny. Wygrałeś!")
        else:
            print("Przegrałeś")

    elif choice == 2:
        print("Wybrałeś: Red")
        if wybrany in roulette_red:
            kasa += kwota * 2
            print("Numer jest czerwony. Wygrałeś!")
        else:
            print("Przegrałeś")

    elif choice == 3:
        print("Wybrałeś: Green")
        if wybrany in roulette_green:
            kasa += kwota * 36
            print("Numer jest zielony. GRUBA WYGRANA!")
        else:
            print("Przegrałeś")

    elif choice == 4:
        print("Wybrałeś: 18–36")
        if wybrany in high_numbers:
            kasa += kwota * 2
            print("Numer jest wysoki. Wygrałeś!")
        else:
            print("Przegrałeś")

    elif choice == 5:
        print("Wybrałeś: 1–18")
        if wybrany in low_numbers:
            kasa += kwota * 2
            print("Numer jest niski. Wygrałeś!")
        else:
            print("Przegrałeś")

    elif choice == 6:
        print("Wybrałeś: Even")
        if wybrany in even_numbers:
            kasa += kwota * 2
            print("Numer jest parzysty. Wygrałeś!")
        else:
            print("Przegrałeś")

    elif choice == 7:
        print("Wybrałeś: Odd")
        if wybrany in odd_numbers:
            kasa += kwota * 2
            print("Numer jest nieparzysty. Wygrałeś!")
        else:
            print("Przegrałeś")
    else:
        print("Niepoprawny wybór.")

# Pętla
def play_roulette():
    global kasa
    spacje()
    print(Fore.RED + hello + Style.RESET_ALL)
    while kasa > 0:
        kwota = stawka()
        gra(kwota)
        print(f"Aktualny stan konta: {kasa} zł")
        ponownie = input(Fore.YELLOW + "Chcesz zagrać ponownie? (t/n): ").lower()
        if ponownie != 't':
            zapytaj = input("Chcesz wrócić do menu głównego? (t/n): " + Style.RESET_ALL).lower()
            if zapytaj == 't':
                return  # powrót do main.py
            else:
                print(Fore.RED + "Koniec gry." + Style.RESET_ALL)
                exit()
    if kasa <= 0:
        print(Fore.RED + "Zbankrutowałeś/aś." + Style.RESET_ALL)

    with open("kasa.json", "w") as file:
        json.dump({"kasa": kasa}, file)







