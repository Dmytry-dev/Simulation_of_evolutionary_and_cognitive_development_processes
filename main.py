#Dmytry-dev
#08.03.2025

from colorama import Fore, Style
from multiprocessing import Process
from multiprocessing.connection import Listener
import subprocess, sys, select, time


from engine.genetic_editor.editor_shell import open_editor
from engine.simulation import simulation_start
from engine.structures.Gen import DNA 
from engine.structures import genetic_compiler


def main():
    menu_text = Fore.YELLOW + "======================\nMENU\n======================\n" + Style.RESET_ALL + "For help information enter " + Fore.YELLOW +"pr -i\n"+ Style.RESET_ALL
    help_text = """\nMain commands:\npr – commands for the main terminal\nsim – commands for the simulation\ned – commands for the genetic editor terminal\n
Flags for the main terminal:\n-e – exit\n-i – help\n
Commands for the genetic editor:\n-s – start\n-e – exit\n
Commands for the editor terminal:\nadd – add a DNA element\nm/a /i – add a morphogen, action, or information cell\ncom – compile the gene chain\n"""

    listener_editor = Listener(("localhost", 6000))
    listener_simulation = Listener(("localhost", 6001))

    conn_editor = None
    conn_simulation = None

    open_simulation = False
    open_editor = False

    

    print(menu_text)
    print("USER: > ", end=" ", flush=True)

    while True:

        #Mesages
        if conn_editor and conn_editor.poll():
            try:
                msg = conn_editor.recv()
                if msg["flag"] == "c":
                    genetic_code = genetic_compiler.compilation(msg["mgs"], msg["act"], msg["inf"])
                    conn_editor.send(genetic_code)
                if msg["flag"] == "recv":
                    print("\r[EDITOR] connected")
                    print("USER: > ", end=" ", flush=True)

                    
            except EOFError:
                print("\r[EDITOR] disconnected")
                conn_editor.close()
                conn_editor = None
                print("USER: > ", end=" ", flush=True)



        # Input
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                continue
                
            # Main
            if cmd[0] == "pr":
                if cmd[1] == "-e":
                    break
                # Manual
                elif cmd[1] == "-i":
                    print(help_text)

            # Simulation
            elif cmd[0] == "sim":
                # Open simulation
                if cmd[1] == "-s":

                    sim_p = Process(target=simulation_start)
                    sim_p.start()
                    conn_simulation = listener_simulation.accept()
                    open_simulation = True

                # Close simulation
                elif cmd[1] == "-e":
                    conn_simulation.send("-e")
                    sim_p.join()
            


            # Editor
            elif cmd[0] == "ed":
                # Open Editor
                if cmd[1] == "-s":
                    subprocess.Popen([
                        "xterm",
                        "-e",
                        "bash",
                        "-c",
                        "python3 -m engine.genetic_editor.editor_shell; echo; echo 'PRESS ENTER'; read"
                    ])
                    conn_editor = listener_editor.accept()
                    conn_editor.send({"flag": "recv"})
                    open_editor = True

                elif cmd[1] == "-e":
                    conn_editor.send("-e")
                    open_editor = False


            else:
                print(f"\r{Fore.YELLOW}[SYSTEM]: UNKNOWN COMMAND: {"".join(cmd)}{Style.RESET_ALL}")
        
            print("USER: > ", end=" ", flush=True)
        time.sleep(0.1)



    if open_simulation == True:
        conn_simulation.send("e")
        sim_p.join()
    if open_editor == True:
        conn_editor.send("e")

    return 0

    
if __name__ == "__main__":
    main()