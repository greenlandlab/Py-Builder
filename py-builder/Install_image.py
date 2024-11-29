import os , sys

image_file = sys.argv[1]
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

os.system(f"sudo mv {image_file} /etc/py-builder/packages")
print(f"{colors['BLUE']} Finished compiling file... To run it do 'py-builder run 'your project name here' 'yaml file name here (only file name since its done installing)")
