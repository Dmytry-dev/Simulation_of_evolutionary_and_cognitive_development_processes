#Dmytry-dev
#08.03.2025

from colorama import Fore, Style
from multiprocessing import Process
from multiprocessing.connection import Listener
import subprocess, sys, select, time


from engine.genetic_editor.editor_shell import open_editor
from engine.simulation import simulation_start


def main():
    menu_text = Fore.YELLOW + "======================\nMENU\n======================\n" + Style.RESET_ALL

    listener_editor = Listener(("localhost", 6000))
    listener_simulation = Listener(("localhost", 6001))

    conn_editor = None
    conn_simulation = None

    open_simulation = False
    open_editor = False
    

    print(menu_text)
    print("User: >", end=" ", flush=True)


    while True:

        #Mesages
        if conn_editor and conn_editor.poll():
            try:
                msg = conn_editor.recv()
                if msg == 1:
                    print("[EDITOR] connected\n")
                    conn_editor.send(1)

            except EOFError:
                print("\n[EDITOR] disconnected\n")
                conn_editor.close()
                conn_editor = None
            print("User: >", end=" ", flush=True)


        # Input
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().split()

            if not cmd:
                print("User: >", end=" ", flush=True)
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
                        "python3 engine/genetic_editor/editor_shell.py"
                    ])
                    conn_editor = listener_editor.accept()

                elif cmd[1] == "-e":
                    conn_editor.send("-e")
            print("User: >", end=" ", flush=True)
        
        time.sleep(0.1)



    if open_simulation == True:
        conn_simulation.send("-e")
        sim_p.join()

    return 0

    
if __name__ == "__main__":
    main()