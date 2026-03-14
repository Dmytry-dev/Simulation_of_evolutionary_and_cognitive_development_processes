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
    menu_text = Fore.YELLOW + "======================\nMENU\n======================\n" + Style.RESET_ALL

    listener_editor = Listener(("localhost", 6000))
    listener_simulation = Listener(("localhost", 6001))

    conn_editor = None
    conn_simulation = None

    open_simulation = False
    open_editor = False

    

    print(menu_text)


    while True:

        #Mesages
        if conn_editor and conn_editor.poll():
            try:
                msg = conn_editor.recv()
                if msg["flag"] == "-c":
                    genetic_code = genetic_compiler.compilation(msg["mgs"], msg["act"], msg["inf"])
                    conn_editor.send(genetic_code)
                    
            except EOFError:
                print("\n[EDITOR] disconnected\n")
                conn_editor.close()
                conn_editor = None


        # Input
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                continue
                
            # Main
            if cmd[0] == "pr":
                if cmd[1] == "-e":
                    break

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
            
            # Manual
            elif cmd[0] == "-i":
                print("Information")

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
                    open_editor = True

                elif cmd[1] == "-e":
                    conn_editor.send("-e")
                    open_editor = False
        
        time.sleep(0.1)



    if open_simulation == True:
        conn_simulation.send("-e")
        sim_p.join()
    if open_editor == True:
        conn_editor.send("-e")

    return 0

    
if __name__ == "__main__":
    main()