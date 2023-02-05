from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from pathlib import Path
import sys, os

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from .openchat import gpt_completion, gpt_image
from .config import check_config, set_config

colorama_init()

def start_chat():
    # Clearing the Screen
    os.system('cls' if os.name == 'nt' else 'clear')
    config_set = check_config()
    if 'OPENAI_API_KEY' not in config_set:
        set_config()
    chatgpt()

def chatgpt():
    input_prompt = input(f"\n{Fore.LIGHTBLUE_EX}Me: {Style.RESET_ALL} ")
    if (input_prompt == 'exit'):
        # Unless exit
        input_prompt = input(f"\n{Fore.GREEN}Thanks for using PaiChat! \nLet me know what can I build next: twitter.com/kranirudha{Style.RESET_ALL} \n")
        sys.exit(0)
    else:
        # Process input
        gpt_completion(input_prompt)
        chatgpt()
