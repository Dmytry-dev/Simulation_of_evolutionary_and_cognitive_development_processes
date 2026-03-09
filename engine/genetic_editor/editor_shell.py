#Dmytry-dev
#Editor chell
#28.02.2026

from colorama import Fore, Style
from multiprocessing.connection import Client
import sys, select, time





def open_editor():

    editor_text = Fore.YELLOW + "======================\nGENETIC EDITOR\n======================\n" + Style.RESET_ALL
    flags = []

    conn_editor = Client(("localhost", 6000))

    conn_editor.send(1)

    print(editor_text)


    while True:
        # Messages
        if conn_editor and conn_editor.poll():
            msg = conn_editor.recv()
            if msg == 1:
                print("[MENU] connected\n")
            if msg == "-e":
                break
            print("User: >", end=" ", flush=True)

        # Inputs and processing
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                print("User: >", end=" ", flush=True)
                continue

            for f in cmd:
                if f.startswith("-"):
                    for ch in f[1:]:
                        flags.append(ch)
            
            # Execution of the request
            for i in range(len(flags)):

                # Add parts of gen
                if flags[0] == "a":

                    if flags[i] == "m":
                        mgs = add_morphogen()
                    elif flags[i] == "a":
                        act = add_action()
                    elif flags[i] == "i":
                        inf = add_information()

                # Genetic compilation
                if flags[0] == "c":
                    compilation(conn_editor)

                if flags[0] == 'e':
                    return 0
            
            flags.clear()
            print("User: >", end=" ", flush=True)
        time.sleep(0.1)



                
                



def add_morphogen():
    Name = input("Enter name: ") # Text
    Distribution = input("Enter distribution: ") # 1 2 3 4 5 6
    Condition = input("Enter condition: ") # < S1 S2

    Action = input("Enter action: ")

    return [Name, Distribution, Condition, Action]

def add_action():
    Name = input("Enter name: ") # Text
    Action = input("Enter action: ") # Action [Information]
    Timer = input("Enter timer: ") # 0 - 5

    return [Name, Action, Timer]


def add_information():
    Name = input("Enter name: ") # Text

    return [Name]

def compilation(conn_editor):
    conn_editor.send("-c")
    
    return 0


if __name__ == "__main__":
    open_editor()

