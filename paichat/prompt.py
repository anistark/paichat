from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from pathlib import Path
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from .openchat import gpt_completion, gpt_image

colorama_init()

def start_chat():
    input_prompt = input(f"\n{Fore.LIGHTBLUE_EX}Me: {Style.RESET_ALL} ")
    # print("\n"+input_prompt)
    # Process input
    gpt_image(input_prompt)
    # Unless exit
    start_chat()
