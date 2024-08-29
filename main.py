import os
import datetime
import json
import random
from git import Repo

config_path = '/home/rbouard/dev/ahahah/daily-commit-python/config.json'

# Load Conf
with open(config_path) as config_file:
    config = json.load(config_file)

repo_path = config['repo_path']
readme_path = os.path.join(repo_path, config['readme_path'])
commit_prefix = config['commit_prefix']

# List of animals for the commit message
animals = [
    "Lion", "Tiger", "Bear", "Fox", "Deer", "Wolf", "Monkey", "Zebra",
    "Elephant", "Giraffe", "Shark", "Panther", "Lynx", "Hippopotamus",
    "Rhinoceros", "Cheetah", "Leopard", "Crocodile", "Snake", "Eagle",
    "Owl", "Penguin", "Hedgehog", "Turtle", "Dolphin", "Orca",
    "Camel", "Llama", "Pony"
]

# List of gemstones for the commit message
gemstones = [
    "Diamond", "Ruby", "Sapphire", "Emerald", "Opal", "Amethyst",
    "Topaz", "Garnet", "Jade", "Pearl", "Turquoise", "Onyx",
    "Citrine", "Quartz", "Peridot", "Alexandrite", "Obsidian",
    "Lapis Lazuli", "Tanzanite", "Aquamarine", "Tourmaline",
    "Malachite", "Chrysoprase", "Spinel"
]

# Generate a random animal name and gemstone
random_animal = random.choice(animals)
random_gemstone = random.choice(gemstones)

# Open the repository
repo = Repo(repo_path)

# Read the README.md content and replace the last update line or append a new one
update_line = f'Update on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'

with open(readme_path, 'r') as readme_file:
    lines = readme_file.readlines()

if lines and lines[-1].startswith('Update on'):
    lines[-1] = update_line
else:
    lines.append(update_line)

with open(readme_path, 'w') as readme_file:
    readme_file.writelines(lines)

# Add README.md to the index
repo.index.add([readme_path])

# Create a commit
commit_message = f'{commit_prefix} {random_gemstone} {random_animal}'
repo.index.commit(commit_message)

# Check the current status
print("Current Status:")
print(repo.git.status())

# Push the changes to the remote repository
try:
    origin = repo.remote(name='origin')
    origin.push()
except Exception as e:
    print(f"Error while pushing: {e}")
