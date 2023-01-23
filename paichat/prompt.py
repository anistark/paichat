from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def start_chat():
    input_cmd = input(f"{Fore.LIGHTBLUE_EX}>>>{Style.RESET_ALL} ")
    
    # output
    print("\n"+input_cmd)
