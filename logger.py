from interface_txt import * 
from datetime import *

def write_log(dir):
    dt = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    dir.insert(0,dt)
    dir[-1] =f'{dir[-1]}\n'
    result = ";".join(dir)
    with open('log.txt','a',encoding='UTF8') as f:
        f.write(result)
    