import os
import typer
from colorama import init as colorama_init
from colorama import Fore
import configparser

config_path = os.path.expanduser('~')+'/.openai'

def check_config(config_path=config_path):
    print(f"{Fore.RED}Initiating Paichat...")
    config = []
    # Check config setup
    isExist = os.path.exists(config_path)
    if isExist:
        # Fetch config
        config = get_config(config_path)
    return config

def get_config(config_path=config_path):
    config = configparser.ConfigParser()
    config.sections()
    config.read(config_path)
    return config['OPENAI']

def set_config(config_path=config_path):
    print(f"{Fore.GREEN}We could not locate your OpenAI Key. We need that to proceed. You can get your OpenAI Key from https://beta.openai.com/ and go to Manage Keys.")
    openai_key = typer.prompt(f"\n{Fore.LIGHTBLUE_EX}Put here OpenAI Key here")
    print(openai_key)
    with open(config_path, 'w') as f:
        f.write('[OPENAI]\n')
        f.write('OPENAI_API_KEY='+openai_key)
