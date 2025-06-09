import os
import json
import time
from colorama import Fore, init, Style
from kasyno.roulette import play_roulette  # noqa: F401
from kasyno.Slots import play_slots       # noqa: F401

init()
#welcome screen
def spacje():
    for i in range(25):
        print(" ")
welcome = """
██╗  ██╗  █████╗  ███████╗ ██╗   ██╗ ███╗   ██╗  ██████╗ 
██║ ██╔╝ ██╔══██╗ ██╔════╝ ╚██╗ ██╔╝ ████╗  ██║ ██╔═══██╗
█████╔╝  ███████║ ███████╗  ╚████╔╝  ██╔██╗ ██║ ██║   ██║
██╔═██╗  ██╔══██║ ╚════██║   ╚██╔╝   ██║╚██╗██║ ██║   ██║
██║  ██╗ ██║  ██║ ███████║    ██║    ██║ ╚████║ ╚██████╔╝
╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚══════╝    ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ 
Autor: Gregoo756
"""

#System kasy
if os.path.exists("kasa.json"):
    with open("kasa.json", "r") as file:
        data = json.load(file)
        kasa = data["kasa"]
else:
    kasa = 1000



def welcome_screen():
    print(Fore.GREEN + welcome + Style.RESET_ALL)
    print(Fore.CYAN + "1. Roulette\n2. BlackJack (not added yet)\n3. Slots\n4.Wychodzenie")
    time.sleep(1)
    choice_input = input(f"Wybierz w co chcesz zagrać, masz {kasa}zł. (1–4): " + Style.RESET_ALL)
    if not choice_input.isdigit():
        print("Niepoprawny wybór.")

    if choice_input == "1":
        play_roulette() #Roulette

    elif choice_input == "2":
        print("this is gonna be added later") #Blackjack

    elif choice_input == "3":
        play_slots() #Slots

    elif choice_input == "4":
        print(Fore.RED + f"Wychdzenie", end="") #Exit
        time.sleep(0.2)
        print(f".", end="")
        time.sleep(0.2)
        print(f".", end="")
        time.sleep(0.3)
        print(f".", end="" + Style.RESET_ALL)
        time.sleep(0.2)
        exit()
    else:
        print("Niepoprawny wybór")


while True:
    spacje()
    welcome_screen()
    if kasa <= 0:
        print("Zbankrutowałeś/aś")
        break