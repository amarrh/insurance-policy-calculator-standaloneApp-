
import sys # Imports are automatically detected (normally) in the script to freeze
import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\tcl\\tcl8.6"
os.environ['TIX_LIBRARY'] = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\tcl\\tix8.4.3"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("Obracun_registracije_vozila.py", base="Win32GUI", icon="thumb.ico")]

cx_Freeze.setup(
        name = "Obračun registracije vozila",
        options = {"build_exe":{"packages": ["tkinter"], "include_files":["icons/", "podaci/", "obracun/",
                                "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs\\tcl86t.dll",
                                "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs\\tk86t.dll"], }},
        version="0.01",
        executables=executables)



