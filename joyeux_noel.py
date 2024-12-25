import time
import os
from colorama import Fore, Style, init # type: ignore

# Initialiser Colorama
init(autoreset=True)

def clear_screen():
    """Nettoie l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree_with_delay(levels, delay=0.3):
    """Affiche un arbre de Noël avec un effet déroulant."""
    decorations = [Fore.RED + 'O', Fore.YELLOW + '*', Fore.GREEN + '@', Fore.CYAN + '#', Fore.MAGENTA + '&']
    trunk = Fore.WHITE + "|||"

    for i in range(levels):
        line = " " * (levels - i - 1)
        for j in range(2 * i + 1):
            if (i + j) % 2 == 0:
                line += decorations[(i + j) % len(decorations)]
            else:
                line += Fore.GREEN + "*"
        print(line)
        time.sleep(delay)  # Pause pour l'effet déroulant
    print(" " * (levels - 2) + trunk)

def animate_tree():
    """Anime l'arbre de Noël avec des couleurs et un message festif."""
    levels = 10  # Nombre de niveaux de l'arbre
    while True:
        clear_screen()
        print(Fore.YELLOW + Style.BRIGHT + "✨🎄 Joyeux Noël à tous ! 🎅✨\n")
        print_tree_with_delay(levels, delay=0.2)
        print("\n" + Fore.CYAN + Style.BRIGHT + "🎁 Que la magie de Noël illumine vos cœurs ! 🎁")
        time.sleep(2)  # Pause avant de redémarrer l'animation

if __name__ == "__main__":
    animate_tree()
