
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
WHITE   = "\033[37m"
GRAY    = "\033[90m"

BOLD      = "\033[1m"
COLUMN_80 = "\033[80G"
UNDERLINE = "\033[4m"
RESET     = "\033[0m" 

def col(n):
    return f"\033[{n}G"

def styled(str, *args):
    return "".join([*args, str, RESET])

DEFAULT_STYLE = {
    "spacer_str":" ", 
    "spacer_thickness":1, 
    "spacer_prefix":styled("│", GRAY), 
    "spacer_sufix":"", 
    "file_prefix": styled("├", GRAY) + styled(" • ", YELLOW), 
    "file_sufix": styled("[file]", GRAY, col(70)), 
    "dir_prefix": styled("├", GRAY) + styled(" ▾ ", GREEN) , 
    "dir_sufix":"/", 
    "end_dir":  styled("└─⚬", GRAY)
}

DOTED_STYLE = {
    "spacer_str":" ", 
    "spacer_thickness":2, 
    "spacer_prefix":"┆", 
    "spacer_sufix":"", 
    "file_prefix":"┕ ", 
    "file_sufix":"", 
    "dir_prefix":"┕ ", 
    "dir_sufix":"/", 
    "end_dir":None 
}

CLEAN_STYLE = {
    "spacer_str":" ", 
    "spacer_thickness":3, 
    "spacer_prefix":"", 
    "spacer_sufix":"", 
    "file_prefix":"⤷ ", 
    "file_sufix":"", 
    "dir_prefix":"⤷ ", 
    "dir_sufix":"", 
    "end_dir":None 
}