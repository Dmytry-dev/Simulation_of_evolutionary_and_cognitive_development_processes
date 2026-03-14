#Dmytry-dev
#Editor chell
#28.02.2026

from colorama import Fore, Style
from multiprocessing.connection import Client
from engine.structures.Gen import DNA
import sys, select, time





def open_editor():

    editor_text = Fore.YELLOW + "======================\nGENETIC EDITOR\n======================\n" + Style.RESET_ALL
    flags = []

    conn_editor = Client(("localhost", 6000))

    mgs = []
    act = []
    inf = []


    print(editor_text)


    while True:
        # Messages
        if conn_editor and conn_editor.poll():
            msg = conn_editor.recv()
            if isinstance(msg, DNA):
                DNA_print(msg)

            if msg == "-e":
                break

        # Inputs and processing
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                continue

            for f in cmd:
                if f.startswith("-"):
                    for ch in f[1:]:
                        flags.append(ch)
            
            # Execution of the request
            for i in range(1, len(flags)):

                # Add parts of gen
                if flags[0] == "a":

                    if flags[i] == "m":
                        mgs.append(add_morphogen())
                    elif flags[i] == "a":
                        act.append(add_action())
                    elif flags[i] == "i":
                        inf.append(add_information())

                # Genetic compilation
                if flags[1] == "c":
                    compilation(conn_editor, mgs, act, inf)

                if flags[1] == 'e':
                    return 0
                print(flags)
            
            flags.clear()
        time.sleep(0.1)



                
                



def add_morphogen():
    print(Fore.RED + "MORPHOGEN"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text
    Distribution = input("Enter distribution: ") # 1 2 3 4 5 6
    Condition = input("Enter condition: ") # < S1 S2
    Action = input("Enter action: ")

    return [Name, Distribution, Condition, Action]

def add_action():
    print(Fore.RED+"ACTION"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text
    Action = input("Enter action: ") # Action [Information]
    Timer = input("Enter timer: ") # 0 - 5

    return [Name, Action, Timer]


def add_information():
    print(Fore.RED+"INFORMATION"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text

    return [Name]

def compilation(conn_editor, mgs, act, inf):
    msg = {
        "flag": "-c",
        "mgs": mgs,
        "act": act,
        "inf": inf
    }

    conn_editor.send(msg)

    dna = conn_editor.recv()
    DNA_print(dna)
    
    return 0

def DNA_print(DNA_chain):
    Mg = DNA_chain.Mg
    Ac = DNA_chain.Ac
    inf = DNA_chain.Inf

    DNA_text = []

    for i in range(len(Mg)):
        temp = Mg[i].A
        DNA_text.append(f"{Fore.RED}[{Mg[i].M_name}{Style.RESET_ALL} -> {Fore.YELLOW}{temp.A_name}{Fore.RED}]{Style.RESET_ALL}")

    for i in range(len(Ac)):
        DNA_text.append(f"{Fore.YELLOW}[{Ac[i].A_name}{Style.RESET_ALL} ->{Fore.GREEN} {Ac[i].A}{Fore.YELLOW}]{Style.RESET_ALL}")

    for i in range(len(inf)):
        DNA_text.append(f"[{inf[i].N}]")

    for i in range(len(DNA_text)):
        print(DNA_text[i], end=" ")



if __name__ == "__main__":
    open_editor()

