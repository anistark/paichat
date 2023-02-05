# Python Open AI CLI Client [Un-official]

Published on pypi: https://pypi.org/project/paichat/
![PyPI - Downloads](https://img.shields.io/pypi/dm/paichat?style=for-the-badge) ![PyPI](https://img.shields.io/pypi/v/paichat?style=for-the-badge) ![PyPI - Format](https://img.shields.io/pypi/format/paichat?style=for-the-badge)

Supported ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/paichat?style=for-the-badge)

A Terminal Tool in Python

## Prerequisites
- `pipx`. If you don't have pipx installed, you can install like this:
  - `python3 -m pip install --user pipx`
  - `python3 -m pipx ensurepath`
- You'll also need to have your own OpenAi apikey:
  - Go to https://beta.openai.com/
  - Select you profile menu and go to Manage API Keys
  - Select + Create new secret key
  - Copy generated key

## Install:
`pipx install paichat`

## Usage:
`paichat --help`

```sh
 Usage: paichat [OPTIONS]

╭─ Options ───────────────────────────────────────╮
│ --help          Show this message and exit.     │
╰─────────────────────────────────────────────────╯
```

## Contribute:

![PyPI - License](https://img.shields.io/pypi/l/paichat?style=for-the-badge)

### Dev:

Start a virtualenv using poetry: `poetry shell`

If `poetry shell` does not activate the virtualenv, then use this:
`source $(poetry env info --path)/bin/activate`
When you're done, exit virtualenv shell: `deactivate`
