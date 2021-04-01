# DiabetesWithMachineLearn

Analise Exploratória de Casos de Diabetes 
O modelo utilizado nessa demo, foi copiado do repositorio abaixo.
https://github.com/cicerojmm/analiseCasosDiabetesComML

O intuito dessa demo é utilizar o modelo de ML apresentado acima em uma aplicação desktop simple desenvolvida em pyhton. 

## Usage

```bash
# Run script
python part_manager.py

# Compiled with Pyinstaller
# Windows
pyinstaller --onefile --windowed part_manager.py

# MacOS
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
```
