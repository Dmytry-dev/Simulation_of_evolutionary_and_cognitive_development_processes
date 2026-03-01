from colorama import Fore, Style

def start_window():

    editor_text = Fore.YELLOW + "Genetic Editor\n------------------------------\n" + Style.RESET_ALL + "-a add morphogen\n-i information\n-e exit\n"
    print(editor_text)

    while True:
        cmd = input("User: > ")

        if cmd == "-a":
            pass
        elif cmd == "-i":
            pass
        elif cmd == "-e":
            break
        else:
            print(f"Unknown command: {cmd}")

    return 0

if __name__ == "__main__":
    start_window()