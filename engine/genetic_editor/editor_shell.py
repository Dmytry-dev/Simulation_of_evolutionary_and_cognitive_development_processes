from colorama import Fore, Style

def start_window():

    editor_text = Fore.YELLOW + "Genetic Editor\n------------------------------\n" + Style.RESET_ALL + "-am - add morphogen\n-aa - add action\n-ai - add information\n-c - compile and send genetic code\n-i - information\n-e - exit\n"
    genetic_code = []

    print(editor_text)

    while True:
        cmd = input("User: > ")

        if cmd == "-am":
            morphogen = add_morphogen()
            genetic_code.append(morphogen)
        elif cmd == "-aa":
            action = add_action()
            genetic_code.append(action)
        elif cmd == "-i":
            information = add_information()
            genetic_code.append(information)
        elif cmd == "-c":
            pass
        elif cmd == "-e":
            break
        else:
            print(f"Unknown command: {cmd}")

    return 0

def add_morphogen():
    
    name = input("Enter name: ")
    distribution = input("Enter distribution: ")
    condition = input("Enter condition: ")
    timer = input("Enter timer: ")
    action = input("Enter action name: ")

    return ["M", name, distribution, condition, timer, action]

def add_action():
    name = input("Enter name: ")
    action = input("Enter action: ")

    return ["A", name, action]

def add_information():
    name = input("Enter name: ")
    return ["I", name]
    

if __name__ == "__main__":
    start_window()