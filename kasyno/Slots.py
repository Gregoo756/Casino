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
slots_hello = """
███████╗██╗      ██████╗ ████████╗███████╗
██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔════╝
███████╗██║     ██║   ██║   ██║   ███████╗
╚════██║██║     ██║   ██║   ██║   ╚════██║
███████║███████╗╚██████╔╝   ██║   ███████║
╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ 
"""

# System kasy i zapisywanie w JSON'ie
if os.path.exists("kasa.json"):
    with open("kasa.json", "r") as file:
        data = json.load(file)
        kasa = data.get("kasa", 1000)
else:
    kasa = 1000  #default balance

def print_row(row):
    print(Fore.YELLOW + "=============" + Style.RESET_ALL)
    print(Fore.YELLOW + " | ".join(row) + Style.RESET_ALL)
    print(Fore.YELLOW + "=============" + Style.RESET_ALL)

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def get_payout(row, bet): #Jeśli wylosują się 3 takie same symbole to jest payout
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def stawka():
    global kasa
    while True:
        try:
            kwota = int(input(f"\nMasz {kasa} zł. Ile chcesz postawić?: "))
            if kwota > kasa:
                print(Fore.RED + "Nie masz tyle kasy, spróbuj ponownie." + Style.RESET_ALL)
            elif kwota <= 0:
                print(Fore.RED + "Wprowadź kwotę większą niż 0." + Style.RESET_ALL)
            else:
                kasa -= kwota
                return kwota
        except ValueError:
            print(Fore.RED + "Wpisz poprawną liczbę." + Style.RESET_ALL)

def play_slots(): #main
    global kasa
    spacje()
    print(Fore.GREEN + slots_hello + Style.RESET_ALL)

    #Exit jeśli skończy się kasa exit
    if kasa <= 0:
        print(Fore.RED + "Nie masz już żadnej kasy. Koniec." + Style.RESET_ALL)
        return

    while kasa > 0:
        # bet
        bet = stawka()

        # Spin the reels
        print("\n" + Fore.CYAN + "Kręcęnie..." + Style.RESET_ALL)
        time.sleep(1)
        row = spin_row()
        print_row(row)

        # Determine payout
        payout = get_payout(row, bet)
        if payout > 0:
            kasa += payout
            print(Fore.GREEN + f"Wygrałeś {payout} zł!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Przegrałeś tę rundę." + Style.RESET_ALL)

        print(Fore.CYAN + f"Aktualny stan konta: {kasa} zł" + Style.RESET_ALL)

        ponownie = input("\nChcesz zagrać jeszcze raz? (t/n): ").lower()
        if ponownie != 't':
            zapytaj = input(Fore.YELLOW +  "Chcesz wrócić do menu głównego? (t/n): " + Style.RESET_ALL).lower()
            if zapytaj == 't':
                break  # powrót do main.py
            else:
                print(Fore.RED + "Koniec gry." + Style.RESET_ALL)
                exit()


    if kasa <= 0:
        print(Fore.RED + "Zbankrutowałeś/aś." + Style.RESET_ALL)

    with open("kasa.json", "w") as file:
        json.dump({"kasa": kasa}, file)