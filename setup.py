import cx_Freeze,os,sys
from cx_Freeze import setup, Executable
options = {"include_files":["MechaMecha_World_Championship.ico"],
           "packages":["pygame"],
           "add_to_path": True}
base = None
icone = None
if (sys.platform == "win32"):
    options["include_msvcr"] = True
    base = "Win32GUI"
    icone = "MechaMecha_World_Championship.ico"
os.environ['TCL_LIBRARY'] = r'C:\Users\Pixel\AppData\Local\Programs\Python\Python38\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Pixel\AppData\Local\Programs\Python\Python38\tcl\tk8.6'

setup(
    version = "1.0",
    description = "Un jeu de ChromaGate",
    options = {"build_exe":options},
    name = "MechaMecha World_Championship",
    executables = [cx_Freeze.Executable("MechaMecha_World_Championship.py",base=base,icon=icone)]
    )
