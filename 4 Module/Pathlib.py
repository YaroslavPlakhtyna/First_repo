#from pathlib import *
#current_dir = Path.cwd()
#home_dir = Path.home()
#print(current_dir)
#print(home_dir)

from pathlib import Path
p = Path('C:/Users/plakh/OneDrive/Documentos/GitHub/First_repo')  # p Вказує на теку /home/user/Downloads
for i in p.iterdir():
    print(i.name)