from colorama import Fore, Style
import json
import os

def start_window():

    editor_text = Fore.YELLOW + "Genetic Editor\n------------------------------\n" + Style.RESET_ALL + "-am - add morphogen\n-aa - add action\n-ai - add information\n-c - compile and send genetic code\n-i - information\n-e - exit\n"
    mgs = []
    act = []
    inf = []


    print(editor_text)

    while True:
        cmd = input("User: > ")

        if cmd == "-am":
            morphogen = add_morphogen()
            mgs.append(morphogen)
        elif cmd == "-aa":
            action = add_action()
            act.append(action)
        elif cmd == "-ai":
            information = add_information()
            inf.append(information)
        elif cmd == "-i":
            pass
        elif cmd == "-c":
            genetic_code = {
                "mgs": mgs,
                "act": act,
                "inf": inf,
                "c": 1
            }

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "genetic_code_raw.json")

            with open(file_path, "w") as file:
                json.dump(genetic_code, file, indent=4)

        elif cmd == "-e":
            break
        else:
            print(f"Unknown command: {cmd}")

    return 0


def add_morphogen():
    
    name = input("Enter name: ")
    distribution = input("Enter distribution: ")
    condition = input("Enter condition: ")
    action = input("Enter action name: ")

    return [name, distribution, condition, action]

def add_action():
    name = input("Enter name: ")
    action = input("Enter action: ")
    timer = input("Enter timer: ")
    return [name, action, timer]

def add_information():
    name = input("Enter name: ")
    itype = input("Enter type: ")
    if itype == "c":
        species = input("Enter species: ")
        return [name, itype, species]


    return [name, itype]
    

if __name__ == "__main__":
    start_window()