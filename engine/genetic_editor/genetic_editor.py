import subprocess
import os
import sys

def open_editor():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    shell_path = os.path.join(current_dir, "editor_shell.py")

    return subprocess.Popen(
        ["xterm",
         "-geometry", "180x60",
         "-e", sys.executable, shell_path]
    )