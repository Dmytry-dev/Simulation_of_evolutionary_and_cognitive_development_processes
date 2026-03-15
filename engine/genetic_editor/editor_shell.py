#Dmytry-dev
#Editor chell
#28.02.2026

from colorama import Fore, Style
from multiprocessing.connection import Client
from engine.structures.Gen import DNA, Actions
import sys, select, time





def open_editor():

    editor_text = Fore.YELLOW + "======================\nGENETIC EDITOR\n======================" + Style.RESET_ALL

    conn_editor = Client(("localhost", 6000))

    mgs = []
    act = []
    inf = []


    print(editor_text)

    print("USER: > ", end=" ", flush=True)
    while True:
        # Messages
        if conn_editor and conn_editor.poll():
            msg = conn_editor.recv()
            if msg["flag"] == "recv":
                print("\r[MAIN] connected")
                conn_editor.send({"flag": "recv"})

            elif msg == "e":
                break
            print("USER: > ", end=" ", flush=True)


        # Inputs and processing
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                continue

            # Execution of the request
            elif cmd[0] == "add":
                if len(cmd) > 1:
                    flags = list(cmd[1])
                    for i in flags:
                        if i == "m":
                            mgs.append(add_morphogen())
                        elif i == "a":
                            act.append(add_action())
                        elif i == "i":
                            inf.append(add_information())
                        else:
                            print(f"\r{Fore.YELLOW}[SYSTEM]: UNKNOWN FLAG: {i}\n{Style.RESET_ALL}")
                        
            # Genetic compilation
            elif cmd[0] == "comp":
                compilation(conn_editor, mgs, act, inf)

            elif cmd[0] == 'exit':
                return 0
            

            else:
                print(f"\r{Fore.YELLOW}[SYSTEM]: UNKNOWN COMMAND: {"".join(cmd)}{Style.RESET_ALL}")
            
            cmd.clear()

            print("USER: > ", end=" ", flush=True)
        time.sleep(0.1)



                
                



def add_morphogen():
    print(Fore.RED + "MORPHOGEN"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text
    Distribution = input("Enter distribution: ") # 1 2 3 4 5 6
    Condition = input("Enter condition: ") # < S1 S2
    Action = input("Enter action: ")

    M = [Name, Distribution, Condition, Action]
    for i in range(len(M)):
        if M[i] == "":
            M[i] = 0 

    return M

def add_action():
    print(Fore.RED+"ACTION"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text
    Action = input("Enter action: ") # Action [Information]
    Timer = input("Enter timer: ") # 0 - 5

    A = [Name, Action, Timer]
    for i in range(len(A)):
        if A[i] == "":
            A[i] = 0 
    
    return A

    


def add_information():
    print(Fore.RED+"INFORMATION"+Style.RESET_ALL)
    Name = input("Enter name: ") # Text

    I = [Name]
    for i in range(len(I)):
        if I[i] == "":
            I[i] = 0 
    
    return I

def compilation(conn_editor, mgs, act, inf):
    msg = {
        "flag": "c",
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
        if isinstance(temp, Actions):
            DNA_text.append(f"{Fore.RED}[{Mg[i].M_name}{Style.RESET_ALL} -> {Fore.YELLOW}{temp.A_name}{Fore.RED}]{Style.RESET_ALL}")
        else:
            DNA_text.append(f"{Fore.RED}[{Mg[i].M_name}{Style.RESET_ALL} -> {Fore.YELLOW}{temp}{Fore.RED}]{Style.RESET_ALL}")

    for i in range(len(Ac)):
        DNA_text.append(f"{Fore.YELLOW}[{Ac[i].A_name}{Style.RESET_ALL} ->{Fore.GREEN} {Ac[i].A}{Fore.YELLOW}]{Style.RESET_ALL}")

    for i in range(len(inf)):
        DNA_text.append(f"[{inf[i].N}]")

    for i in range(len(DNA_text)):
        print(DNA_text[i], end=" ")
    print("\n")



if __name__ == "__main__":
    open_editor()

