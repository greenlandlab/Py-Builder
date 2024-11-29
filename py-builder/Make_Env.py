import sys , yaml , os

name = sys.argv[1]
package = sys.argv[2]
colors = { "BLACK": "\033[0;30m", "RED": "\033[0;31m", "GREEN": "\033[0;32m", "YELLOW": "\033[0;33m", 
           "BLUE": "\033[0;34m", "MAGENTA": "\033[0;35m", "CYAN": "\033[0;36m", "WHITE": "\033[0;37m", 
           "RESET": "\033[0m", "BOLD_BLACK": "\033[1;30m", "BOLD_RED": "\033[1;31m", "BOLD_GREEN": "\033[1;32m", 
           "BOLD_YELLOW": "\033[1;33m", "BOLD_BLUE": "\033[1;34m", "BOLD_MAGENTA": "\033[1;35m", "BOLD_CYAN": "\033[1;36m", 
           "BOLD_WHITE": "\033[1;37m", "UNDERLINE_BLACK": "\033[4;30m", "UNDERLINE_RED": "\033[4;31m", 
           "UNDERLINE_GREEN": "\033[4;32m", "UNDERLINE_YELLOW": "\033[4;33m", "UNDERLINE_BLUE": "\033[4;34m", 
           "UNDERLINE_MAGENTA": "\033[4;35m", "UNDERLINE_CYAN": "\033[4;36m", "UNDERLINE_WHITE": "\033[4;37m", 
           "BACKGROUND_BLACK": "\033[40m", "BACKGROUND_RED": "\033[41m", "BACKGROUND_GREEN": "\033[42m", 
           "BACKGROUND_YELLOW": "\033[43m", "BACKGROUND_BLUE": "\033[44m", "BACKGROUND_MAGENTA": "\033[45m", 
           "BACKGROUND_CYAN": "\033[46m", "BACKGROUND_WHITE": "\033[47m", "BOLD_BACKGROUND_BLACK": "\033[1;40m", 
           "BOLD_BACKGROUND_RED": "\033[1;41m", "BOLD_BACKGROUND_GREEN": "\033[1;42m", "BOLD_BACKGROUND_YELLOW": "\033[1;43m", 
           "BOLD_BACKGROUND_BLUE": "\033[1;44m", "BOLD_BACKGROUND_MAGENTA": "\033[1;45m", "BOLD_BACKGROUND_CYAN": "\033[1;46m", 
           "BOLD_BACKGROUND_WHITE": "\033[1;47m"}

os.system(f"mkdir {name}")

with open(f"/opt/py-builder/packages/{package}.yaml") as file_obj:
    data = yaml.load(file_obj, yaml.FullLoader)
    splitted = data['Commands'].split(" %$thisstringisonlyusedforslpittingandnotanythingelseoritwillerror$% ")
    
    for command in splitted: 
        split_local = command.split(" ")

        if split_local[2] and split_local[0] == "NEW_FILE" and split_local[2] == "WITHIN" :
            os.system(f"cd {name}")
            os.system(f"cd {split_local[3]}")
            os.system(f"touch {split_local[1]}")
            print(f"{colors['GREEN']} Successfully Created & Loaded File {split_local[1]} | dir=./{name}/{split_local[3]}")
            os.system(f"cd ..")
        elif split_local[0] == "NEW_FILE":
            os.system(f"cd {name}")
            os.system(f"cd {name} && touch {split_local[1]}")
            os.system(f"cd .. && echo \"{colors['GREEN']} Successfully Created & Loaded file {split_local[1]} | dir=./{name} {colors['RESET']}\"")  
        if split_local[2] and split_local[0] == "NEW_DIR" and split_local[2] == "WITHIN" :
            os.system(f"cd {name}")
            os.system(f"cd {split_local[3]}")
            os.system(f"mkdir {split_local[1]}")
            print(f"{colors['GREEN']} Successfully Created & Loaded Folder {split_local[1]} | dir=./{name}/{split_local[3]}")
            os.system(f"cd ..")
        elif split_local[0] == "NEW_DIR":
            os.system(f"cd {name}")
            os.system(f"mkdir {split_local[1]}")
            os.system(f"cd .. && {colors['GREEN']} Successfully Created & Loaded folder {split_local[1]} | dir=./{name} {colors['RESET']}")

print(f"{colors['BLUE']}Returned from installation env. Setup finished")