import os
import sys
from questao4_styles import * 

IGNORE_PREFIX = [".", "__"]

def print_dir(path, depth=0, max_depth=10, show_full_dirname=False, style=DEFAULT_STYLE):
    
    # Definições de estilização
    spacer = (
        style.get("spacer_prefix")+
        (style.get("spacer_str")*style.get("spacer_thickness"))+
        style.get("spacer_sufix")
        ) *depth 

    def print_styled(str, is_file=False, is_dir=False):
        if is_file:
            print_styled(style.get("file_prefix") + str + style.get("file_sufix"))
        elif is_dir:
            print_styled(style.get("dir_prefix") + str + style.get("dir_sufix"))
        else:
            print(spacer + str)
    
    # Limite de recursão
    if max_depth and depth > max_depth:
        return

    # Ordem alfabetica
    itens = os.listdir(path) 
    itens.sort() 
    
    for item in itens:
        item_path = os.path.join(path, item)
        
        # Ignor arquivos escondidos
        if any(item.startswith(p) for p in IGNORE_PREFIX): 
            continue

        if not os.path.isdir(item_path):
            print_styled(item, is_file=True)

        else:
            if show_full_dirname:
                print_styled(item_path, is_dir=True)
            else:
                print_styled(item, is_dir=True)

            print_dir(item_path, depth+1, max_depth, show_full_dirname, style)

    if(style.get("end_dir") and len(itens)>0):
        print_styled(style.get("end_dir"))

if __name__ == "__main__":
    current_path = os.getcwd()
    depth = 10
    if len(sys.argv) > 1:
        current_path = current_path = os.path.abspath(sys.argv[1])
    if len(sys.argv) > 2:
        depth = int(sys.argv[2])
    
    print_dir(current_path, max_depth=depth, style=DEFAULT_STYLE)