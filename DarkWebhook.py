import os
import sys
import time
import http.client
import json
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    loading_message = "Chargement"
    for _ in range(3):
        sys.stdout.write(f"\r{loading_message}...")
        sys.stdout.flush()
        time.sleep(0.5)
        loading_message += "."
    sys.stdout.write("\rChargement Terminé!\n")
    time.sleep(1)

def ascii_art():
    blue = '\033[94m'
    reset = '\033[0m'
    art = f"""
{blue}
        ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
        ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
        ██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
        ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
        ██████╔╝██║  ██║██║  ██║██║  ██╗    ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝By N4S

         [1] WebhookSpammer
{reset}
    """
    print(art)

def webhook_spammer():
    clear_screen()
    webhook_url = input("Entrez l'URL du webhook: ")
    message = input("Entrez le message à spammer: ")
    num_spams = int(input("Entrez le nombre de spams: "))
    delay = int(input("Entrez le délai entre les spams en secondes (par défaut 1): ") or 1)

    for _ in range(num_spams):
        try:
            conn = http.client.HTTPSConnection("discord.com")
            payload = json.dumps({"content": message})
            conn.request("POST", webhook_url, payload, {"Content-Type": "application/json"})
            response = conn.getresponse()
            print(f"[+] Message envoyé: {message}")
        except Exception as e:
            print(f"Erreur: {e}")

        time.sleep(delay)

    input("Appuyez sur Entrée pour revenir au menu principal...")

def main_menu():
    clear_screen()
    ascii_art()
    while True:
        choice = input('[User: DarkUser]_______[Main: Menu]: ')
        if choice == "1":
            webhook_spammer()
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    loading_animation()
    main_menu()