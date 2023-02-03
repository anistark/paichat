import os
from dotenv import load_dotenv
import openai
import webbrowser
from colorama import init as colorama_init
from colorama import Fore

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def list_engines():
    # list engines
    engines = openai.Engine.list()

    # print the first engine's id
    print(engines.data[0].id)

def gpt_completion(prompt):
    # create a completion
    completion = openai.Completion.create(engine="ada", prompt="Hello world")
    # print the completion
    print("GPT:", completion.choices[0].text)

def gpt_image(prompt):
    # create a completion
    image = openai.Image.create(prompt="Hello world", n=4, size="256x256")
    # print the completion
    print(f"{Fore.LIGHTGREEN_EX}GPT: Your image is opening in default web browser...")
    webbrowser.open(image.data[0].url)
